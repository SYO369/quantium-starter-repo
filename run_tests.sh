#!/bin/bash

# 1. Activate the project virtual environment
. ./venv/bin/activate

# 2. Execute the test suite.
python -m pytest test_pink_morsel_visualizer.py
PYTEST_EXIT_CODE=$?

# 3. Return exit code 0 if all tests passed, or 1 if something went wrong.
if [ $PYTEST_EXIT_CODE -eq 0 ]
then
  exit 0
else
  exit 1
fi