from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("blog/", views.BlogList.as_view(), name="blog-list"),
    path("create_post/", views.CreateView.as_view(), name="create"),
]
