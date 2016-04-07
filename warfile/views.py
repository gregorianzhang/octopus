from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from models import Warfile


from django.contrib.auth.decorators import login_required

@login_required(login_url='/account/login/')
def lists(request):
    #return HttpResponse("warfile")
    return render(request,'bs1/warfile/lists.html',locals())

def upload(request):
    return HttpResponse("warfile")
