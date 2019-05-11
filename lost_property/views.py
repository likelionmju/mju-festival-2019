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
            lost.author = request.user
            lost.pub_date = timezone.now()
            lost.save()
        return redirect('lost_home')
    else:
        return render(request, 'lost_new.html')

def detail(request, stuff_id):
    stuff = get_object_or_404(Lost, pk=stuff_id)
    return render(request, 'lost_detail.html', {'stuff': stuff})

def delete(request, stuff_id):
    stuff = get_object_or_404(Lost, pk=stuff_id)
    if stuff.author == request.user:
        stuff.delete()
        return redirect('lost_home')
    else:
        return redirect('lost_detail', stuff_id)

def edit(request, stuff_id):
    stuff = get_object_or_404(Lost, pk=stuff_id)
    if request.method == 'POST':
        stuff.content = request.POST['content']
        # image 파일이 있으면 post 객체에 저장
        if 'image' in request.FILES:
            stuff.image = request.FILES['image']
        stuff.save()
        return redirect('/lost/detail/'+str(stuff.id))
    else:
        if stuff.author == request.user:
            return render(request, 'lost_edit.html', {'stuff':stuff})
        else:
            return redirect('lost_home')