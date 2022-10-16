from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_cars, name="get_cars"),
    path("add/", views.add_car, name="add_car"),
    path("delete/<int:car_id>/", views.delete_car, name="delete_car"),
]
