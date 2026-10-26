"""
UVCE Campus Club & Lab Registry (Merge Conflict Exercise).

When you merge `upstream/merge-conflict-practice` (or `origin/merge-conflict-practice`)
into your branch, a Git merge conflict will occur in `get_registered_clubs()` and
`get_lab_operating_hours()`.

To resolve the conflict correctly:
1. `get_registered_clubs()` must return all 4 clubs in this exact order:
   ["MARVEL", "IEEE", "GDSC", "SAE"]
2. `get_lab_operating_hours()` must return a dictionary containing both keys:
   {"weekday": "09:00-20:00", "weekend": "10:00-17:00"}
3. Remove all Git conflict markers (<<<<<<<, =======, >>>>>>>).
"""


def get_registered_clubs() -> list:
    """Return the official list of registered technical clubs."""
    return ["MARVEL"]


def get_lab_operating_hours() -> dict:
    """Return the operating hours schedule for the makerspace."""
    return {}
