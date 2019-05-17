#!/usr/bin/env python3
# coding=utf-8
# author = ljs


def countX(lst, x):
	count = 0
	for ele in lst:
		if (ele == x):
			count = count + 1
			print(count)
		return count

lst = [8,6,8,10,8,20,10,8,8]
x = 8 

count = 0
for i in lst:
	if i == x:
		count +=1
		print(i,count)
print(countX(lst, x))