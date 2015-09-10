from django.shortcuts import render

from models import Engines

# Create your views here.

def lists(request):
    allengines = Engines.objects.all()
    if allengines:
        bb = allengines
    return render(request,'bs1/engines/lists.html',locals())

def add(request):
    return render(request,'bs1/engines/add.html',locals())

def remove(request):
    return render(request,'bs1/engines/remove.html',locals())

def detail(request):
    return render(request,'bs1/engines/detail.html',locals())

