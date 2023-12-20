from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField(max_length=200)
