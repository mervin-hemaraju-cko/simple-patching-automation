import os

###############################################################
############## All constants values resides here ##############
###############################################################

## Confirmation messages
LIST_CONFIRMATION_EXECUTION = ["yes", "sure", "yeah", "yup", "yep", "ofcourse", "of course"]

####################################
############# MESSAGES #############
####################################
MESSAGE_OPERATION_CONFIRMATION = "Are you sure you want to send mail for {}: "
MESSAGE_OPERATION_CANCELLED = "Operation has been cancelled."

#################################
############# PATHS #############
#################################
PATH_FILE_PATCHING_AUDBLUE = f"{os.environ['PROJECTS']}/CKO/patching-mail-automation/models/mail_contents/aud-blue.txt"
PATH_FILE_PATCHING_AUDGREEN = f"{os.environ['PROJECTS']}/CKO/patching-mail-automation/models/mail_contents/aud-green.txt"

#################################
############# VALUES ############
#################################

VALUE_MAIL_SUBJECT_AUDBLUE = "Patching of AUD-BLUE servers and HAPs"
VALUE_MAIL_SUBJECT_AUDGREEN = "Patching of AUD-GREEN servers and HAPs"

VALUE_PATCHING_TYPE_AUDBLUE = "AUD-BLUE"
VALUE_PATCHING_TYPE_AUDGREEN = "AUD-GREEN"
