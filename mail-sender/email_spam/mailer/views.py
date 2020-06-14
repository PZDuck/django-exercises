from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.conf import settings
from .models import EmailMsg
from .forms import EmailMsgForm
from django.db.models import Q

import threading
import random, time


class EmailSender(threading.Thread):

    def __init__(self, new_mail, mail_subject, mail_body, mail_to):
        threading.Thread.__init__(self)
        self.mail_id = new_mail.id
        self.mail_to = mail_to
        self.mail_subject = mail_subject
        self.mail_body = mail_body
        self.mail_sender = settings.EMAIL_HOST_USER
        self.start()

    def run(self):
        current_message = EmailMsg.objects.get(id=self.mail_id)
        time.sleep(random.randint(1,60))
        send_mail(self.mail_subject, self.mail_body, self.mail_sender, self.mail_to)
        current_message.mail_status = True
        current_message.save()



def index(request):
    mailbox = EmailMsg.objects.all()
    return render(request, "home.html", {'mailbox': mailbox})


def construct_mail(request):
    if request.method == 'POST':
        form = EmailMsgForm(request.POST)
        if form.is_valid():
            mail_subject = form.cleaned_data['mail_subject']
            mail_body = form.cleaned_data['mail_body']
            mail_to = [form.cleaned_data['mail_to']]
            new_mail = form.save()

            EmailSender(new_mail, mail_subject, mail_body, mail_to)

            return HttpResponseRedirect(reverse_lazy('mailer:home'))
    else:
        form = EmailMsgForm()
    
    return render(request, 'compose.html', {'form': form})
        




