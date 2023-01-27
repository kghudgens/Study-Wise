from django import forms
from .models import Post, Comment, PostImage


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        labels = {"title": "Title", "content": "Content"}

        fields = ["title", "content"]


class BlogPostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        labels = {"post_img": "Upload your photo"}

        fields = ["post_img"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        labels = {"content": "Join the discussion and leave a comment!"}

        fields = ["content"]
