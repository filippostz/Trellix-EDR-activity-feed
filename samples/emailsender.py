"""Example of subscription to all threats events and email sender
"""
import ssl
import smtplib
from email.mime.text import MIMEText
import logging
import json
from mvision_edr_activity_feed import subscribe
context = ssl.create_default_context()

smtp_server = '' #smtp server
smtp_username = '' #smtp username
smtp_password = '' #smtp password
smtp_port = 465

sender = '' #email sender
receivers = [''] #email receiver(s)

@subscribe(entity='threat')
def send_threat(event):
    event_complete = str(event['threat'])
    logging.info("EVENT: %s", event)
    threat_name = str(event['threat']['threatAttrs']['name'])
    severity = str(event['threat']['severity'])
    mailtext = MIMEText(event_complete)
    subject = "EDR Alert: [" + severity + "] " + threat_name
    mailtext['From'] = sender
    mailtext['Subject'] = subject

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as mail_service:
        mail_service.login(smtp_username, smtp_password)
        mail_service.sendmail(sender, receivers, mailtext.as_string())
        logging.info("EVENT: %s", "email sent!")
        
     
