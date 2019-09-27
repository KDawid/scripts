from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

import base64
import pickle


class EmailSender:
    def __init__(self, config):
        self.config = config

        self.SCOPES = ['https://mail.google.com/']

    def get_credentials(self):
        creds = None
        try:
            with open(self.config.get_pickle_file(), 'rb') as token:
                creds = pickle.load(token)
        except FileNotFoundError:
            print("token.pickle not found")
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.config.get_credentials_file(), self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(self.config.get_pickle_file(), 'wb') as token:
                pickle.dump(creds, token)
        return creds

    def create_message(self, sender, to, subject, message_text):
        message = MIMEText(message_text % (subject, self.config.get_imax_url()), 'html')
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

    def send_message(self, service, user_id, message):
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print('Message Id: %s' % message['id'])
        return message

    def notify(self):
        creds = self.get_credentials()

        service = build('gmail', 'v1', credentials=creds)

        user_id = self.config.get_user_id
        sender = self.config.get_user_email()
        recipients = ','.join(self.config.get_recipients())
        subject = self.config.get_subject() % self.config.get_movie_title().upper()
        body = self.config.get_html_body()

        self.send_message(service, user_id, self.create_message(sender, recipients, subject, body))
