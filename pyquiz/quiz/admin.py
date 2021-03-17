from django.contrib import admin
from .models import QuestionAnswer, Quiz, QuizQuestions

# Register your models here.
admin.site.register(QuestionAnswer)
admin.site.register(Quiz)
admin.site.register(QuizQuestions)