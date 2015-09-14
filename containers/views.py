from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponseRedirect
from django.http import HttpResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
import urllib3

from command.docker import docker,getdata
from engines.models import Engines

# Create your views here.

def list(request):
    allengines = Engines.objects.all()
    all=[]
    for x in allengines:
        data = docker(x.Addr,'containers/json?all=1','GET','')
        datajson = data
        #print data
        for t in data:
            tmp={}
            print t
            print "x" *80
            try:
                if t["Status"].find('Up') != -1:
                    tmp["Status"] = "Up"
                elif t["Status"].find('Exited') != -1:
                    tmp["Status"] = "Down"
                tmp["Id"] = t["Id"]
                tmp["Names"] = t["Names"][0]
                tmp["Image"] = t["Image"]
                tmp["Engine"] = x.Addr
                all.append(tmp)
            except:
                pass

    print all

    return render(request,'bs1/containers/list.html',locals())
#    return HttpResponse('list')

def create(request):
    return HttpResponse('create')

def destroy(request):
    return HttpResponse('destroy')

def detail(request,containers):
    return render(request,'bs1/containers/detail.html',locals())
    #return HttpResponse(containers)

def start(request):
    return HttpResponse('start')

def stop(request):
    return HttpResponse('stop')

def restart(request):
    return HttpResponse('restart')


