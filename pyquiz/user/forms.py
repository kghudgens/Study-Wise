from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PyQuizUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")

    def save(self, commit=True):
        user = super(PyQuizUserForm, self).save(commit=False)
        user.first_name = first_name
        user.last_name = last_name
        if commit:
            user.save()
        return User