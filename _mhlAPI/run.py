from .xcdl import *
from .dl import *
from .url import *
from time import sleep
from json import loads
dl=xcdl()
def v():
    url='https://launchermeta.mojang.com/mc/game/version_manifest.json'
    dl.dnldfile(url,pathurl(url))
    url='https://launchermeta.mojang.com/mc/game/version_manifest_v2.json'
    dl.dnldfile(url,pathurl(url))
def start(tim):
    while 1:
        bqmc(dl,vers(),512)
        v()
        sleep(tim)
