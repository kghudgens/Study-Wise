from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import StudyPost


def study(request):
    study_guides = StudyPost.objects.all()[:3]
    context = {"study_guides": study_guides}
    return render(request, "study/study.html", context)


class StudyPostCreateView(LoginRequiredMixin, CreateView):
    model = StudyPost
    fields = ["title", "subject", "photo", "content"]
