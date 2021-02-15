from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


def index(request):
    return render(request, "blog/index.html")


def about(request):
    return render(request, "blog/about.html")


class BlogList(ListView):
    model = Post
    template_name = "blog/blog.html"
