from django.shortcuts import render

# Create your views here.

def lists(request):
    page = '23'
    print "aaaaa"
    #return "ttt"
    return render(request,'bs1/images/lists.html',locals())
