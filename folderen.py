#!/usr/bin/python
# -*- coding: utf8 -*-
import re
from mydict import mydict

def getSource():
  #source = []
  #source.append("this is ヤングチャンピオン Book")
  f = open('sorted.txt','r')
  source = f.readlines()  
  return source

def translate(before,thedict):
  after = before
  for src,dest in thedict.iteritems():
    pat = "(" + src + ")"
    p = re.compile(pat)
    after = p.sub(dest,after)
  return after

if __name__ == '__main__' :
  source = getSource()
  for before in source:
    after = translate(before,mydict)
    print before + " : " + after
