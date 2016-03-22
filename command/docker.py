import urllib3
import json

def docker(host,command,method,data):
    http = urllib3.PoolManager()
    url = host + "/" + command
    print "docker url %s " % url
    if method == 'GET':
        try:
            r = http.request(method,url)
            if r.status == 200:
                #return r.data
                return json.loads(r.data)
            if r.status == 404:
                return json.loads('{"message":"no such container"}')
            if r.status == 500:
                return json.loads('{"message":"server error"}')


        except :
            return json.loads('{"error":"-1"}')
    elif method == 'POST':
        try:
            r = http.request(method,url,data)
            if r.status == 204:
                return json.loads('{"message":"no error"}')
            if r.status == 304:
                return json.loads('{"message":"container already " }')
            if r.status == 404:
                return json.loads('{"message":"no such container"}')
            if r.status == 500:
                return json.loads('{"message":"server error"}')

        except :
            return json.loads('{"error":"-2"}')
    elif method == 'DELETE':
        try:
            r = http.request(method,url)
            if r.status == 204:
                return json.loads('{"message":"no error"}')
            if r.status == 400:
                return json.loads('{"message":"bed parameter"}')
            if r.status == 404:
                return json.loads('{"message":"no such container"}')
            if r.status == 500:
                return json.loads('{"message":"server error"}')
            
        except :
            return json.loads('{"error":"-4"}')

    else:
        print json.loads('{"error":"-3"}')


def getdata(data,key):
    temp = json.loads(data)
    try:
        return temp[key]
    except:
        return "error"

