#!/usr/bin/python
# -*- coding: utf8 -*-
import re
from mydict import mydict

def getSource(filename):
  f = open(filename,'r')
  source = f.readlines()  
  return source

def translate(before,thedict):
  after = before
  for src,dest in thedict.iteritems():
    pattern = "(" + src + ")"
    p = re.compile(pattern)
    after = p.sub(dest,after)
  return after

if __name__ == '__main__' :
  source = getSource('input.txt')
  for before in source:
    after = translate(before,mydict)
    print before + " : " + after
