"""
CI Verification Runner for UVCE Marvel Git-Task.

Verifies:
1. Test suite integrity (`testing.py`, `ci_check.py`, `my_task.py` unmodified).
2. Contributor's assigned functions for `--user <github_username>`.
3. Merge conflict resolution in `campus_registry.py` (`get_registered_clubs()` and
   `get_lab_operating_hours()`).
"""
import argparse
import os
import subprocess
import sys
import testing


REPO_DIR = os.path.dirname(os.path.abspath(__file__))


def git_show_file(ref: str, rel_path: str):
    """Return file content at git ref, or None if ref/file does not exist."""
    res = subprocess.run(
        ["git", "-C", REPO_DIR, "show", f"{ref}:{rel_path}"],
        capture_output=True,
        text=True,
    )
    if res.returncode != 0:
        return None
    return res.stdout


def find_base_ref(preferred_base: str = None) -> str:
    """Find a valid git base reference to compare protected files against."""
    candidates = []
    if preferred_base:
        candidates.append(preferred_base)
    candidates.extend(["origin/main", "upstream/main", "HEAD"])
    for ref in candidates:
        res = subprocess.run(
            ["git", "-C", REPO_DIR, "rev-parse", "--verify", ref],
            capture_output=True,
            text=True,
        )
        if res.returncode == 0:
            return ref
    return "HEAD"


def check_merge_conflict_status() -> tuple:
    """
    Check the state of `campus_registry.py`.
    Returns (status, message) where status is 'PASS', 'CONFLICT_MARKERS', or 'PENDING'.
    """
    reg_path = os.path.join(REPO_DIR, "campus_registry.py")
    with open(reg_path, "r", encoding="utf-8") as f:
        raw = f.read()
    if any(line.startswith(("<<<<<<<", "=======", ">>>>>>>")) for line in raw.splitlines()):
        return (
            "CONFLICT_MARKERS",
            "Git conflict markers (<<<<<<<, =======, >>>>>>>) are still present in "
            "`campus_registry.py`. Open `campus_registry.py`, combine both branches, "
            "and delete the marker lines.",
        )
    import campus_registry
    import importlib
    importlib.reload(campus_registry)
    clubs = campus_registry.get_registered_clubs()
    hours = campus_registry.get_lab_operating_hours()
    expected_clubs = ["MARVEL", "IEEE", "GDSC", "SAE"]
    expected_hours = {"weekday": "09:00-20:00", "weekend": "10:00-17:00"}
    if clubs == expected_clubs and hours == expected_hours:
        return ("PASS", "Merge conflict in `campus_registry.py` resolved.")
    if clubs == ["MARVEL", "IEEE"] and hours == {"weekday": "09:00-20:00"}:
        return (
            "PENDING",
            "You have not merged the practice conflict branch yet.\n"
            "  Next steps to complete Part 2:\n"
            "    1. Run: git fetch upstream   (or: git fetch origin)\n"
            "    2. Run: git merge upstream/merge-conflict-practice\n"
            "            (or: git merge origin/merge-conflict-practice)\n"
            "    3. Open `campus_registry.py`, combine both branches as shown in its\n"
            "       docstring, save the file, and re-run this command.",
        )
    return (
        "INCORRECT",
        f"`campus_registry.py` does not match the combined values yet.\n"
        f"  - get_registered_clubs() returned:  {clubs}\n"
        f"    expected:                         {expected_clubs}\n"
        f"  - get_lab_operating_hours() returned: {hours}\n"
        f"    expected:                           {expected_hours}",
    )


