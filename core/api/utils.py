from django.conf import settings
# send_mail is a built-in function in django
from django.core.mail import send_mail
from django.template.loader import render_to_string

def send_email(subject, message, recipient_list):
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, recipient_list)
