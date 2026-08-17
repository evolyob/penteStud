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
DEFAULT_TARGETS = [
  {
    "name": "python3",
    "category": "Languages & Runtimes",
    "eol_slug": "python",
    "lts": "3.14 / 3.13",
    "eol_below": [
      3,
      13
    ],
    "flags": [
      "--version",
      "-v"
    ]
  },
  {
    "name": "node",
    "category": "Languages & Runtimes",
    "eol_slug": "nodejs",
    "lts": "26 / 24 LTS",
    "eol_below": [
      24,
      0
    ],
    "flags": [
      "--version",
      "-v"
    ]
  },
  {
    "name": "go",
    "category": "Languages & Runtimes",
    "eol_slug": "go",
    "lts": "1.26 / 1.25",
    "eol_below": [
      1,
      25
    ],
    "flags": [
      "version",
      "--version"
    ]
  },
  {
    "name": "rustc",
    "category": "Languages & Runtimes",
    "eol_slug": "rust",
    "lts": "1.97",
    "flags": [
      "--version",
      "-v"
    ],
    "eol_below": [
      1,
      97
    ]
  },
  {
    "name": "java",
    "category": "Languages & Runtimes",
    "eol_slug": "oracle-jdk",
    "lts": "25 / 21 LTS",
    "eol_below": [
      21,
      0
    ],
    "flags": [
      "--version",
      "-version"
    ]
  },
  {
    "name": "ruby",
    "category": "Languages & Runtimes",
    "eol_slug": "ruby",
    "lts": "4.0 / 3.4",
    "eol_below": [
      3,
      3
    ],
    "flags": [
      "--version",
      "-v"
    ]
  },
  {
    "name": "perl",
    "category": "Languages & Runtimes",
    "eol_slug": "perl",
    "lts": "5.44 / 5.42",
    "eol_below": [
      5,
      40
    ],
    "flags": [
      "--version",
      "-v"
    ]
  },
  {
    "name": "php",
    "category": "Languages & Runtimes",
    "eol_slug": "php",
    "lts": "8.5 / 8.4",
    "eol_below": [
      8,
      4
    ],
    "flags": [
      "--version",
      "-v"
    ]
  },
  {
    "name": "dotnet",
    "category": "Languages & Runtimes",
    "eol_slug": "dotnet",
    "lts": "10 LTS",
    "eol_below": [
      10,
      0
    ],
    "flags": [
      "--version",
      "-v"
    ]
  },
  {
    "name": "clang",
    "category": "Compilers & Toolchains",
    "lts": "17.x / 16.x+",
    "eol_below": [
      15,
      0
    ],
    "flags": [
      "--version",
      "-v"
    ]
  },
  {
    "name": "make",
    "category": "Compilers & Toolchains",
    "lts": "4.4.x / 3.81+",
    "flags": [
      "--version",
      "-v"
    ]
  },
  {
    "name": "git",
    "category": "VCS & Code Quality",
    "lts": "2.55.x / 2.45+",
    "eol_below": [
      2,
      39
    ],
    "flags": [
      "--version",
      "-v"
    ]
  },
  {
    "name": "gh",
    "category": "VCS & Code Quality",
    "lts": "2.97.x",
    "flags": [
      "--version",
      "-v"
    ]
  },
  {
    "name": "jq",
    "category": "VCS & Code Quality",
    "lts": "1.8.x / 1.7.x",
    "flags": [
      "--version",
      "-v"
    ]
  },
  {
    "name": "openssl",
    "category": "Security & Cryptography",
    "eol_slug": "openssl",
    "lts": "3.5 / 3.0 LTS",
    "eol_below": [
      3,
      0
    ],
    "flags": [
      "version",
      "--version"
    ]
  },
  {
    "name": "dpkg",
    "category": "System & Package Managers",
    "lts": "1.22.x",
    "flags": [
      "--version",
      "-v"
    ]
  },
  {
    "name": "brew",
    "category": "System & Package Managers",
    "lts": "6.0.x / Latest",
    "flags": [
      "--version",
      "-v"
    ]
  },
  {
    "name": "ssh",
    "category": "System & Security",
    "lts": "10.x / 9.9p+",
    "flags": [
      "-V",
      "--version"
    ]
  },
  {
    "name": "sudo",
    "category": "System & Security",
    "lts": "1.9.17p+ / Stable",
    "eol_below": [
      1,
      9
    ],
    "flags": [
      "-V",
      "--version"
    ]
  },
  {
    "name": "rsync",
    "category": "System & File Utils",
    "lts": "3.5.x / 3.2+",
    "flags": [
      "--version",
      "-v"
    ]
  },
  {
    "name": "gitlab-runner",
    "category": "CI/CD & Automation",
    "eol_slug": "gitlab-runner",
    "lts": "19.2 / 19.1",
    "eol_below": [
      19,
      0
    ],
    "flags": [
      "--version",
      "-v"
    ]
  },
  {
    "name": "jenkins",
    "category": "CI/CD & Automation",
    "eol_slug": "jenkins",
    "lts": "2.568 LTS",
    "eol_below": [
      2,
      568
    ],
    "flags": [
      "--version",
      "-v"
    ]
  },
  {
    "name": "kong",
    "category": "Web & API Gateways",
    "eol_slug": "kong-gateway",
    "lts": "3.4 LTS",
    "eol_below": [
      3,
      4
    ],
    "flags": [
      "version",
      "--version"
    ]
  },
  {
    "name": "nginx",
    "category": "Web & API Gateways",
    "eol_slug": "nginx",
    "lts": "1.31 / 1.30",
    "eol_below": [
      1,
      30
    ],
    "flags": [
      "-v",
      "-V",
      "--version"
    ]
  },
  {
    "name": "mysql",
    "category": "Databases & Storage",
    "eol_slug": "mysql",
    "flags": [
      "--version",
      "-V",
      "-v"
    ],
    "eol_below": [
      8,
      4
    ],
    "lts": "9.7 / 8.4 LTS"
  },
  {
    "name": "mariadb",
    "category": "Databases & Storage",
    "eol_slug": "mariadb",
    "flags": [
      "--version",
      "-V",
      "-v"
    ],
    "eol_below": [
      10,
      11
    ],
    "lts": "12.3 / 11.8 LTS"
  },
  {
    "name": "mongod",
    "category": "Databases & Storage",
    "eol_slug": "mongodb",
    "flags": [
      "--version",
      "-v"
    ],
    "eol_below": [
      7,
      0
    ],
    "lts": "8.3 / 8.0"
  },
  {
    "name": "redis-server",
    "category": "Databases & Storage",
    "eol_slug": "redis",
    "flags": [
      "--version",
      "-v"
    ],
    "eol_below": [
      7,
      0
    ],
    "lts": "8.10 / 8.8"
  },
  {
    "name": "psql",
    "category": "Databases & Storage",
    "eol_slug": "postgresql",
    "flags": [
      "--version",
      "-V",
      "-v"
    ],
    "eol_below": [
      16,
      0
    ],
    "lts": "18 / 17"
  },
  {
    "name": "pip3",
    "category": "Package Managers & Tools",
    "lts": "26.x / 25.x+",
    "eol_below": [
      23,
      0
    ],
    "flags": [
      "--version",
      "-V"
    ]
  },
  {
    "name": "pipx",
    "category": "Package Managers & Tools",
    "lts": "1.16.x+",
    "flags": [
      "--version"
    ]
  },
  {
    "name": "npm",
    "category": "Package Managers & Tools",
    "lts": "11.x / 10.x+",
    "eol_below": [
      9,
      0
    ],
    "flags": [
      "--version",
      "-v"
    ]
  },
  {
    "name": "curl",
    "category": "Network & System Utils",
    "lts": "8.12.x / 8.7+",
    "eol_below": [
      7,
      80
    ],
    "flags": [
      "--version",
      "-V"
    ]
  },
  {
    "name": "docker",
    "category": "Containers & Cloud Native",
    "eol_slug": "docker-engine",
    "lts": "28.x / 27.x+",
    "flags": [
      "--version",
      "-v"
    ]
  }
]

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

