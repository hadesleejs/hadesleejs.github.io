#!/usr/bin/env python3
# coding=utf-8
# author = ljs



i = int(input('净利润：'))
arr = [100000,600000,400000,200000,1000000,0]
rat = [0.01,0.02,0.03,0.04,0.05,0.06,0.07]

r = 0 


for idx in range(0,6):
	if i > arr[idx] :
		r+=(i-arr[idx])*rat[idx]
		print (i - arr[idx])*rat[idx]
		i = arr[idx]
print(r)