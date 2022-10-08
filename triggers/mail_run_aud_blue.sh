#!/bin/bash

# * Set patching keyword
export PATCHING_KEYWORD="AUD-BLUE"

# * Load virtual environment
source $PROJECTS/CKO/patching-mail-automation/.venv/bin/activate

# * Load secrets
source $PROJECTS/CKO/patching-mail-automation/secrets.env

# * Exceute script
python $PROJECTS/CKO/patching-mail-automation/main_mail.py

# * Deactivate the virtual environment
deactivate