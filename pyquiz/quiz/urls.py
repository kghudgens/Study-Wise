from django.urls import path
from . import views

urlpatterns = [
    # Correct this to reflect the quiz app
    path("quiz/", views.quiz, name="quiz"),
]