from django.shortcuts import render, render_to_response, redirect
from django.http import Http404, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

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
                    tmp["Status"] = "up"
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
    return render(request,'bs1/containers/create.html',locals())

def destroy(request, container, engine):
    data = docker(engine,'containers/'+container+'/kill','POST','')
    data1 = docker(engine,'containers/'+container+'?v=1&force=1' ,'DELETE','')
    #return HttpResponse('destroy ' + container)
    print data,data1
    return HttpResponseRedirect('/containers/list')

def detail(request,container,engine):
    #print container,engine
    #container = containers.split("?")
    #for x in container:
    #    print x
    print "x" * 17
    print engine
    print "x" * 17
    data = docker(engine,'containers/'+ container + '/json','GET','')
    all = data
    #print type(data)
    print all["State"]


    return render(request,'bs1/containers/detail.html',locals())
    #return HttpResponse(containers)

def start(request, container, engine):
    data = docker(engine,'containers/'+container+'/start','POST','')
    #return redirect('containers/detail/'+ container+engine)
    #return redirect('/aa')
    return HttpResponseRedirect('/containers/detail/'+container+'/'+engine)
#    return HttpResponse(data )

def stop(request, container, engine):
    data = docker(engine,'containers/'+container+'/stop','POST','')
    return HttpResponseRedirect('/containers/detail/'+container+'/'+engine)
    #return HttpResponse('/containers/detail/'+container+engine)

def restart(request, container, engine):

    data = docker(engine,'containers/'+container+'/restart','POST','')
    #return HttpResponse('restart ' + container)
    return HttpResponseRedirect('/containers/detail/'+container+'/'+engine)


