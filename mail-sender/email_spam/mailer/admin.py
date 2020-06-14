from django.contrib import admin
from .models import EmailMsg


@admin.register(EmailMsg)
class EmailMsgAdmin(admin.ModelAdmin):
    pass
