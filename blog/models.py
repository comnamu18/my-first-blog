from django.db import models
from django.utils import timezone

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=10)
    emailAdr = models.CharField(max_length=200)
    phoneNum = models.CharField(max_length=13)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
