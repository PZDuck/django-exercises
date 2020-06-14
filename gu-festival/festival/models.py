from django.db import models
from user_management.models import UserProfile


# Arena Model, complete
class Arena(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    

# ArenaTimeSlot model, complete
class ArenaTimeSlot(models.Model):
    NOON = 1
    DUSK = 2
    EVENING = 3

    TIME_CHOICES = [
        (NOON, "День"),
        (DUSK, "Ранний вечер"),
        (EVENING, "Поздний вечер"),
    ]
    
    arena = models.ForeignKey(Arena, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.IntegerField(choices=TIME_CHOICES, default=None)
    capacity = models.SmallIntegerField(default=0)
    reserved = models.SmallIntegerField(default=0)

    def __str__(self):
        return f"{self.arena} - {self.get_time_display()} - {self.date}"
    

# Band request model, complete
class BandRequest(models.Model):
    PASSED = 1
    REJECTED = 2
    IN_PROGRESS = 3

    STATUS = [
        (PASSED, 'Passed'),
        (REJECTED, 'Rejected'),
        (IN_PROGRESS, 'In progress'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    band_name = models.CharField(max_length=255)
    request_text = models.TextField()
    timeslot = models.ForeignKey(ArenaTimeSlot, on_delete=models.CASCADE, blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=IN_PROGRESS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request by {self.band_name}"
    

# Censor vote model, complete
class CensorVote(models.Model):
    PASS = 1
    REJECT = 2

    VOTES = [
        (PASS, 'Pass'),
        (REJECT, 'Reject'),
        (None, 'None'),
    ]

    censor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    band_request = models.ForeignKey(BandRequest, on_delete=models.CASCADE)
    vote = models.IntegerField(choices=VOTES, default=None)

