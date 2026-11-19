"""
UVCE Campus Club & Lab Registry (Merge Conflict Exercise).

Combined club registrations and lab operating hours
from both branches.
"""


def get_registered_clubs() -> list:
    """Return the official list of registered technical clubs."""
    return ["MARVEL", "IEEE", "GDSC", "SAE"]


def get_lab_operating_hours() -> dict:
    """Return the operating hours schedule for the makerspace."""
    return {
        "weekday": "09:00-20:00",
        "weekend": "10:00-17:00"
    }
