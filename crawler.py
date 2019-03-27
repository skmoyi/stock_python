#!bin/usr/python
#coding:utf-8
from urllib import request,parse

page = urllib.urlopen('http://tieba.baidu.com/p/1753935195')
htmlcode = page.read()#读取页面源码

print(htmlcode)
