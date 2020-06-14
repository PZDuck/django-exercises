from django import forms
from .models import EmailMsg


class EmailMsgForm(forms.ModelForm):
    class Meta:
        model = EmailMsg
        exclude = ('mail_status',)