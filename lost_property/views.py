from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'lost.html')

def new(request):
    return render(request, 'lost_new.html')

def detail(request):
    return render(request, 'lost_detail.html')