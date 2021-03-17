from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Quiz


class QuizListView(ListView):
    model = Quiz
    template_name = "quiz/quiz.html"