"""Smoke test: the Project 1 demonstration (main.py) still runs."""
import subprocess
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent


def test_main_demo_runs_to_completion():
    result = subprocess.run([sys.executable, 'main.py'], cwd=PROJECT_DIR,
                            capture_output=True, text=True, timeout=30)
    assert result.returncode == 0
    assert 'Final balance: $' in result.stdout
    assert 'Traceback' not in result.stderr


def test_demo_shows_each_failure_and_carries_on():
    result = subprocess.run([sys.executable, 'main.py'], cwd=PROJECT_DIR,
                            capture_output=True, text=True, timeout=30)
    for expected in ('exceeds the maximum', 'balance is only',
                     'below the minimum balance', 'not a valid deposit',
                     'has no account numbered 99', 'Retry status: Processed'):
        assert expected in result.stdout
    assert 'Traceback' not in result.stderr
