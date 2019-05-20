#!/usr/bin/env python3
# coding=utf-8
# author = ljs


counter = 0
for i in range(1,5):
	for x in range(1,5):
		for j in range(1,5):
			if (i != x) and (x != j ) and (i != j):
				counter +=1
				print(i,x,j,counter)
