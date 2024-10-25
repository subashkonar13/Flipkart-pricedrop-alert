import smtplib
from email.mime.text import MIMEText
import logging

class EmailNotifier:
    """
    A class to send email notifications when the product price drops.

    Attributes:
        sender_email (str): The email address of the sender.
        receiver_email (str): The email address of the receiver.
        email_password (str): The password of the sender's email.
        smtp_server (str): The SMTP server for sending the email.
        smtp_port (int): The port number for the SMTP server.
    """

    def __init__(self, sender_email: str, receiver_email: str, email_password: str, smtp_server: str, smtp_port: int):
        """
        Initializes the EmailNotifier with the given email credentials and SMTP server details.

        Args:
            sender_email (str): The sender's email address.
            receiver_email (str): The receiver's email address.
            email_password (str): The password of the sender's email.
            smtp_server (str): The SMTP server address.
            smtp_port (int): The port number of the SMTP server.
        """
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.email_password = email_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_price_alert(self, new_price: float, product_url: str) -> None:
        """
        Sends an email notification if the product price drops.

        Args:
            new_price (float): The new price of the product.
            product_url (str): The URL of the product page.
        """
        subject = f"Price Drop Alert! New Price: ${new_price}"
        body = f"The price has dropped to ${new_price}. Check the product here: {product_url}"
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.sender_email
        msg['To'] = self.receiver_email

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.email_password)
                server.sendmail(self.sender_email, self.receiver_email, msg.as_string())
            logging.info(f"Price drop email sent! New price: ${new_price}")
        except Exception as e:
            logging.error(f"Error sending email: {e}")