def get_npm_audit():
    npm_path = shutil.which("npm")
    if not npm_path:
        return None
    cwd = os.getcwd()
    pkg_file = os.path.join(cwd, "package.json")
    if not os.path.exists(pkg_file):
        return None
    try:
        proc = subprocess.run([npm_path, "audit", "--json"], cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=8)
        out = proc.stdout.strip()
        if out:
            data = json.loads(out)
            metadata = data.get("metadata", {}).get("vulnerabilities", {})
            vulns = data.get("vulnerabilities", {})
            return {
                "package_json_dir": cwd,
                "total_vulnerabilities": sum(metadata.values()) if metadata else len(vulns),
                "severity_summary": metadata,
                "vulnerabilities": {
                    k: {
                        "name": v.get("name"),
                        "severity": v.get("severity"),
                        "isDirect": v.get("isDirect"),
                        "range": v.get("range"),
                        "fixAvailable": v.get("fixAvailable")
                    } for k, v in list(vulns.items())[:15]
                }
            }
    except Exception:
        pass
    return None

def main():
    os_name, kernel, family = get_os_info()
    targets = DEFAULT_TARGETS
    if os.path.exists(TARGETS_FILE):
        try:
            with open(TARGETS_FILE) as f:
                targets = json.load(f)
        except Exception:
            pass

    results = {}
    for item in targets:
        info = get_tool_version(item)
        if info:
            results[item["name"]] = info

    attach_brew_info(results)

    npm_audit_data = get_npm_audit()

    cve_list = []
    if npm_audit_data and npm_audit_data.get("total_vulnerabilities", 0) > 0:
        for k, v in npm_audit_data.get("vulnerabilities", {}).items():
            cve_list.append({
                "source": "npm_audit",
                "package": k,
                "severity": v.get("severity"),
                "fixAvailable": v.get("fixAvailable")
            })

    report = {
        "os_name": os_name,
        "kernel": kernel,
        "family": family,
        "shell": os.environ.get("SHELL", "/bin/zsh"),
        "detected_count": len(results),
        "installed_binaries": results,
        "npm_audit": npm_audit_data,
        "cve_vulnerabilities": cve_list
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
