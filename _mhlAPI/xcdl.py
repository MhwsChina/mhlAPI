import threading as th
import requests as rq
import os
from time import sleep
from .log import *
def pj(*args):
    return os.path.join(*args).replace('\\','/')
def exists(p):
    return os.path.exists(p)
def jd_tqdm(f1,thread):
    tmp,t=0,0
    for i in tqdm(range(f1),desc='进度',unit='文件'):
        if th>=thread:break
        while i>=f:sleep(0.1)
class xcdl:
    def __init__(self):
        self.Threads=[]
        self.files=[]
        self.timeout=10
        self.th=0
    def dnldfile(self,url,path,timeout=10,size=1048576):
        while True:
            try:
                res=rq.get(url,timeout=timeout)
                try:os.makedirs(os.path.split(path)[0])
                except:pass
                with open(path,'wb') as ff:
                    ff.write(res.content)
                res=None
                self.th+=1
                return
            except:pass
    def dnldfiles(self):
        name=th.current_thread().name
        print(name,'已启动')
        while self.files:
            url,path=self.files.pop(0)
            print(name+'-'+url)
            self.dnldfile(url,path,self.timeout)
    def dl(self,urls,paths,thread=128,timeout=10,join=1):
        if self.files:thread=self.th
        else:self.th=0
        if thread>len(urls):thread=len(urls)
        self.files=self.files+list(zip(urls,paths))
        self.timeout=timeout
        for i in range(thread):
            while True:
                try:
                    st=th.Thread(target=self.dnldfiles)
                    st.start()
                    self.Threads.append(st)
                    break
                except:pass
        if join:
            for i in self.Threads:
                i.join()
