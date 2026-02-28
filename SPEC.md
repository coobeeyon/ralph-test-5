# Project Specification

## Overview

A simple "Hello World" CLI program that prints a greeting message. This is a minimal test project to verify the ralph harness end-to-end workflow.

## Requirements

- Create a Python script `hello.py` that prints "Hello, World!" to stdout
- The script should accept an optional `--name` argument: `hello.py --name Alice` prints "Hello, Alice!"
- If no name is given, default to "World"
- Include a test file `test_hello.py` that verifies both cases
- Tests should be runnable with `python -m pytest test_hello.py`

## Architecture

Single-file CLI script using only the Python standard library (`argparse`). Tests use `pytest`.

## Constraints

- Python 3.x only, no external dependencies beyond pytest for testing
- Must exit with code 0 on success
