from django.shortcuts import render, get_object_or_404
from .models import Board

# Create your views here.

def home(request):
    boards = Board.objects.all()
    return render(request, "board.html", {'boards':boards})

#글작성 (new)
def new(request):
    return render(request, "board_new.html")

#상세보기(detailed view)
def detail(request, board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    return render(request, "board_detail.html", {'board_detail':board_detail})