from django.urls import path
from . import views

urlpatterns = [
    path("study/", views.study, name="study"),
    path(
        "new_study_post/",
        views.StudyPostCreateView.as_view(template_name="study/studypost_form.html"),
        name="create-guide",
    ),
]
