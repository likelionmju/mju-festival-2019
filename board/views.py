from django.shortcuts import render
from .models import Board

# Create your views here.

def home(request):
    posts = Board.objects.all()
    return render(request, "post.html", {'posts':posts})

#글작성 (new)
def post_new(request):
    return render(request, "post_new.html")

#상세보기(detailed view)
def post_detail(request):
    return render(request, "post_detail.html")