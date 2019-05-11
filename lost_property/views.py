from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Lost
from .forms import LostForm

# Create your views here.
def home(request):
    stuffs = Lost.objects.all()
    return render(request, 'lost.html', {'stuffs' : stuffs})

def new(request):
    if request.method == 'POST':
        form = LostForm(request.POST)
        if form.is_valid():
            lost = form.save(commit=False)
            lost.pub_date = timezone.now()
            lost.save()
        return redirect('lost_home')
    else:
        form = LostForm()
        return render(request, 'lost_new.html', {'form':form})

def detail(request):
    return render(request, 'lost_detail.html')