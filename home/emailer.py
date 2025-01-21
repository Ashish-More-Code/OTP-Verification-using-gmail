from django.core.mail import send_mail
from django.conf import settings
def send_otp_on_email(email,subject,message):
    send_mail(subject,message,settings.EMAIL_HOST_USER,[email])