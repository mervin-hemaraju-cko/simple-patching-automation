#!/bin/bash

# * Set patching keyword
export PATCHING_KEYWORD="AUD-BLUE"

# * Load virtual environment
source /Users/mervin.hemaraju/Projects/patching-mail-automation/.venv/bin/activate

# * Load secrets
source /Users/mervin.hemaraju/Projects/patching-mail-automation/secrets.env

# * Exceute script
python /Users/mervin.hemaraju/Projects/patching-mail-automation/main_mail.py

# * Deactivate the virtual environment
deactivate