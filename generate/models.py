from django.db import models

from user.models import User

# Create your models here.


class Story(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='stories')
    content = models.TextField()
