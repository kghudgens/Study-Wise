from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Post


def index(request):
    return render(request, "blog/index.html")


def about(request):
    return render(request, "blog/about.html")


class BlogList(ListView):
    model = Post
    template_name = "blog/blog.html"


class CreateView(CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]
