from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import StudyPost


def study(request):
    return render(request, "study/study.html")


class StudyPostCreateView(CreateView):
    model = StudyPost
    fields = ["title", "subject", "photo", "content"]
