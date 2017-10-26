# coding: utf-8

import random

from django.core.mail import send_mail

from test2.settings import EMAIL_FROM
from users.models import EmailVerifyRecord


def random_code():
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
    sa = []
    for i in range(8):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt


# 发送邮箱验证码

def send_register_email(email):
    email_record = EmailVerifyRecord()
    random_str = random_code()
    email_record.code = random_str
    email_record.email = "letuszou@126.com"
    email_record.save()

    email_title = "来自test2"
    email_body = "来自test2基于django发送邮箱"

    send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
    if send_status:
        pass
