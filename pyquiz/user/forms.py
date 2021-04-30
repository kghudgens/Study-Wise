from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
        ]


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "subjectOfInterest",
            "goal",
            "age",
        ]
