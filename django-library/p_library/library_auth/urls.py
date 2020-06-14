from library_auth.views import index
from django.urls import path, reverse_lazy, include
from allauth.account.views import login, logout
  
app_name = 'library_auth'  
urlpatterns = [  
    path('', include('library.urls', namespace='library')),  
	path('login/', login, name='login'),  
	path('logout/', logout, name='logout'),
]