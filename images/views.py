from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from engines.models import Engines
import json
import urllib3
import datetime


http = urllib3.PoolManager(timeout=3.0)

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
    #print allengines1
    images =[]
    bb={}
    n=1
    for x in allengines1:
        #print x.Addr
        tt = json.loads(docker(x.Addr,'images/json','GET',''))
        #print tt[0]
        #print len(tt),type(tt)
        #print tt
        print "---------------"
        print bb
        print "8888888888888888888888888"
        if not isinstance(tt,list):
            continue
        else:
            for yy in tt:
            #print yy.has_key('Id')
            
                bb['number']=n
                #print yy['Created']
                #print yy['RepoTags']
                bb['REPOSITORY']=yy['RepoTags'][0].split(':')[0]
                bb['TAG']=yy['RepoTags'][0].split(':')[1]
            #print yy['Id']
                bb['image_id']=yy['Id']
                bb['VirtualSize']=yy['VirtualSize']
                bb['date']=datetime.datetime.fromtimestamp(yy['Created'])
                bb['engine']=x.Addr
                n = n + 1
                images.append(bb)
                bb={}
    print images
    if images:
        bb = images
    #    vdata = getdata(docker(x.Addr,'images/json','GET',''),'Id')
    #    print vdata

    return render(request,'bs1/images/lists.html',locals())
