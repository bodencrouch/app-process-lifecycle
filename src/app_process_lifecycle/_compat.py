"""Standalone compat helpers."""
from __future__ import annotations
import sys

def is_frozen() -> bool:
    return bool(getattr(sys, "frozen", False) or getattr(sys, "_MEIPASS", False))

def assign_process_to_job_object(*args, **kwargs):
    return None

def close_handle(*args, **kwargs):
    return None

def create_job_object(*args, **kwargs):
    return None

def win_get_system32_dir():
    from pathlib import Path
    import os
    return Path(os.environ.get("SystemRoot", r"C:\Windows")) / "System32"

