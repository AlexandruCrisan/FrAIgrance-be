from django.db import models

from user.models import User

# Create your models here.


class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories')
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
