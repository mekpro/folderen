#!/usr/bin/python
# -*- coding: utf8 -*-
import re
from mydict import mydict

def progressBenchmark():
  #todo: count translated word percentages by all japanese words
  print "progress = 0"

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
  source = getSource('full_input.txt')
  for before in source:
    after = translate(before,mydict)
    print after
