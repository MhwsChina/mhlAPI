from _mhlAPI import *
from flask import *
from os.path import exists,join
import threading as th
print('mhlAPI v0.0.2')
def pj(*args):
    return join(*args).replace('\\','/')
a=input('1.是否循环补全文件?(y/n)')
if a=='y':tmp=int(input('延迟(分):'))*60
b=input('2.是否运行在公网ipv6(y/n)')
if a=='y':th.Thread(target=start,args=(tmp,)).start()
app=Flask('mhlAPI')
app.secret_key='mhlAPI114514114514114514114514'
ind='''
<p>版本信息</p>
<p>http://mhlapi的网址/mc/game/version_manifest.json</p>
<p>http://mhlapi的网址/mc/game/version_manifest_v2.json</p>
<p>用法</p>
<p>所有http://piston-meta.mojang.com替换为"http://mhlapi的网址"</p>
<p>所有http://piston-data.mojang.com替换为"http://mhlapi的网址"</p>
<p>所有http://libraries.minecraft.net替换为"http://mhlapi的网址/maven"</p>
<p>所有http://resources.download.minecraft.net替换为"http://mhlapi的网址/assets"</p>
'''[0:-1]
@app.route('/')
def index():
    return ind
@app.route('/assets/<path:path>')
def assets(path):
    path=pj('assets',path)
    if exists(path):return send_file(path)
    else:
        return "{'code': 404,'text': 'file not found'}",404
@app.route('/maven/<path:path>')
def libraries(path):
    path=pj('maven',path)
    if exists(path):return send_file(path)
    else:
        return "{'code': 404,'text': 'file not found'}",404
@app.route('/v1/<path:path>')
def v1(path):
    path=pj('v1',path)
    if exists(path):return send_file(path)
    else:
        return "{'code': 404,'text': 'file not found'}",404
@app.route('/mc/<path:path>')
def mc(path):
    path=pj('mc',path)
    if exists(path):return send_file(path)
    else:
        return "{'code': 404,'text': 'file not found'}",404
if b=='n':app.run(host='0.0.0.0',port=80)
else:app.run(host='::',port=80)
