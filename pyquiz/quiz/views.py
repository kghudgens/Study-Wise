from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from .models import Quiz, QuizQuestions, QuestionAnswer
from .forms import QuizForm, ChoiceForm


class QuizListView(ListView):
    model = Quiz
    template_name = "quiz/quiz.html"


def createQuiz(request):
    if request.method == "POST":
        # Create instance of the quiz form
        qform = QuizForm(request.POST, instance=Quiz())
        # Create instance of the choice form
        cform = [
            ChoiceForm(request.POST, prefix=str(x), instance=QuizQuestions())
            for x in range(0, 5)
        ]
        if qform.is_valid() and all([cf.is_valid() for cf in cform]):
            new_quiz = qform.save()
            for cf in cform:
                new_choice = cf.save(commit=False)
                new_choice.quiz = new_quiz
                new_choice.save()
            return HttpResponseRedirect("/quiz-list/")
    else:
        qform = QuizForm(instance=Quiz())
        cform = [
            ChoiceForm(prefix=str(x), instance=QuizQuestions()) for x in range(0, 5)
        ]
    return render(
        request,
        "quiz/create_quiz_form.html",
        {"quiz_form": qform, "choice_forms": cform},
    )
