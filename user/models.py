from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    auth0_id = models.CharField(max_length=255, unique=True)
    credits = models.IntegerField(default=5)

    def __str__(self):
        return self.username
