---
name: env-audit
description: Audit OS binaries, CVEs, EOL risks, upstream versions, and generate upgrade commands.
---

# Terminal Environment & Security Audit Skill (`env-audit`)

## Objective & Priority
Act as a Senior System Security Auditor to inspect host OS binaries, audit installed tool CVEs/EOL risks against endoflife.date lifecycle standards, compare versions against native package managers, and generate targeted upgrade commands.

Priority Rules: `Dynamic OS Routing > Package Manager Querying > Risk Filtering > Targeted Repair`

## Execution Steps

### Step 1: Dynamic Environment Discovery & Target Inspection
- Action: Execute the OS-dispatching audit router script to extract host details, functional installed binaries, and package manager candidates in JSON format:
  ```bash
  python3 <skill_dir>/scripts/audit.py
  ```
- Completion Criterion: Exit code 0 with valid JSON containing host OS, functional binaries, and vulnerability status.

### Step 2: Real-Time Upstream & Vulnerability Assessment
- Action: Parse inspection JSON, query native package manager candidates (`apt policy`, `dnf info`, `brew info`), and evaluate security risk status against synchronized endoflife.date rules.
- Completion Criterion: Package manager versions and EOL statuses are fully evaluated.

### Step 3: Render Structured Audit Report
- Action: Output a 3-part structured audit report:
  1. **System & Binary Inventory**: Render a SINGLE consolidated table for all discovered binaries (`Category`, `Component`, `Installed Version`, `Recommended LTS Version`, `Status` as `PASS`/`FAIL`).
  2. **CVE & Risk Summary**: Audit all components from Part 1. **ONLY display items marked as FAIL**.
  3. **Targeted Maintenance & Upgrade Commands**: Provide exact commands **ONLY for FAIL items in Part 2**, structured by (1) official package repository setup, (2) native package manager upgrade, and (3) verification.
- Completion Criterion: 3-part report rendered cleanly without redundant clean-item noise.
