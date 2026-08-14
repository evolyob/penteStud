#!/usr/bin/env python3
"""
Sync targets.json with live endoflife.date API
"""
import os
import json
import re
import datetime
import urllib.request
from concurrent.futures import ThreadPoolExecutor

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
TARGETS_FILE = os.path.join(SCRIPT_DIR, "targets.json")

def parse_cycle_version(cycle_str):
    m = re.findall(r"\d+", str(cycle_str))
    if len(m) >= 2:
        return (int(m[0]), int(m[1]))
    elif len(m) == 1:
        return (int(m[0]), 0)
    return None

def fetch_slug_data(slug):
    url = f"https://endoflife.date/api/{slug}.json"
    req = urllib.request.Request(url, headers={"User-Agent": "env-audit/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode())
            return slug, data, None
    except Exception as e:
        return slug, None, str(e)

def sync():
    if not os.path.exists(TARGETS_FILE):
        print(f"Error: {TARGETS_FILE} not found.")
        return

    with open(TARGETS_FILE, "r") as f:
        targets = json.load(f)

    slug_items = [t for t in targets if "eol_slug" in t]
    unique_slugs = list(set(t["eol_slug"] for t in slug_items))
    print(f"Fetching live data from endoflife.date for {len(unique_slugs)} targets...")

    slug_data_map = {}
    with ThreadPoolExecutor(max_workers=8) as ex:
        results = list(ex.map(fetch_slug_data, unique_slugs))
        for slug, data, err in results:
            if data:
                slug_data_map[slug] = data
            else:
                print(f"  [Warning] Failed to fetch {slug}: {err}")

    today = datetime.date.today().isoformat()
    updated_count = 0

    print("\nSynchronizing target definitions:")
    for item in targets:
        slug = item.get("eol_slug")
        if not slug or slug not in slug_data_map:
            continue

        cycles = slug_data_map[slug]
        # Sort cycles
        active_lts = []
        active_supported = []
        eol_cycles = []

        for c in cycles:
            eol_val = c.get("eol")
            cycle_name = str(c.get("cycle"))
            is_lts = bool(c.get("lts"))

            is_eol = False
            if isinstance(eol_val, str) and eol_val <= today:
                is_eol = True
            elif eol_val is True:
                is_eol = True

            if is_eol:
                eol_cycles.append(cycle_name)
            else:
                if is_lts:
                    active_lts.append(cycle_name)
                active_supported.append(cycle_name)

        old_lts = item.get("lts", "")
        if active_lts:
            new_lts = " / ".join(active_lts[:2]) + " LTS"
        elif active_supported:
            new_lts = " / ".join(active_supported[:2])
        else:
            new_lts = old_lts

        old_eol_below = item.get("eol_below")
        new_eol_below = old_eol_below
        if active_supported:
            lowest_supported = active_supported[-1]
            parsed = parse_cycle_version(lowest_supported)
            if parsed:
                new_eol_below = list(parsed)

        changed = False
        if new_eol_below and new_eol_below != old_eol_below:
            item["eol_below"] = new_eol_below
            changed = True

        if new_lts and new_lts != old_lts:
            item["lts"] = new_lts
            changed = True

        status_str = f"LTS: {item.get('lts')} | eol_below: {item.get('eol_below')}"
        if changed:
            updated_count += 1
            print(f"  [UPDATED] {item['name']} ({slug}) -> {status_str}")
        else:
            print(f"  [UP-TO-DATE] {item['name']} ({slug}) -> {status_str}")

    with open(TARGETS_FILE, "w", encoding="utf-8") as f:
        json.dump(targets, f, ensure_ascii=False, indent=2)

    print(f"\nSuccessfully synchronized! ({updated_count} targets updated, saved to targets.json)")

if __name__ == "__main__":
    sync()
