from django.shortcuts import render

from models import Engines
from forms import AddEngineForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def lists(request):
    allengines = Engines.objects.all()
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
    return render(request,'bs1/engines/remove.html',locals())

def detail(request):
    return render(request,'bs1/engines/detail.html',locals())

