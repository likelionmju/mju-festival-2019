from django.shortcuts import render, get_object_or_404, redirect
from .models import Board
from .forms import BoardForm
from django.utils import timezone

# Create your views here.

def home(request):
    boards = Board.objects.all()
    return render(request, "board.html", {'boards':boards})

#글작성 (new)
def new(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            lost = form.save(commit=False)
            lost.pub_date = timezone.now()
            lost.save()
        return redirect('board_home')
    else:
        form = BoardForm()   
        return render(request, "board_new.html", {'form':form})

#상세보기(detailed view)
def detail(request, board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    return render(request, "board_detail.html", {'board_detail':board_detail})
