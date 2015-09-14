import urllib3
import json

def docker(host,command,method,data):
    http = urllib3.PoolManager()
    url = host + "/" + command
    if method == 'GET':
        try:
            r = http.request(method,url)
        except :
            return json.loads('{"error":"-1"}')
    elif method == 'POST':
        try:
            r = http.request(method,url,data)
        except :
            return json.loads('{"error":"-2"}')
    else:
        print json.loads('{"error":"-3"}')

    if r.status == 200:
        #return r.data
        return json.loads(r.data)
    else:
        return json.loads('{"error":"-4"}')

def getdata(data,key):
    temp = json.loads(data)
    try:
        return temp[key]
    except:
        return "error"

