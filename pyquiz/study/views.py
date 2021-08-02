from django.shortcuts import render


def study(request):
    return render(request, "study/study.html")
