from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from user import views as user_views


urlpatterns = [
    path("admin/", admin.site.urls),
    # Added the blog path to the projects urls to look for
    path("", include("blog.urls")),
    path("register/", user_views.register, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path(
        "accounts/login",
        auth_views.LoginView.as_view(template_name="login.html "),
        name="login",
    ),
    path(
        "accounts/logout",
        auth_views.LogoutView.as_view(template_name="logout.html"),
        name="logout",
    ),
]
