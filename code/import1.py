#!/usr/bin/env python3
# coding=utf-8
# author = ljs


import os
os.getcwd()

def Reverse(lst):
	return [ele for ele in reversed(lst)]

lst = [10,11,12,13,14,15]

print(Reverse(lst))


def Reverse1(lst):
	lst.reverse()
	return lst


lst = [10,11,12,13,14,15]

print(Reverse1(lst))