from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Arena, ArenaTimeSlot
from django.views.generic import ListView, CreateView, DetailView, UpdateView, CreateView
from .forms import BandRequestForm, CensorVoteForm
from .models import BandRequest, CensorVote
from user_management.models import UserProfile
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from .mixins import GroupRequiredMixin
from django.views.generic import View
import datetime

# Homepage view, no functionality
def index(request):
    return render(request, 'festival/home.html')
    
# List all the Arenas and available ArenaTimeSlots
class ArenaList(ListView):
    context_object_name = 'arena_list'

    def get_queryset(self):
        return Arena.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ArenaList, self).get_context_data(**kwargs)
        context['arena_timeslot_first'] = ArenaTimeSlot.objects.filter(date=datetime.date(2020,1,30))
        context['arena_timeslot_second'] = ArenaTimeSlot.objects.filter(date=datetime.date(2020,1,31))
        context['bands'] = BandRequest.objects.filter(status=1)
        print(context['arena_timeslot_first'])
        print(context['arena_timeslot_second'])
        return context

# Handling the form for new band requests
class BandRequestPost(SuccessMessageMixin, GroupRequiredMixin, CreateView):

    group_required= ['admin', 'Censor', 'Musician']

    model = BandRequest
    form_class = BandRequestForm
    success_url = reverse_lazy('festival:home')
    template_name = 'festival/band_request.html'

    def form_valid(self, form):
        user = UserProfile.objects.get(user=self.request.user)
        form.instance.user = user
        return super(BandRequestPost, self).form_valid(form)

# Showing the status of the particular BandRequest (for Musicians)
class BandRequestStatus(GroupRequiredMixin, ListView):

    group_required = ['admin', 'Censor', 'Musician']

    model = BandRequest
    template_name = 'festival/user_request.html'
    context_object_name = 'bandrequest'
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            profile = UserProfile.objects.get(user=self.request.user)
            return BandRequest.objects.filter(user=profile)
        else:
            return BandRequest.objects.none()

# Listing of all pending, approved and rejected BandRequests (for Censors)
class BandRequestList(GroupRequiredMixin, ListView):

    group_required = ['admin', 'Censor']

    model = BandRequest
    context_object_name = 'bandrequests'
    template_name = 'festival/requests.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BandRequestList, self).get_context_data(*args, **kwargs)

        band_votes = {}

        # Very ugly method for getting the dictionary of BandRequest objects and calculated value of censor votes
        # NEEDS REVIEWING
        for i in BandRequest.objects.all():
            votes = 0
            for j in CensorVote.objects.all():
                if j.band_request == i:
                    if j.vote == 1:
                        votes += 1
                    elif j.vote == 2:
                        votes -= 2
            band_votes[i] = votes

        context['votes'] = band_votes
        print(context['votes'])
        return context
 
# Giving a censor an opportunity to accept or reject the pending request
class CensorVoteCreate(GroupRequiredMixin, CreateView):

    group_required = ['admin', 'Censor']

    model = CensorVote
    template_name = 'festival/vote.html'
    form_class = CensorVoteForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect('festival:home')
    
    def get_initial(self, *args, **kwargs):
        print(self.request.GET)
        return {'band_request': self.kwargs['pk'], 'censor': self.request.user.profile}
    
    def get_context_data(self, **kwargs):
        context = super(CensorVoteCreate, self).get_context_data(**kwargs)
        context['voted'] = CensorVote.objects.filter(censor=self.request.user.profile, band_request=self.kwargs['pk'])
        context['current_request'] = BandRequest.objects.get(pk=self.kwargs['pk'])
        return context

# The final voting system for censors
class BandRequestUpdate(GroupRequiredMixin, UpdateView):

    group_required = ['admin', 'Censor']

    model = BandRequest
    template_name = 'festival/verdict.html'
    fields = ['status', 'timeslot']
    success_url = reverse_lazy('festival:home')

    def get_initial(self, *args, **kwargs):
        return {'status': self.kwargs['decision'],}

    def form_valid(self, form):
        if form.cleaned_data['status'] == 1:
            reserved_slot = ArenaTimeSlot.objects.filter(id=form.cleaned_data['timeslot'].id)[0]
            if reserved_slot.reserved < reserved_slot.capacity:
                reserved_slot.reserved += 1
                reserved_slot.save()
            else:
                messages.add_message(self.request, messages.ERROR, 'The Arena\'s timeslots are full. Select a new timeslot or reject')
                return HttpResponseRedirect(reverse_lazy('festival:decision', kwargs={'pk':self.kwargs['pk'], 'decision': self.kwargs['decision']}))
            
        return super(BandRequestUpdate, self).form_valid(form)





