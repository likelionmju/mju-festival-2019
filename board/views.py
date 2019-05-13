from django.shortcuts import render, get_object_or_404, redirect
from .models import Board
from django.utils import timezone

#자유게시판 홈(board)
def home(request):
    boards = Board.objects.all().order_by('-id')
    return render(request, "board.html", {'boards':boards})

#글작성 (new)
def new(request):
    if request.method == 'POST':
        board = Board()
        board.purpose = request.POST['purpose']
        board.title = request.POST['title']
        if request.user.is_authenticated:
            board.author = request.user
        # image 파일이 있으면 post 객체에 저장
        if 'image' in request.FILES:
            board.image = request.FILES['image']
        board.pub_date = timezone.datetime.now()
        board.content = request.POST['content']
        board.save()
        return redirect('board_home')
    else:
        return render(request, "board_new.html")

#상세보기(detailed view)
def detail(request, board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    return render(request, "board_detail.html", {'board_detail':board_detail})

def delete(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if board.author == request.user:
        board.delete()
        return redirect('board_home')
    else:
        return redirect('board_detail', board_id)

def edit(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if request.method == 'POST':
        board.purpose = request.POST['purpose']
        # image 파일이 있으면 post 객체에 저장
        if 'image' in request.FILES:
            board.image = request.FILES['image']
        board.content = request.POST['content']
        board.save()
        return redirect('/board/detail/'+str(board.id))
    else:
        if board.author == request.user:
            return render(request, 'board_edit.html', {'board':board})
        else:
            return redirect('board_home')