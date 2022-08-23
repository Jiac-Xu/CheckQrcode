"""
Created on Mon Aug 22 21:37:53 2022

@author: Xu
"""


from easygui import boolbox
from pyperclip import copy
from webbrowser import open
from pyzbar.pyzbar import decode
from PIL import ImageGrab

#识别二维码
img = ImageGrab.grab()
texts = decode(img)

#输出结果
result=[]
for text in texts:
    tt=text.data.decode("utf-8")
    result.append(tt)

#美化结果
res=""
for i in range(0,len(result)):
    res+=str(result[i])+"\n"

wx,wy,wz=0,0,0
wxsave=""
for i in range(0,len(result)):
    if "." in str(result[i]):
        if "wechat_redirect" in str(result[i]):
            wx+=1
        else:
            wy+=1            
    else:
        wz+=1
    
#GUI管理     
msg="共识别网页{}条，文字{}条，微信链接{}条\n点击“打开”后，将会复制微信链接至剪贴板，请粘贴到微信打开。\n{}".format(wy,wz,wx,res)
title="识别到"+str(len(result))+"个结果："
if boolbox(msg,title,choices=("打开","复制")):
    for i in range(0,len(result)):
        if "." in str(result[i]):
            if "wechat_redirect" in str(result[i]):
                wxsave+=str(result[i])+"\n"
            else:
                open(str(result[i]))            
        else:
            continue
        copy(wxsave)
else:
    copy(res) 