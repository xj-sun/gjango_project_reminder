from __future__ import unicode_literals
from django.contrib.auth.models import  User
from datetime import datetime
from django.db import models
class Reminder(models.Model):
    ALWAYS = 0
    RAIN = 1
    SNOW = 2
    TEMPDROP3F = 3
    TEMPRISE3F = 4
    MAX_CHOICES = 5
    MAX = [0,1,2,3,4]
    WARNING_TEXT = [
        'Always',
        'Raining tomorrow',
        'Snowing tomorrow',
        'Temperature dropping by 3 F ',
        'Temperature rising by 3 F',
    ]
    #WARNING_CHOICE = [(i,  WARNING_TEXT[i]) for i in range(MAX_CHOICES)]
    WARNING_CHOICE = list(zip(MAX, WARNING_TEXT))
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    zipcode = models.CharField(max_length=30)
    #warning_event = models.ImageField(default=0, choices=WARNING_CHOICE)
    warning_event = models.IntegerField(default=0)
    reminder_sent = models.DateField(default=datetime.min, blank=True)

    def __str__(self):
        return self.user.get_username() + '_' + self.zipcode
# Create your models here.
