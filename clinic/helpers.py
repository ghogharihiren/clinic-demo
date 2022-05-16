
from django.core.mail import send_mail
import uuid
from django.conf import settings

def send_forgot_password(email,token):
    subject='your forgot password link'
    message=f"hi your forgot passworld link http://127.0.0.1:8000/rest-password/{token}/"
    email_from=settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list )
    return True
    