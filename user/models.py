from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    uid = models.CharField(max_length=255)
    displayName = models.CharField(max_length=255)
