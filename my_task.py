"""
Student Assignment CLI for UVCE Marvel Git-Task.

Usage:
    python my_task.py <your-github-username>
"""
import ast
import os
import sys
import testing


REPO_DIR = os.path.dirname(os.path.abspath(__file__))


def get_function_line(mod_name: str, func_name: str) -> int:
    """Return 1-based line number of func_name in mod_name.py."""
    path = os.path.join(REPO_DIR, f"{mod_name}.py")
    if not os.path.exists(path):
        return 1
    with open(path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == func_name:
            return node.lineno
    return 1


def main():
    if len(sys.argv) < 2 or not sys.argv[1].strip():
        print("Usage: python my_task.py <your-github-username>")
        sys.exit(1)

    username = sys.argv[1].strip().lstrip("@")
    assigned = testing.get_user_assignment(username)

    print("=" * 74)
    print(f"UVCE MARVEL GIT-TASK ASSIGNMENT FOR: @{username}")
    print("=" * 74)
    print("\nPart 1: Inspect Your 5 Assigned Scenario Functions")
    print("-" * 74)
    print(
        "Open each file below at the listed line number. Every function has a\n"
        "short description and an `Example:` in its docstring.\n\n"
        "How to spot a bug:\n"
        "  Trace the function's code using the `Example:` input. If the code\n"
        "  produces a different answer from the `Example:`, fix the bug!\n"
    )
    print(f"{'#':<4} {'File':<32} {'Line':<8} {'Function Name'}")
    print("-" * 74)
    for idx, item in enumerate(assigned, start=1):
        mod_file = f"{item['module']}.py"
        lineno = get_function_line(item["module"], item["function"])
        print(f"{idx:<4} {mod_file:<32} L{lineno:<7} {item['function']}()")

    print("\nPart 2: Resolve the Merge Conflict in campus_registry.py")
    print("-" * 74)
    print(
        "After fixing the bugs in Part 1, merge the practice conflict branch:\n"
        "    git fetch upstream\n"
        "    git merge upstream/merge-conflict-practice\n"
        "    (or `git merge origin/merge-conflict-practice` if working on your fork)\n\n"
        "Open `campus_registry.py`, combine both branches as described in its\n"
        "docstring, and check your overall progress anytime by running:\n"
        f"    python ci_check.py --user {username}\n\n"
        "Note: Some of your 5 assigned functions may already work correctly --\n"
        "only edit a function if its code does not match its docstring/Example."
    )
    print("=" * 74)


if __name__ == "__main__":
    main()
