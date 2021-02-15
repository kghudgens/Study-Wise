from django import forms
from .models import Post


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        labels = {"title": "Title", "content": "Content"}

        fields = ["title", "content"]
