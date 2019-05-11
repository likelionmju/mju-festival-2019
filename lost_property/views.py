from django.shortcuts import render, redirect, get_object_or_404
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
    lost_detail = get_object_or_404(Lost, pk=lost_id)
    return render(request, 'lost_detail.html', {'lost_detail': lost_detail})