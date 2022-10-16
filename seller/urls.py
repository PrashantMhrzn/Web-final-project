from django.urls import path

from .views import dashboard, register_seller

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("register/", register_seller),
]
