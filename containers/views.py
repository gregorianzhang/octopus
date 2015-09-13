from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.

def list(request):

    return render(request,'bs1/containers/list.html',locals())
#    return HttpResponse('list')

def create(request):
    return HttpResponse('create')

def destroy(request):
    return HttpResponse('destroy')

def detail(request):
    return HttpResponse('detail')

def start(request):
    return HttpResponse('start')

def stop(request):
    return HttpResponse('stop')

def restart(request):
    return HttpResponse('restart')


