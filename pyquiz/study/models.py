from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image

# The choices for the subject field in the Study Post model
subject_choices = (
    ("Information Technology", "Information Technology"),
    ("Math", "Math"),
    ("Science", "Science"),
    ("History", "History"),
    ("Literature", "Literature"),
    ("Foreign Language", "Foreign Language"),
    ("Geography", "Geography"),
)


class StudyPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(
        max_length=30, choices=subject_choices, default="Information Technology"
    )
    content = models.TextField()
    photo = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("studypost_detail", kwargs={"pk": self.pk})
