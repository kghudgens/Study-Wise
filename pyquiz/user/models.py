from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjectOfInterest = models.CharField(max_length=100, default="Default String")
    age = models.IntegerField(default=18)
    goal = models.TextField(max_length=500, default="Default String")

    def __str__(self):
        return f"Username: {self.user}"
