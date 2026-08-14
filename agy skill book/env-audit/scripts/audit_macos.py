#!/usr/bin/env python3
"""
macOS Environment & Security Audit Script (Ultra-Lightweight Engine)
Reads tool registry from targets.json and executes native macOS / Homebrew queries.
"""
import os
import shutil
import platform
import subprocess
import json
import re

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
TARGETS_FILE = os.path.join(SCRIPT_DIR, "targets.json")

def get_os_info():
    arch = platform.machine()
    try:
        ver = subprocess.check_output(["sw_vers", "-productVersion"], text=True).strip()
        product_name = subprocess.check_output(["sw_vers", "-productName"], text=True).strip()
        return f"{product_name} {ver}", f"Darwin ({arch})", "macos"
    except Exception:
        return "macOS", f"Darwin ({arch})", "macos"

def get_tool_version(tool_item):
    name = tool_item["name"]
    path = shutil.which(name)
    if not path or path.startswith("/Volumes/") or path.startswith("/mnt/"):
        return None
    
    env = dict(os.environ, DISPLAY="", WAYLAND_DISPLAY="", SUDO_ASKPASS="/bin/false", SUDO_NONINTERACTIVE="true")
    ver = "Installed"
    flags = tool_item.get("flags", ["--version", "-v", "version"])
    for flag in flags:
        try:
            cmd = [path] + flag.split()
            proc = subprocess.run(cmd, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=1.0, env=env, start_new_session=True)
            out = proc.stdout.strip() if proc.stdout else ""
            if proc.returncode == 0 and out and not any(err in out.lower() for err in ["usage:", "password for", "invalid option", "unknown option", "xcode-select: error"]):
                ver = out.split("\n")[0]
                break
        except Exception:
            continue
            
    lts = tool_item.get("lts", "Latest")
    is_eol = False
    eol_below = tool_item.get("eol_below")
    if eol_below and ver != "Installed":
        m = re.search(r"(\d+)\.(\d+)", ver)
        if m:
            try:
                major, minor = int(m.group(1)), int(m.group(2))
                if (major, minor) < tuple(eol_below):
                    is_eol = True
            except Exception:
                pass
                
    return {
        "path": path,
        "version": ver,
        "category": tool_item.get("category", "General"),
        "recommended_lts": lts,
        "is_eol": is_eol
    }

def attach_brew_info(results):
    brew_path = shutil.which("brew")
    if not brew_path:
        return
    try:
        proc = subprocess.run([brew_path, "outdated", "--json"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=3)
        outdated_set = set()
        if proc.returncode == 0 and proc.stdout.strip():
            data = json.loads(proc.stdout)
            formulae = data.get("formulae", [])
            outdated_set = {item.get("name") for item in formulae}
        
        for k, data in results.items():
            is_eol = data.get("is_eol", False)
            is_outdated = k in outdated_set or is_eol
            data["is_upgradable"] = is_outdated
            data["pkg_manager"] = {
                "brew_package": k,
                "is_outdated": is_outdated
            }
    except Exception:
        pass

def main():
    os_name, kernel, family = get_os_info()
    targets = []
    if os.path.exists(TARGETS_FILE):
        with open(TARGETS_FILE) as f:
            targets = json.load(f)

    results = {}
    for item in targets:
        info = get_tool_version(item)
        if info:
            results[item["name"]] = info

    attach_brew_info(results)

    report = {
        "os_name": os_name,
        "kernel": kernel,
        "family": family,
        "shell": os.environ.get("SHELL", "/bin/zsh"),
        "detected_count": len(results),
        "installed_binaries": results,
        "cve_vulnerabilities": []
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
