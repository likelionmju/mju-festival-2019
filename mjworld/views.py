from django.shortcuts import render
from .models import Mjworld

# Create your views here.
def mjworld(request):
    mjworlds = Mjworld.objects.all()
    return render(request, 'mjworld.html', {'mjworlds':mjworlds})