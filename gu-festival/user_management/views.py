from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import FormView
from .forms import ProfileCreationForm
from django.http.response import HttpResponseRedirect
from allauth.socialaccount.models import SocialAccount
from django.urls import reverse_lazy



# Create the UserProfile instance for a new user, INCOMPLETE
class CreateUserProfile(FormView):

    form_class = ProfileCreationForm
    template_name = 'create-profile.html'
    success_url = reverse_lazy('user_management:home')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return HttpResponseRedirect(reverse_lazy('user_management:home'))
        return super(CreateUserProfile, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super(CreateUserProfile, self).form_valid(form)