from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Post


def index(request):
    return render(request, "blog/index.html")


def about(request):
    return render(request, "blog/about.html")


class BlogList(ListView):
    model = Post
    template_name = "blog/blog.html"


class CreateView(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog-list")


class DetailPostView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class PostUpdate(SuccessMessageMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name_suffix = "_update_form"

    success_message = "You have successfully updated your post."

    def get_success_url(self):
        return reverse("blog-list")