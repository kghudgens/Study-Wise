from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import StudyPost


def study(request):
    return render(request, "study/study.html")


class StudyPostCreateView(LoginRequiredMixin, CreateView):
    model = StudyPost
    fields = ["title", "subject", "photo", "content"]
