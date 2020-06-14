from allauth.account.views import login, logout
from django.urls import path
from .views import CreateUserProfile


app_name = 'user_management'

urlpatterns = [
    path('profile/', CreateUserProfile.as_view(), name='profile'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
