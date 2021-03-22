from django.urls import path
from . import views

urlpatterns = [
    path("quiz/", views.QuizListView.as_view(), name="quiz-list"),
    path("create_new_quiz", views.createQuiz, name="create-quiz-form"),
]