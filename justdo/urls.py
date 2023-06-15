"""
URL configuration for justdo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from tasks import views as task_views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (PasswordResetView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", user_views.index, name="home_page"),
    path("login/", auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),  # noqa
    path("logout/", auth_views.LogoutView.as_view(next_page='home_page'), name="logout"),  # noqa
    path("register/", user_views.register, name="register"),
    path("password-reset/", PasswordResetView.as_view(
        template_name="users/password-reset.html", html_email_template_name='users/password_reset_email.html'), name="password-reset"),  # noqa

    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'),
         name='password_reset_done'),  # noqa

    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html')),  # noqa
      path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),  # noqa
    path("terms/", user_views.terms, name="terms"),
    path("features/", user_views.features, name="features"),
    path("", include("users.urls")),
    path("tasks/", include("tasks.urls"), name="tasks"),
]
