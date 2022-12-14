import smtplib
import ssl
from email.message import EmailMessage


def send_email(

        smtp_email_login,
        smtp_pass,
        smtp_email_recipient,
        smtp_subject,
        smtp_send_msg,
        smtp_server,
        smtp_port

        ):
    """
    Function responsible for sending emails.
    """

    smtp_msg = EmailMessage()

    smtp_msg.set_content(

        f"***   ATTENTION!   ***\n\n"
        f"{'-' * 55}\n"
        f"{smtp_send_msg}\n"
        f"{'-' * 55}\n\n"

    )

    smtp_msg["Subject"] = smtp_subject

    smtp_msg["From"] = smtp_email_login

    smtp_msg["To"] = smtp_email_recipient

    context = ssl.create_default_context()

    with smtplib.SMTP(smtp_server, port=smtp_port) as smtp:

        smtp.starttls(context=context)

        smtp.login(smtp_msg["From"], smtp_pass)

        smtp.send_message(smtp_msg)
