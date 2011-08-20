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

def wordcount(mylist):
  mydict = dict()
  for i in mylist:
    if i in mydict:
      mydict[i] += 1
    else:
      mydict[i] = 1 
  return mydict

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

#mylist = uniquify(mylist)
mylist = wordcount(mylist)
#mylist = filtering(mylist)

for key,value in mylist.items():
  print str(value) + " : " + key 
