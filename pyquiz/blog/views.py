from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.apps import apps
from .models import Post, Comment
from .forms import CommentForm
from study.models import StudyPost
from contact.forms import ContactForm


def index(request):
    # Query the entries in the db for data to display
    posts = Post.objects.all()[:3]
    guides = StudyPost.objects.all()[:3]
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/success.html')
    form = ContactForm()
    context = {"posts": posts, "guides": guides, "form": form}
    return render(request, "blog/index.html", context)


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


class DetailPostView(FormMixin, DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "posts"
    form_class = CommentForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.object = self.get_object()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse("post-detail", kwargs={"pk": self.object.pk})


class PostUpdate(
    UserPassesTestMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView
):
    model = Post
    fields = ["title", "content"]
    template_name_suffix = "_update_form"
    login_url = "/login/"
    success_message = "You have successfully updated your post."

    def get_success_url(self):
        return reverse("post-detail", kwargs={"pk": self.object.pk})

    def test_func(self):
        self.object = self.get_object()
        return self.request.user == self.object.author


class DeletePostView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("blog-list")

    def test_func(self):
        self.object = self.get_object()
        return self.request.user == self.object.author
