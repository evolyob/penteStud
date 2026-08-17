#!/usr/bin/env python3
"""
Linux Environment & Security Audit Script (Ultra-Lightweight Engine)
Reads tool registry from targets.json and executes native OS queries.
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
    distro = "Linux"
    family = "debian"
    if os.path.exists("/etc/os-release"):
        with open("/etc/os-release") as f:
            content = f.read().lower()
            for line in content.splitlines():
                if line.startswith("pretty_name="):
                    distro = line.split("=", 1)[1].strip('"\'\n')
            if any(x in content for x in ["rhel", "centos", "rocky", "fedora"]):
                family = "redhat"
    return distro, f"Linux ({platform.machine()})", family

def get_tool_version(tool_item):
    name = tool_item["name"]
    path = shutil.which(name)
    if not path or path.startswith("/mnt/"):
        return None
    
    env = dict(os.environ, DISPLAY="", WAYLAND_DISPLAY="", SUDO_ASKPASS="/bin/false", SUDO_NONINTERACTIVE="true")
    ver = "Installed"
    flags = tool_item.get("flags", ["--version", "-v", "version"])
    for flag in flags:
        try:
            cmd = [path] + flag.split()
            proc = subprocess.run(cmd, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=1.0, env=env, start_new_session=True)
            out = proc.stdout.strip() if proc.stdout else ""
            if proc.returncode == 0 and out and not any(err in out.lower() for err in ["usage:", "password for", "invalid option", "unknown option"]):
                ver = out.split("\n")[0]
                break
        except Exception:
            continue
            
    # Evaluate EOL against endoflife.date rule
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

def get_outdated_packages(family):
    outdated = {}
    if family == "debian" and shutil.which("apt"):
        try:
            proc = subprocess.run(["apt", "list", "--upgradable"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=3)
            if proc.returncode == 0:
                for line in proc.stdout.splitlines():
                    if "upgradable from:" in line:
                        parts = line.split()
                        pkg_name = parts[0].split("/")[0]
                        candidate_ver = parts[1]
                        installed_ver = line.split("upgradable from:")[1].strip(" ]\n")
                        outdated[pkg_name] = {"installed": installed_ver, "candidate": candidate_ver}
        except Exception:
            pass
    elif family == "redhat":
        pkg_mgr = shutil.which("dnf") or shutil.which("yum")
        if pkg_mgr:
            try:
                proc = subprocess.run([pkg_mgr, "check-update", "--quiet"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
                if proc.returncode in (0, 100) and proc.stdout:
                    for line in proc.stdout.splitlines():
                        parts = line.strip().split()
                        if len(parts) >= 2:
                            pkg_name = parts[0].split(".")[0]
                            outdated[pkg_name] = {"candidate": parts[1]}
            except Exception:
                pass
    return outdated

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

    outdated_pkgs = get_outdated_packages(family)
    pkg_map = {"pip3": "python3-pip", "node": "nodejs"}
    
    for name, data in results.items():
        pkg_name = pkg_map.get(name, name)
        is_upgradable = pkg_name in outdated_pkgs
        is_eol = data.get("is_eol", False)
        candidate = outdated_pkgs[pkg_name]["candidate"] if is_upgradable else data["version"]
        
        data["is_upgradable"] = is_upgradable or is_eol
        data["candidate"] = candidate
        data["pkg_manager"] = {
            "pkg_package": pkg_name,
            "is_upgradable": is_upgradable or is_eol,
            "candidate": candidate
        }

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
        "shell": os.environ.get("SHELL", "/bin/bash"),
        "detected_count": len(results),
        "installed_binaries": results,
        "outdated_system_packages": outdated_pkgs,
        "npm_audit": npm_audit_data,
        "cve_vulnerabilities": cve_list
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
