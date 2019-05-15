from django.urls import path
from . import views

urlpatterns = [
    path('', views.mjworld, name="mjworld"),
]
