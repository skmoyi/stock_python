# import time
#
# def times(func):
# 	print(time.time())
#
# 	return func()
#
# @times
# def test():
# 	print("hello world")
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.taobao.com')
