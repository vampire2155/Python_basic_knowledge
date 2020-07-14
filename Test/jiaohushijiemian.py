#!/usr/local/bin/python
#encoding=utf-8
from tkinter import *  #tkinter 是另外一个脚本
root = Tk()
textLabel = Label(root,text=u'您所下载的影片含有未成年人限制内容，\n请满18岁后再点击观看！',justify=LEFT,padx=10)
textLabel.pack(side=LEFT)
photo = PhotoImage(file="18.gif")
imgLabel = Label(root, image=photo)
imgLabel.pack(side=RIGHT)
mainloop()
print(textLabel)
