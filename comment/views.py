from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import LostComment, BoardComment
from lost_property.models import Lost
from board.models import Board

# Create your views here.
def board_new(request, board_id):
    board = get_object_or_404(Board, pk=board_id)

    if request.method == 'POST':
        comment = BoardComment()
        comment.content = request.POST['comment']
        comment.title = board
        if request.user.is_authenticated:
            comment.author = request.user
        comment.pub_date = timezone.now()
        comment.save()
    return redirect('board_detail', board_id)

def board_delete(request, board_id, comment_id):
    comment = get_object_or_404(BoardComment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
    return redirect('board_detail', board_id)

def lost_new(request, stuff_id):
    lost = get_object_or_404(Lost, pk=stuff_id)

    if request.method == 'POST':
        comment = LostComment()
        comment.content = request.POST['comment']
        comment.title = lost
        if request.user.is_authenticated:
            comment.author = request.user
        comment.pub_date = timezone.now()
        comment.save()
    return redirect('lost_detail', stuff_id)

def lost_delete(request, stuff_id, comment_id):
    comment = get_object_or_404(LostComment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
    return redirect('lost_detail', stuff_id)