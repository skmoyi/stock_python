#! usr/bin/python

# -*- coding:UTF-8 -*-
# from tkinter import *
#
# root = Tk()
#
# Scale(root,from_=0,to=42).pack()
# Scale(root,from_=0,to=200,orient=HORIZONTAL).pack()
#
# mainloop()

from tkinter import *

root = Tk()

Scale(root,from_=0,to=42,tickinterval=5,length=200,resolution=5,orient=VERTICAL).pack()
Scale(root,from_=0,to=200,tickinterval=10,length=600,orient=HORIZONTAL).pack()

mainloop()




# from tkinter import *
#
# root = Tk()
#
# Scale(root,from_=0,to=42).pack()
# Scale(root,from_=0,to=200,orient=HORIZONTAL).pack()
#
# mainloop()

# from tkinter import *
# root = Tk()
#
# s1=Scale(root,from_=0,to=42)
# s1.pack()
# s2=Scale(root,from_=0,to=200,orient=HORIZONTAL)
# s2.pack()
#
# def show():
#     print(s1.get(),s2.get())
#
# Button(root,text="获取位置",command=show).pack()
#
# mainloop()





# from tkinter import *
#
# root = Tk()
#
# sb = Scrollbar(root)
# sb.pack(side=RIGHT,fill=Y)
#
# lb = Listbox(root,yscrollcommand=sb.set)
# for i in range(1000):
#     lb.insert(END,str(i))
# lb.pack(side=LEFT,fill=BOTH)
# sb.config(command=lb.yview)
#
# mainloop()




# from tkinter import *
#
# root = Tk()
#
# theLB = Listbox(root,setgrid=True)
# theLB.pack()
#
# for item in range(11):
#     theLB.insert(END,item)
#
# mainloop()




# from tkinter import *
# root = Tk()
# theLB = Listbox(root,setgrid=True)
# theLB.pack()
#
# for item in ["篮球","足球","兵乓球","羽毛球"]:
#     theLB.insert(END,item)
# theButton=Button(root,text="删除",command=lambda x=theLB:x.delete(ACTIVE))
# theButton.pack()
#
# mainloop()








# from tkinter import *
#
# root = Tk()
#
# def test():
#     if e1.get()=="小甲鱼":
#         print("正确")
#         return True
#
#     else:
#         print("错误")
#         e1.delete(0,END)
#         return False
#
# v=StringVar()
# e1 = Entry(root,textvariable=v,validate="focusout",validatecommand=test)
# e2 = Entry(root)
# e1.pack(padx=10,pady=10)
# e2.pack(padx=10,pady=10)
#
# mainloop()




# from tkinter import *
#
# root= Tk()
#
# Label(root,text="User:").grid(row=0)
# Label(root,text="Password:").grid(row=1)
# e1=Entry(root)
# e2=Entry(root,show="*")
#
# e1.grid(row=0,column=1,padx=10,pady=10)
# e2.grid(row=1,column=1,padx=10,pady=10)
#
# def show():
#     print("User:<<%s>>"%e1.get())
#     print("Password:<<%s>>"%e2.get())
#     e1.delete(0,END)
#     e2.delete(0,END)
#
# Button(root,text="芝麻开门",width=10,command=show).grid(row=3,column=0,sticky=W,padx=10,pady=5)
# Button(root,text="退出",width=10,command=root.quit()).grid(row=3,column=1,sticky=E,padx=10,pady=5)
#
# mainloop()






# from tkinter import *
#
# root = Tk()
#
# Label(root,text="作品：").grid(row=0)
# Label(root,text="作者：").grid(row=1)
# e1=Entry(root)
# e2=Entry(root)
# e1.grid(row=0,column=1,padx=10,pady=10)
# e2.grid(row=1,column=1,padx=10,pady=5)
#
# def show():
#     print("作品：<<%s>>"%e1.get())
#     print("作者：<<%s>>"%e2.get())
#     e1.delete(0,END)
#     e2.delete(0,END)
#
#
# Button(root,text="获取信息",width=10,command=show).grid(row=3,column=0,sticky=W,padx=10,pady=5)
# Button(root,text="退出",width=10,command=root.quit()).grid(row=3,column=1,sticky=E,padx=10,pady=5)
#
# mainloop()





# from tkinter import *
#
# root = Tk()
# e=Entry(root)
# e.pack(padx=20,pady=20)
# e.delete(0,END)
# e.insert(0,"默认字体。。。")
#
# mainloop()



