#!/usr/bin/env python
import json



s = '__guid=17726245.802017517894455900.1509584201948.9084; _job910utmc=d9c9b2a6-7492-4b9f-9e2c-b2f096b4775e; _utmc=5dc1dxtojfn4y1eptkozthpm; _chat_cuid=w7W/X/lo6UHkvhkuQ8yA6g4geqy6VZzTgxFJ/9aahWIgT1uwWGVJNfP+wDpnetxfOvKHHkfBusZDJ6caCVHsAQ==; _chat_cuid.sig=7Dmxp78tWG04YBl13HxRpvdFgrI; Hm_lvt_10fe842eb8d711feaf59d650aee966e0=1527122006,1527235151,1527467973,1527554063; Hm_lpvt_10fe842eb8d711feaf59d650aee966e0=1527554214'
s1 = s.split('=')
for item in s1:
	if item == '':

s2 = {"__guid":"17726245.802017517894455900.1509584201948.9084",
"_job910utmc":"d9c9b2a6-7492-4b9f-9e2c-b2f096b4775e",
"_utmc":"5dc1dxtojfn4y1eptkozthpm",
"_chat_cuid":"w7W/X/lo6UHkvhkuQ8yA6g4geqy6VZzTgxFJ/9aahWIgT1uwWGVJNfP+wDpnetxfOvKHHkfBusZDJ6caCVHsAQ==",
"_chat_cuid.sig":"7Dmxp78tWG04YBl13HxRpvdFgrI",
"Hm_lvt_10fe842eb8d711feaf59d650aee966e0":"1527122006,1527235151,1527467973,1527554063",
"Hm_lpvt_10fe842eb8d711feaf59d650aee966e0":"1527554214"}	
	
print(s1)