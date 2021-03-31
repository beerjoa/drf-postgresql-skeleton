from django.urls import path, include
from .views import Calculations



urlpatterns = [
    path("", Calculations.as_view())
]