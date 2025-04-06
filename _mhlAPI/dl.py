from .url import *
import os,hashlib
import threading as thh
from time import sleep
vers,th=[],0
Threads=[]
hashing=0
def exists(p):
    return os.path.exists(p)
def ghash(f,typ='sha1'):
    global hashing
    while hashing>=2:sleep(0.01)
    hashing+=1
    with open(f,'rb') as f:
        while True:
            try:
                sha1=hashlib.sha1()
                sha1.update(f.read())
                hashing-=1
                return sha1.hexdigest()
            except:pass
def chck(uu,pp,zz,dl,thread):
    urls,paths=[],[]
    for i in range(len(uu)):
        a,b,c=uu[i],pp[i],zz[i]
        if exists(b) and ghash(b)==c:
            continue
        urls.append(a);paths.append(b)
    if urls and paths:
         dl.dl(urls,paths,thread,1000000,0)
def mcver(dl,ver,vd,thread,b=0):
    url=verjsurl(ver,vd)
    path=pathurl(url)
    print(ver,'json')
    if not exists(path):dl.dnldfile(url,path,1000000)
    vdc=ljs(path)
    url=assurl(vdc)
    path=pathurl(url)
    if not exists(path):dl.dnldfile(url,path,1000000)
    assdc=ljs(path)
    if b:return
    clients,cliz=clienturl(vdc,1)
    clientpath=psurl(clients)
    lib,libpath,libz=libraries(vdc,1)
    vdc=None
    ass,asspath,assz=assets(assdc,1)
    assdc=None
    print(ver,'client')
    chck(clients,clientpath,cliz,dl,thread)
    print(ver,'libraries')
    chck(lib,libpath,libz,dl,thread)
    print(ver,'assets')
    chck(ass,asspath,assz,dl,thread)
def thver(dl,vd,thread):
    global vers,th
    while len(vers)>0:
        ver=vers.pop(0)
        mcver(dl,ver,vd,thread)
    th+=1
def bqmc(dl,vd,thread,join=1):
    global vers,th,Thread
    bqt=thread//2
    thread=thread//2
    if vers:thread=th
    else:th=0
    vers=vers+[i['id'] for i in allv(vd)]
    for i in range(thread):
        while True:
            try:
                st=thh.Thread(target=thver,args=(dl,vd,bqt))
                st.start()
                Threads.append(st)
                break
            except:raise
    if join:
        for i in Threads:
            i.join()
