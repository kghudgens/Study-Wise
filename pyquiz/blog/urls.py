from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="index"),
    path("blog/", views.BlogList.as_view(), name="blog-list"),
]
