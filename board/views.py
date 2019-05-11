from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

#글작성 (new)
def post_new(request):
    return render(request, "post_new.html")

#상세보기(detailed view)
def post_detail(request, post_id):
    return render(request, "post.html")