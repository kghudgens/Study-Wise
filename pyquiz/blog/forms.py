from django import forms
from .models import Post, Comment


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        labels = {"title": "Title", "content": "Content"}

        fields = ["title", "content"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        labels = {"author": "Author", "title": "Title", "content": "Comment"}

        fields = ["post", "author", "title", "content"]
