import subprocess
import sys


def test_default_greeting():
    result = subprocess.run(
        [sys.executable, "hello.py"], capture_output=True, text=True
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "Hello, World!"


def test_custom_name():
    result = subprocess.run(
        [sys.executable, "hello.py", "--name", "Alice"], capture_output=True, text=True
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "Hello, Alice!"
