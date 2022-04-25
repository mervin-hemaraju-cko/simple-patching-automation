import os, sys
import utils.constants as Consts

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from models.mail_content import MailContent


def create_mail(recipient, subject, content):

    return Mail(
        from_email= os.environ['MAIL_SCRIPT_SENDER'],
        to_emails=recipient,
        subject=subject,
        html_content=content)

def main():

    # Get the keyword
    keyword = os.environ["PATCHING_KEYWORD"]

    # Make sure this is the intended action:
    confirmation = input(Consts.MESSAGE_OPERATION_CONFIRMATION.format(keyword)) 

    # If not confirmed
    if(confirmation.lower() not in Consts.LIST_CONFIRMATION_EXECUTION):

        # Print message
        print(Consts.MESSAGE_OPERATION_CANCELLED)

        # Exit script
        sys.exit(0)

    # Create the mail content
    mail_content = MailContent(keyword)
    
    # Generate the mail
    mail = create_mail(mail_content.recipient, mail_content.subject, mail_content.content)

    try:
        sg = SendGridAPIClient(os.environ["API_KEY_SENDGRID"])
        response = sg.send(mail)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

if __name__ == "__main__":
    main()

