from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UpdateUserForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created.")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "user/register.html", {"form": form})


def profile(request):
    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated")
            return redirect("profile")
    else:
        form = UpdateUserForm()
    return render(request, "user/profile.html", {"form": form})
