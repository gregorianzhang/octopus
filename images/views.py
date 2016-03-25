from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from engines.models import Engines
import json
import urllib3

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
    print allengines1
    bb={}
    n=1
    for x in allengines1:
        print x.Addr
        tt = json.loads(docker(x.Addr,'images/json','GET',''))
        print tt
        print type(tt)
        #print tt[0]
        print len(tt),type(tt)
        for yy in tt:
            print "----------------------------------------------------"
            print yy,type(yy)
            #print yy.has_key('Id')
            #print yy['Id']

            bb['number']=n
            #print yy['Created']
            #print yy['RepoTags']
            #bb['REPOSITORY']=yy['RepoTags'][0].split(':')[0]
            #bb['TAG']=yy['RepoTags'][0].split(':')[0]
            #print yy['Id']
            #bb['image_id']=yy['Id']
            #bb['VirtualSize']=yy['VirtualSize']
            n = n + 1
    print bb
    #    vdata = getdata(docker(x.Addr,'images/json','GET',''),'Id')
    #    print vdata

    return render(request,'bs1/images/lists.html',locals())
