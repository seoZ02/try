from django.shortcuts import render, get_object_or_404
from .models import First
# Create your views here.

def home(request):
    allblogs = First.objects.all()
    return render(request, 'home.html', {'ablog':allblogs})

def detail(request, id):
    oneblog = get_object_or_404(First, pk = id)
    return render(request, 'detail.html', {'o':oneblog})