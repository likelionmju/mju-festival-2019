from django.shortcuts import render
from .models import Lost

# Create your views here.
def home(request):
    stuffs = Lost.objects.all()
    return render(request, 'lost.html', {'stuffs' : stuffs})

def new(request):
    return render(request, 'lost_new.html')

def detail(request):
    return render(request, 'lost_detail.html')