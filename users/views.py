from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import RegistrationForm


def index(request):
    return render(request, "index_carousel.html")


def register(request):
    if request.method == "GET":
        form = RegistrationForm()
        context = {"form": form}
        return render(request, "users/register.html", context)

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, f"{user} account created successfully")
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
