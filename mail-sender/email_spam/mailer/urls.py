from django.urls import path
from .views import index, construct_mail


app_name = 'mailer'
urlpatterns = [
    path('', index, name='home'),
    path('compose/', construct_mail, name='compose'),   
]