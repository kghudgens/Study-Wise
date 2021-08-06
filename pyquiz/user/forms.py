from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "username": "Username",
            "email": "Email",
        }
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
        ]


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        labels = {
            "subjectOfInterest": "What subject interests you most?",
            "goal": "Whats the goal you want to achieve with Study Wise?",
            "age": "What is your age?",
        }
        fields = [
            "subjectOfInterest",
            "goal",
            "age",
        ]