def main():
    parser = argparse.ArgumentParser(description="CI verification runner.")
    parser.add_argument("--user", default=None, help="GitHub username to verify assignment for")
    parser.add_argument("--base", default=None, help="Base git ref to check protected files against")
    parser.add_argument("--pr", action="store_true", help="Enforce strict Pull Request checks")
    parser.add_argument("--func", default=None, help="Verify a single function by name")
    args = parser.parse_args()

    modified = set(testing.detect_modified_functions())

    if args.func:
        if args.func not in testing.ORACLE:
            print(f"[ERROR] Function '{args.func}' not found.")
            sys.exit(1)
        if args.func not in modified:
            spec = testing.ORACLE[args.func]
            print(
                f"[UNCHANGED] {spec['module']}.{args.func}() has not been modified yet.\n"
                "  Read its docstring and Example carefully: if it contains a bug, edit it\n"
                "  first and re-run; if it already matches its docstring, leave it untouched."
            )
            sys.exit(0)
        try:
            testing.verify_function(args.func)
            print(f"[PASS] {args.func}() passed all test cases.")
            sys.exit(0)
        except AssertionError as exc:
            print(f"[FAIL] {exc}")
            sys.exit(1)

    if args.pr:
        base_ref = find_base_ref(args.base)
        for protected in ("testing.py", "ci_check.py", "my_task.py"):
            base_src = git_show_file(base_ref, protected)
            if base_src is not None:
                with open(os.path.join(REPO_DIR, protected), "r", encoding="utf-8") as f:
                    curr_src = f.read()
                if curr_src.strip() != base_src.strip():
                    print(f"[ERROR] `{protected}` was modified in this Pull Request.")
                    print("        Do not modify the test suite or task scripts.")
                    sys.exit(1)

    if args.user:
        username = args.user.strip().lstrip("@")
        assigned = testing.get_user_assignment(username)
        assigned_names = {item["function"] for item in assigned}
        print("=" * 72)
        print(f"PROGRESS CHECK FOR: @{username}")
        print("=" * 72)
        print("\nPart 1: Your 5 Assigned Scenario Functions")
        print("-" * 72)

        extra = modified - assigned_names
        if extra:
            print(f"[ERROR] You modified function(s) outside your assignment: {sorted(extra)}")
            print("        Please revert changes to functions not in your list.")
            sys.exit(1)

        passed_fixes = 0
        failed_items = []
        for item in assigned:
            fname = item["function"]
            mod_name = item["module"]
            if fname in modified:
                try:
                    testing.verify_function(fname)
                    print(f"  [PASS]      {mod_name}.py -> {fname}() (Fixed & Verified)")
                    passed_fixes += 1
                except Exception as exc:
                    print(f"  [FAIL]      {mod_name}.py -> {fname}()\n    {exc}")
                    failed_items.append(fname)
            else:
                print(f"  [UNCHANGED] {mod_name}.py -> {fname}()")

        if failed_items:
            print("\n  Part 1 Status: [NEEDS FIX] Check the failed function(s) above.")
            sys.exit(1)

        if passed_fixes < 3:
            print(
                "\n  Part 1 Status: [IN PROGRESS] You still have broken function(s) in your\n"
                "  list of 5 above. Compare each [UNCHANGED] function with its docstring\n"
                "  and Example to find the remaining bug(s)."
            )
            sys.exit(1)

        print("\n  Part 1 Status: [COMPLETE] All buggy functions in your assignment are fixed!")

        print("\nPart 2: Merge Conflict Exercise (campus_registry.py)")
        print("-" * 72)
        m_status, m_msg = check_merge_conflict_status()
        print(f"  [{m_status}] {m_msg}")
        if m_status != "PASS":
            sys.exit(1)

        print("\n" + "=" * 72)
        print(f"SUCCESS: All tasks for @{username} are complete and ready to commit/push!")
        print("=" * 72)
        sys.exit(0)

    if not modified:
        print("[INFO] No modified scenario functions detected.")
        sys.exit(0)

    failed = False
    for fname in sorted(modified):
        try:
            testing.verify_function(fname)
            print(f"  [PASS] {fname}()")
        except Exception as exc:
            print(f"  [FAIL] {fname}(): {exc}")
            failed = True
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
