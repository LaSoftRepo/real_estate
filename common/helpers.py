# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.core.mail import send_mail
from django.contrib.contenttypes.models import ContentType
from django.template.loader import render_to_string

from admin2.models import EmailForward, ActiveFranchise, EmailSettings
from django.conf import settings

from django.core.mail import send_mail as core_send_mail
from django.core.mail import EmailMultiAlternatives
import threading


class EmailThread(threading.Thread):
    def __init__(self, subject, body, from_email, recipient_list,
                 fail_silently, html):
        self.subject = subject
        self.body = body
        self.recipient_list = recipient_list
        self.from_email = from_email
        self.fail_silently = fail_silently
        self.html = html
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMultiAlternatives(self.subject, self.body, self.from_email,
                                     self.recipient_list)
        if self.html:
            msg.attach_alternative(self.body, "text/html")
        msg.send(self.fail_silently)


def send_mail(subject, message, from_email, recipient_list,
              fail_silently=False, html=None, *args, **kwargs):
    EmailThread(subject, message, from_email, recipient_list, fail_silently,
                html).start()


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def sending_email(obj):
    emails_to = EmailForward.objects.all().values_list('email', flat=True)
    try:
        service = ContentType.objects.get_for_id(
            obj.content_type.id).model_class().objects.get(id=obj.object_id)
        partners_emails = service.partners.all().values_list('email',
                                                             flat=True)
    except AttributeError:
        partners_emails = None
    from_email = get_from_email()
    subject = 'Новая Заявка'
    context = {
        'created': obj.created,
        'source': obj.source,
        'name': obj.name or '--',
        'phone': obj.phone or '--',
        'email': obj.email or '--',
        'address': obj.address or '--',
        'price': obj.price or '--',
        'text': obj.text or '--'
    }
    message = render_to_string('common/email/notification.html',
                               context=context)
    if ActiveFranchise.get_solo().is_active:
        send_mail(subject=subject, message=message, from_email=from_email,
                  recipient_list=emails_to,
                  fail_silently=False, html=True)
        if partners_emails:
            send_mail(subject=subject, message=message, from_email=from_email,
                      recipient_list=partners_emails,
                      fail_silently=False, html=True)
    else:
        message = 'Источник: {source}'.format(source=obj.source)
        send_mail(subject=subject, message=message, from_email=from_email,
                  recipient_list=emails_to,
                  fail_silently=False, )


def get_from_email():
    email = EmailSettings.get_solo()
    if not email.domen:
        email = settings.DEFAULT_FROM_EMAIL
    return email