# from tkinter import *
#
# root = Tk()
# group = LabelFrame(root,text="最好的脚本语言是？",padx=5,pady=5)
# group.pack(padx=10,pady=10)
# LANGS=[('Python',1),('Perl',2),('Ruby',3),('Lua',4)]
# v = IntVar()
# v.set(1)
# for lang,num in LANGS:
#     b = Radiobutton(group,text=lang,variable=v,value=num)
#     b.pack(anchor=W)
#
# mainloop()





# from tkinter import *
#
# root = Tk()
# LANGS = [("Python",1),("Perl",2),("Ruby",3),("Lua",4)]
# v = IntVar()
# v.set(1)
# for lang,num in LANGS:
#     b=Radiobutton(root,text=lang,variable=v,value=num,indicatoron=False)
#     b.pack(fill=X)
#
# mainloop()




# from tkinter import *
#
# root = Tk()
# LANGS = [("Python",1),("Perl",2),("Ruby",3),("Lua",4)]
# v = IntVar()
# v.set(1)
# for lang,num in LANGS:
#     b=Radiobutton(root,text=lang,variable=v,value=num)
#     b.pack(anchor=W)
#
# mainloop()





# from tkinter import *
#
# root = Tk()
# v = IntVar()
# Radiobutton(root,text="One",variable=v,value=1).pack(anchor=W)
# Radiobutton(root,text="Two",variable=v,value=2).pack(anchor=W)
# Radiobutton(root,text="Three",variable=v,value=3).pack(anchor=W)
#
# mainloop()




# from tkinter import *
#
# root = Tk()
# GIRLS = ["西施","王昭君","貂蝉","杨玉环"]
# v=[]
# for girl in GIRLS:
#     v.append(IntVar())
#     b=Checkbutton(root,text=girl,variable=v[-1])
#     b.pack(anchor=W)
#
# mainloop()


# from tkinter import *
#
# def callback():
#     var.set("吹吧你，我才不信来！")
#
# root=Tk()
# frame1 =Frame(root)
# frame2 =Frame(root)
#
# var = StringVar()
# var.set('您所下载的影片含有未成年人限制内容,\n请满18岁后再点击观看！')
# textLabel =Label(frame1,textvariable=var,justify=LEFT)
# textLabel.pack(side=LEFT)
#
# photo =PhotoImage(file="C:\\Users\\Administrator\\Desktop\\python\\image\\cute.gif")
# imgLabel=Label(frame1,image=photo)
# imgLabel.pack(side=RIGHT)
#
# theButton= Button(frame2,text="已满18周岁",command=callback)
# theButton.pack()
# frame1.pack(padx=10,pady=10)
# frame2.pack(padx=10,pady=10)
#
# mainloop()




# from tkinter import *
#
# root = Tk()
#
# photo = PhotoImage(file="C:\\Users\\Administrator\\Desktop\\python\\image\\cute.gif")
# theLabel = Label(root,text="学Python\n到FishC",justify=LEFT,image=photo,compound=CENTER,font=("幼圆",20),fg="white")
# theLabel.pack()
#
# mainloop()




# from tkinter import *
#
# root = Tk()
#
# textLabel = Label(root,text="您所下载的影片含有未成年人限制内容，\n请满18岁后再点击观看！",justify=LEFT,padx=10)
# textLabel.pack(side=LEFT)
# photo = PhotoImage(file="C:\\Users\\Administrator\\Desktop\\python\\image\\cute.gif")
# imgLabel=Label(root,image=photo)
# imgLabel.pack(side=RIGHT)
#
# mainloop()





# import tkinter as tk
#
# class App:
#     def __init__(self,root):
#         frame = tk.Frame(root)
#         frame.pack()
#
#         self.hi_there = tk.Button(frame,text="打招呼",fg="#f46",command=self.say_hi,bg="blue")
#         self.hi_there.pack(side=tk.LEFT)
#
#     def say_hi(self):
#         print("互联网的广大朋友们大家好，我是初音未来！")
#
# root=tk.Tk()
# app = App(root)
#
# root.mainloop()

# import tkinter as tk
#
# root = tk.Tk()
#
# root.title("NEW")
#
# theLable = tk.Label(root,text="就是体验一下")
#
# theLable.pack()
#
# root.mainloop()



# from tkinter import *
#
# root = Tk()
#
# li =['C','python','php','html','SQl','java']
# movie = ['CSS','jQuery','Bootstrap']
# listb =Listbox(root)
# listb2 =Listbox(root)
# for item in li:
#     listb.insert(0,item)
# for item in movie:
#     listb2.insert(0,item)
#
# listb.pack()
# listb2.pack()
# root.mainloop()



# import tkinter
#
# top = tkinter.Tk()
#
# top.mainloop()
