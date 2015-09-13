from django.shortcuts import render

from django.http import HttpResponse
from models import Engines
from forms import AddEngineForm

from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
import urllib3


http = urllib3.PoolManager()
# Create your views here.
def docker(host,command,method,data):
    #http = urllib3.PoolManager()
    url = host + "/" + command
    if method == 'GET':
        try:
            r = http.request(method,url)
        except :
            return '{"error":"error"}'
    elif method == 'POST':
        try:
            r = http.request(method,url,data)
        except :
            return '{"error":"error"}'
    else:
        print "Error"

    if r.status == 200:
        return r.data
    else:
        return '{"error":"error"}'

def getdata(data,key):
    temp = json.loads(data)
    try:
        return temp[key]
    except:
        return "error"

def lists(request):
    allengines1 = Engines.objects.all()
    allengines = []
    bb={}
    n=1
    for x in allengines1:
        bb['id'] = n
        bb['Name'] = x.Name
        bb['Cpus'] = x.Cpus
        bb['Memory'] = x.Memory
        bb['Addr'] = x.Addr
        vdata = getdata(docker(x.Addr,'version','GET',""),'Version')
        if vdata != 'error':
            bb['status']='up'
        else:
            bb['status']='down'
        bb['Version'] = vdata
        allengines.append(bb)
        print allengines
        bb={}
        n += 1


    limit = 25
    paginator = Paginator(allengines,limit)

    page = request.GET.get('page')
    if allengines:
        bb = allengines
    try:
        allengines = paginator.page(page)
        if int(page) <= 3:
            pages = [x for x in xrange(1,6)]
	    print "22222"
        elif int(page) +1 >= paginator.num_pages:
            pages = [x for x in xrange(int(paginator.num_pages)-4,int(paginator.num_pages)+1)]
	    print "33333"
        else :
            pages = [x for x in xrange(int(page)-2,int(page)+3)]
	    print "4444"

    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        allengines = paginator.page(1)
        pages = [x for x in xrange(1,6)]
	print "66666"
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        if paginator.num_pages < 5:
	    allengines = paginator.page(paginator.num_pages)
	    pages = [x for x in xrange(1,6)]
	else:
            allengines = paginator.page(paginator.num_pages)
            pages = [x for x in xrange(paginator.num_pages-6,paginator.num_pages)]
	print "55555"

    return render(request,'bs1/engines/lists.html',locals())

def add(request):

    if request.method == 'POST':
	engine = AddEngineForm(request.POST)
	if engine.is_valid():
	    print request
	    
	    aa = Engines(Name = request.POST['Name'],
                         Cpus = request.POST['Cpus'],
			 Memory = request.POST['Memory'],
			 Addr = request.POST['Addr']
			)
	    aa.save()

    else:
	aa = AddEngineForm()
	return render(request, 'bs1/engines/add.html',locals())

    return render(request,'bs1/engines/add.html',locals())

def remove(request):
    if request.method == 'POST':
	data = request.POST['engines']
	Engines.objects.filter(Addr=data).delete()
        #return HttpResponse("POST ABC")
	return HttpResponseRedirect('engines/lists/')
    else:
    #print request.POST['engines']
    
    #return render(request,'bs1/engines/remove.html',locals())
        return HttpResponseRedirect('engines/lists/')

def detail(request,engine):
    print engine
    bb = Engines.objects.filter(Addr=engine)
    print len(bb)
    cc = bb[0]
    print cc.Addr,cc.Name
    return render(request,'bs1/engines/detail.html',locals())


