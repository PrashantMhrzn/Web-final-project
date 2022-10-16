from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import CarForm
from .models import Car


def home(request):
    return render(request, "homepage.html")


def about(request):
    return render(request, "about.html")


def get_cars(request):
    cars = Car.objects.all()
    query = request.GET.get("query", None)
    if query:
        cars = cars.filter(Q(model_name__iexact=query) | Q(location__iexact=query))

    return render(request, "get_cars.html", {"cars": cars})


@login_required
def delete_car(request, car_id):
    car = Car.objects.filter(id=car_id).first()

    if car:
        messages.success(
            request,
            f"{car.model_name}has been successfully removed from your listings.",
        )
        car.delete()
        return redirect("dashboard")


@login_required
def add_car(request):
    form = CarForm()
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            n_form = form.save(commit=False)
            n_form.seller_id = request.user
            n_form.save()
            return redirect(reverse("get_cars"))
    return render(request, "add_car.html", {"form": form})
