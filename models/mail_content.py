import os
import utils.constants as Consts

class MailContent:

    def __init__(self, keyword) -> None:

        # If the patching is for AUD BLUE
        if keyword == Consts.VALUE_PATCHING_TYPE_AUDBLUE:
            self.recipient = os.environ["MAIL_SCRIPT_RECIPIENT"]
            self.subject = Consts.VALUE_MAIL_SUBJECT_AUDBLUE

            # Get the file to read
            mail_content = Consts.PATH_FILE_PATCHING_AUDBLUE
        
        # If the patching is for AUD GREEN
        elif keyword == Consts.VALUE_PATCHING_TYPE_AUDGREEN:
            self.recipient = os.environ["MAIL_SCRIPT_RECIPIENT"]
            self.subject =  Consts.VALUE_MAIL_SUBJECT_AUDGREEN

            # Get the file to read
            mail_content = Consts.PATH_FILE_PATCHING_AUDGREEN

        # If the patching is for CP3 API BLUE
        elif keyword == Consts.VALUE_PATCHING_TYPE_CP3_API_BLUE:
            self.recipient = os.environ["MAIL_SCRIPT_RECIPIENT"]
            self.subject = Consts.VALUE_MAIL_SUBJECT_CP3_API_BLUE

            # Get the file to read
            mail_content = Consts.PATH_FILE_PATCHING_CP3_API_BLUE

        # If the patching is for CP3 API GREEN
        elif keyword == Consts.VALUE_PATCHING_TYPE_CP3_API_GREEN:
            self.recipient = os.environ["MAIL_SCRIPT_RECIPIENT"]
            self.subject = Consts.VALUE_MAIL_SUBJECT_CP3_API_GREEN

            # Get the file to read
            mail_content = Consts.PATH_FILE_PATCHING_CP3_API_GREEN

        
        # Read the mail content from file
        f = open(mail_content, "r")
        self.content = f.read()