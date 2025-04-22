from django.db import models
from django.contrib.auth.models import AbstractUser


class customerAcc(AbstractUser):
    #Storing points that might accumulate for some rewards?
    points = models.IntegerField(default=0)
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField (max_length=14, blank = True)

# Create your models here.


