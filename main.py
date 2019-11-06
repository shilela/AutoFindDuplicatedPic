import os
import time
import shutil
import imagehash
from PIL import Image


class Pic:
    def __init__(self, filelct, phash):
        self.filelct = filelct
        self.phash = phash
        self.isRemoved = False

    def move(self, dst=r'.\duplication'):
        if self.isRemoved:
            return
        try:
            shutil.move(self.filelct, dst)
        except:
            shutil.move(self.filelct, dst+'\\'+str(time.time()
                                                   ).split(".")[1]+'.'+self.filelct.split(".")[-1])
        self.isRemoved = True


PicInfo = []

for root, dirs, files in os.walk(r".\pic"):
    for name in files:
        try:
            filename = os.path.join(root, name)
            phash = imagehash.phash(Image.open(filename))
            PicInfo.append(Pic(filename, phash))
        except:
            pass

if len(PicInfo) > 2:
    for i in range(len(PicInfo)-1):
        for j in range(i+1, len(PicInfo)):
            if PicInfo[i].phash - PicInfo[j].phash < 10:
                #print(PicInfo[i].phash - PicInfo[j].phash)
                PicInfo[i].move()
                PicInfo[j].move()
