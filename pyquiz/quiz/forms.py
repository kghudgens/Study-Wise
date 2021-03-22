from django import forms
from .models import QuestionAnswer, Quiz, QuizQuestions


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ["title", "subject"]


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = QuizQuestions
        exclude = ["quiz"]
