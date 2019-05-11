from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def booth(request):
    return render(request, "booth.html")

def foodtruck(request):
    return render(request, "foodtruck.html")

def lineup(request):
    return render(request, "lineup.html")

def bus(request):
    return render(request, "bus.html")