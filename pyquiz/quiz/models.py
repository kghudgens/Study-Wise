from django.db import models
from django.conf import settings

# Create your models here.
class Quiz(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class QuizQuestions(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class QuestionAnswer(models.Model):
    quiz_questions = models.ForeignKey(QuizQuestions, on_delete=models.CASCADE)
    user_answer = models.TextField()
    correct = models.CharField(max_length=100)
