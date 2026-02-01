import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class MailClient:

    def __init__(self, login, password, smtp_address, imap_address):
        """
        Initialize a mail client with authentication credentials and mail server addresses.

        :param login: Email address used for authentication.
        :param password: Password or application-specific password for the email account.
        :param smtp_address: SMTP server address for sending emails.
        :param imap_address: IMAP server address for receiving emails.
        """
        self.login = login
        self.password = password
        self.smtp_address = smtp_address
        self.imap_address = imap_address
        

    def send_message(self, subject, recipients, message):
        """
        Send an email message using the configured SMTP server.

        :param subject: Subject of the email.
        :param recipients: List of recipient email addresses.
        :param message: Text content of the email message.
        :return: None
        """
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        # start SMTP_server connection
        smtp_server = smtplib.SMTP(self.smtp_address, 587)
        # identify ourselves to smtp gmail client
        smtp_server.ehlo()
        # secure our email with tls encryption
        smtp_server.starttls()
        # re-identify ourselves as an encrypted connection
        smtp_server.ehlo()

        smtp_server.login(self.login, self.password)
        smtp_server.sendmail(self.login, recipients, msg.as_string())
        smtp_server.quit()


    def receive_message(self, header):
        """
        Receive the most recent email matching the given subject header.

        :param header: Subject header to filter emails. If None, retrieves the latest email.
        :return: Parsed email message object.
        :raises AssertionError: If no emails matching the criteria are found.
        """
        mail = imaplib.IMAP4_SSL(self.imap_address)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        mail.logout()
        return email_message


USER_ADDRESS_MAIL_SMTP = "smtp.gmail.com"
USER_ADDRESS_MAIL_IMAP = "imap.gmail.com"

user_login = 'login@gmail.com'
user_password = 'qwerty'
user_subject = 'Subject'
user_recipients = ['vasya@email.com', 'petya@email.com']
user_message = 'Message'
user_header = None


if __name__ == '__main__':
    user_1 = MailClient(user_login, user_password, USER_ADDRESS_MAIL_SMTP, USER_ADDRESS_MAIL_IMAP)
    user_1.send_message(user_subject, user_recipients, user_message)
    message = user_1.receive_message(user_header)