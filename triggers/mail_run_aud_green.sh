#!/bin/bash

export PATCHING_KEYWORD="AUD-GREEN"

source $HOME/Projects/patching-mail-automation/secrets.env

python $HOME/Projects/patching-mail-automation/main_mail.py
