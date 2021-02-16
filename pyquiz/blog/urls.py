from django.urls import path
from . import views
from user import views as user_views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("blog/", views.BlogList.as_view(), name="blog-list"),
]
