from django.urls import path
from .views import *

app_name = 'festival'
urlpatterns = [
    path('', index, name='home'),
    path('schedule/', ArenaList.as_view(), name='schedule'),
    path('request/', BandRequestPost.as_view(), name='band-request'),
    path('request/status/', BandRequestStatus.as_view(), name='request-status'),
    path('requests', BandRequestList.as_view(), name='requests'),
    # path('vote/', band_request_update, name='vote'),
    # path('requests/<int:pk>', BandRequestDetail.as_view(), name='request-detail'),
    path('requests/<int:pk>', CensorVoteCreate.as_view(), name='vote'),
    path('request/<int:pk>/<int:decision>', BandRequestUpdate.as_view(), name='decision'),
]
