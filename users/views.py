from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import RegistrationForm
from .models import UserProfile


def index(request):
    xp = request.user.userprofile.xp
    context = {"xp": xp}
    return render(request, "index_carousel.html", context)


def register(request):
    if request.method == "GET":
        form = RegistrationForm()
        context = {"form": form}
        return render(request, "users/register.html", context)

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            messages.success(request, f"{user.username} account created successfully")  # noqa
            return redirect("home_page")
    else:
        context = {"form": form}
        messages.error(request, "Error processing your request")
        return render(request, "users/register.html", context)

    return render(request, "users/register.html", {})


def terms(request):
    return render(request, "terms_and_conditions.html")


def features(request):
    return render(request, "features.html")
