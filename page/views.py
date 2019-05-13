from django.shortcuts import render
from .models import Food, Individual, Organization

# Create your views here.
def home(request):
    return render(request, "home.html")

def booth(request):
    return render(request, "booth.html")

def foodtruck(request):
    foods = Food.objects.all()
    return render(request, "foodtruck.html", {'foods':foods})

def lineup(request):
    return render(request, "lineup.html")

def bus(request):
    return render(request, "bus.html")

def individual(request):
    booths = Individual.objects.all()
    return render(request, "individual.html", {'booths':booths})

def organization(request):
    booths = Organization.objects.all()
    return render(request, "organization.html", {'booths':booths})