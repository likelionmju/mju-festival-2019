from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def board_new(request):
    return redirect('board_detail')

def board_delete(request):
    return redirect('board_detail')

def lost_new(request):
    return redirect('lost_detail')

def lost_delete(request):
    return redirect('lost_detail')