#!/usr/bin/python
# -*- coding: utf8 -*-

def getSource():
  f = open('sorted.txt','r')
  source = f.readlines()
  return source

def uniquify(mylist):
  myset = set(mylist)
  newlist = [] 
  for i in myset:
    newlist.append(i)
  newlist.sort()
  return newlist

def filtering(mylist):
  return mylist

mylist = []
lines = getSource()
for line in lines:
  words = line.split()
  for word in words:
    word = word.replace('[','')
    word = word.replace(']','')
    mylist.append(word)

mylist = uniquify(mylist)
mylist = filtering(mylist)

for w in mylist:
  print w
