#!/usr/bin/env python3
# coding=utf-8
# author = ljs

class site:
	def __init__(self,name,url):
		self.name= name
		self.__url=url
	def who(self):
		print('name',self.name)
		print('url',self.__url)


	def __foo(self):
		print('私有方法')

	def foo(self):
		print('这是共有方法')
		self.__foo()

x = site('benbi','www.benbi.cn')
x.who()
x.foo()
x.__foo()


