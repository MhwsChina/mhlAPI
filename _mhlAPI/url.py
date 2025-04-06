import requests as req
import os
from time import sleep
from json import loads
#版本json v1/packages/sdafasdfasdfasdf/fasdfasd.json
#版本列表 mc/game/version_manifest.json
#版本列表(带sha1) mc/game/version_manifest_v2.json
def pj(*args):
    return os.path.join(*args).replace('\\','/')
def vers(txt=0,v2=0):
    url="https://launchermeta.mojang.com/mc/game/version_manifest.json"
    if v2:url='https://launchermeta.mojang.com/mc/game/version_manifest_v2.json'
    res=req.get(url,timeout=1000000)
    if txt:return res.text
    return res.json()
def pathurl(url):
    url=url.replace('http://','')
    url=url.replace('https://','')
    return '/'.join(url.split('/')[1:])
def ljs(path):
    with open(path,'rb') as f:
        return loads(f.read())
def psurl(ls):
    ls1=[]
    for i in ls:
        ls1.append(pathurl(i))
    return ls1
def allv(vdc,find=''):
    finds=[]
    tmp=0
    for i in vdc['versions']:
        if tmp>=50:
            sleep(0.000000001)
            tmp=0
        if find==i['id'] or find==i['type'] or not find:
            finds.append(i)
        tmp+=1
    if len(finds)==1:return finds[0]
    return finds
def verjsurl(ver,vdc):
    verurl=allv(vdc,ver)
    return verurl['url']
def assurl(verjs):
    return verjs['assetIndex']['url']
def allverurl(vdc):
    url=[]
    for i in allv(vdc):
        url.append(i['url'])
    return url
def clienturl(vdc,bq=0):
    url=[]
    ss=[]
    for i in vdc['downloads']:
        if not i=='client':continue
        if bq:ss.append(vdc['downloads'][i]['sha1'])
        url.append(vdc['downloads'][i]['url'])
    if bq:return url,ss
    return url
def libraries(vdc,bq=False,d='maven'):
    us,ps,ss=[],[],[]
    for lib in vdc['libraries']:
        sleep(0.000000000000000000001)
        if "artifact" in lib["downloads"] and not "classifiers" in lib["downloads"]:
            if lib["downloads"]["artifact"]["url"]=='':continue
            url=str(lib["downloads"]["artifact"]["url"])
            path=pj(d,lib["downloads"]["artifact"]["path"])
            us.append(url);ps.append(path)
            if bq:ss.append(lib["downloads"]["artifact"]['sha1'])
        if "classifiers" in lib["downloads"]:
            if "artifact" in lib["downloads"]:
                url = lib["downloads"]["artifact"]["url"]
                path = pj(d,lib["downloads"]["artifact"]["path"])
                us.append(url);ps.append(path)
                if bq:ss.append(lib["downloads"]["artifact"]['sha1'])
            for cl in lib["downloads"]["classifiers"].values():
                url=cl["url"]
                path=pj(d,cl["path"])
                us.append(url);ps.append(path)
                if bq:ss.append(cl['sha1'])
    if bq:return us,ps,ss
    return us,ps
def assets(assdc,bq=False,d='assets'):
    us,ps,ss=[],[],[]
    tmp=0
    for obj in assdc['objects'].values():
        if tmp>=1000:
            sleep(0.0000001)
            tmp=0
        url=f"https://resources.download.minecraft.net/{obj['hash'][0:2]}/{obj['hash']}"
        path=pj(d,f"{obj['hash'][0:2]}/{obj['hash']}")
        us.append(url);ps.append(path)
        if bq:ss.append(obj['hash'])
        tmp+=1
    if bq:return us,ps,ss
    return us,ps

    
