import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
import pylab as pl
from PIL import Image
import opendatasets
img0 = "images/train/_111510370_060683565.jpg"
_ = plt.figure(figsize = (15,20))
_ = plt.axis('off')
_ = plt.imshow(mpimg.imread(img0))
directory = 'images/train'

imagepath=[]
imagefile=[]
boxset=[]
boxfile=[]

for im in os.listdir(directory):
    if im[-5:]=='.jpeg':
        path=os.path.join(directory,im)
        imagepath+=[path]
        imagefile+=[im]
    elif im[-4:]=='.jpg':
        path=os.path.join(directory,im)
        imagepath+=[path]
        imagefile+=[im]
        
for im in imagefile:
    if im[-5:]=='.jpeg':
        bx=im[0:-5]+'.txt'
        path=os.path.join(directory,bx)
        bxdata=np.loadtxt(path)
        boxset+=[bxdata]
        boxfile+=[bx]
    elif im[-4:]=='.jpg':
        bx=im[0:-4]+'.txt'
        path=os.path.join(directory,bx)
        bxdata=np.loadtxt(path)
        boxset+=[bxdata]
        boxfile+=[bx]
        print(imagefile[0:5])
print(boxfile[0:5])
print(len(boxset))
print(len(imagepath))
def draw_bbox2(num0):
    
    img0=imagepath[num0]
    box0=boxset[num0]
    print(box0)
    print(img0)
    im = Image.open(img0)
    W,H = im.size
    print(im.size)  
    _ = plt.figure(figsize = (15,20))
    _ = plt.axis('on')
    _ = plt.imshow(mpimg.imread(img0))   
    ax = plt.gca()
    ax.text(W*0.02,H*0.05,f'MASK',fontsize=20,color='yellow')
    ax.text(W*0.02,H*0.09,f'NO MASK',fontsize=20,color='red')
    
    if type(box0[0])==int:
        mk,x0,y0,w0,h0 = box0
        x=(x0-w0/2)*W
        y=(y0-h0/2)*H
        w=w0*W
        h=h0*H
        if mk==1:
            rect = patches.Rectangle((x,y),w,h,linewidth=2,edgecolor='yellow',fill = False)
        elif mk==0:
            rect = patches.Rectangle((x,y),w,h,linewidth=2,edgecolor='red',fill = False)
        ax.add_patch(rect)
        print(rect)
        plt.show
    else:
        for item in box0:
            arr = np.array(item, dtype=np.float64)
            print(arr)
            mk,x0,y0,w0,h0 = arr
            print(mk,x0,y0,w0,h0)
            x=(x0-w0/2)*W
            y=(y0-h0/2)*H
            w=w0*W
            h=h0*H
            if mk==1:
                rect = patches.Rectangle((x,y),w,h,linewidth=2,edgecolor='yellow',fill = False)
            elif mk==0:
                rect = patches.Rectangle((x,y),w,h,linewidth=2,edgecolor='red',fill = False)            
            ax.add_patch(rect)
            plt.show
            num0=0
for i in range(692):
    if imagepath[i]==img0:
        num0=i
        print(i)
draw_bbox2(num0)
draw_bbox2(10)
draw_bbox2(11)
draw_bbox2(18)
