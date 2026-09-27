"""Seeded security fault: subprocess call with shell=True (expected code S602)."""

import subprocess


def run(command: str) -> int:
    """Run a command line."""
    return subprocess.call(command, shell=True)
