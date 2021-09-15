from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView
from .models import StudyPost


def study(request):

    study_guides = StudyPost.objects.all()[:3]
    context = {"study_guides": study_guides}
    return render(request, "study/study.html", context)


class StudyPostCreateView(LoginRequiredMixin, CreateView):
    model = StudyPost
    fields = ["title", "subject", "photo", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class StudyPostDetailView(DetailView):
    model = StudyPost
    context_object_name = "sg"
    template_name = "study/studypost_detail.html"
