#!/usr/bin/env python3
"""
Terminal Environment Audit Router
Dynamically detects host OS and dispatches execution to audit_macos.py or audit_linux.py.
"""
import sys
import os
import platform

def main():
    system = platform.system()
    script_dir = os.path.dirname(os.path.realpath(__file__))
    
    if system == "Darwin":
        target_script = os.path.join(script_dir, "audit_macos.py")
    elif system == "Linux":
        target_script = os.path.join(script_dir, "audit_linux.py")
    else:
        print(f'{{"error": "Unsupported OS platform: {system}"}}')
        sys.exit(1)
        
    if not os.path.exists(target_script):
        print(f'{{"error": "Audit script not found at {target_script}"}}')
        sys.exit(1)
        
    os.execv(sys.executable, [sys.executable, target_script] + sys.argv[1:])

if __name__ == "__main__":
    main()
