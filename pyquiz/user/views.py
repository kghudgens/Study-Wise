from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UpdateUserForm, UpdateProfileForm
from .models import Profile


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
    form_class = UpdateUserForm
    p_form_class = UpdateProfileForm
    if request.method == "POST":
        p_form = p_form_class(request.POST, instance=request.user)
        user_form = form_class(request.POST, instance=request.user)
        if user_form.is_valid() and p_form.is_valid():
            user_form.save()
            p_form.save()
            messages.success(request, "Your profile has been updated")
            return redirect("profile")
    else:
        user_form = UpdateUserForm()
        p_form = UpdateProfileForm()

    profile_data = Profile.objects.all().filter(user=request.user)
    return render(
        request,
        "user/profile.html",
        {"user_form": user_form, "p_form": p_form, "profile_data": profile_data},
    )
