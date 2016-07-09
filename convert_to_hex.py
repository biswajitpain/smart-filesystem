#!/usr/bin/python

with open ('testfile','r') as fi, open('testhex','w') as fo:
	s=fi.readlines()
	k=s[0]
	for i in k:
		fo.write(hex(ord(i)))