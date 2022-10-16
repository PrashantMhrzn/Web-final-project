from cars.models import Car
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse


@login_required
def dashboard(request):
    cars = Car.objects.filter(seller_id=request.user.id)
    return render(request, "registration/dashboard.html", {"cars": cars})


def register_seller(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully")
            return redirect(reverse("login"))
        return render(request, "registration/register.html", {"form": form})

    return render(request, "registration/register.html", {"form": form})
