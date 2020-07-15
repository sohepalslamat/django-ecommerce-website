# هذا لملف من أجل الاضافات
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

from .token import confirm_mail_token_generator


def send_confirmation_email(request, user):
    # http://132.168.0.0/uid/token

    uid = user.id
    token = confirm_mail_token_generator.make_token(user)
    domain = get_current_site(request)

    subject = 'Activate Your Account'
    message = render_to_string('registration/account-activation-email.html',
                               {
                                   'user': user,
                                   'domain': domain,
                                   'token': token,
                                   'uid': uid
                               })

    user.email_user(subject, message)
