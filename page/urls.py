from django.urls import path
from . import views

urlpatterns = [
    path('booth/', views.booth, name='booth'),
    path('foodtruck/', views.foodtruck, name='foodtruck'),
    path('lineup/', views.lineup, name='lineup'),
    path('bus/', views.bus, name='bus'),
    path('individual/', views.individual, name="individual"),
    path('organization/', views.organization, name="organization"),
]