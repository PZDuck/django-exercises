from django.db import models


class EmailMsg(models.Model):
    mail_to = models.CharField(max_length=255)
    mail_subject = models.CharField(max_length=255)
    mail_body = models.TextField()
    mail_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Sent: {self.mail_status} || Recipient: {self.mail_to} || Subject: {self.mail_subject} || Message: {self.mail_body}"

