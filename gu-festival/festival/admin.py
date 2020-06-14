from django.contrib import admin
from .models import *


@admin.register(Arena)
class ArenaAdmin(admin.ModelAdmin):
    pass

@admin.register(ArenaTimeSlot)
class ArenaTimeSlotAdmin(admin.ModelAdmin):
    pass

@admin.register(BandRequest)
class BandRequestAdmin(admin.ModelAdmin):
    pass

@admin.register(CensorVote)
class CensorVoteAdmin(admin.ModelAdmin):
    pass
