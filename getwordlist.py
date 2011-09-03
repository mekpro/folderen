#!/usr/bin/python
# -*- coding: utf8 -*-
import unicodedata
import codecs 

def getSource(filename):
  f = codecs.open(filename,'r','utf-8','strict')
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

def getUnicodeName(w):
  import unicodedata
  r1 = unicodedata.name(w[0])
  r2 = r1.split()
  UnicodeName = r2[0]
  return UnicodeName

def filtering(mylist):
  #todo: get only japanese text!
  newlist = []
  for w in mylist:
    un = getUnicodeName(w)
    if (un == 'KATAKANA') or (un == 'HIRAGANA') or (un == 'CJK'):
      newlist.append(w)
  return newlist 


mylist = []
lines = getSource('full_input.txt')
for line in lines:
  words = line.split()
  for word in words:
    word = word.replace('[','')
    word = word.replace(']','')
    mylist.append(word)

#mylist = uniquify(mylist)
mylist = filtering(mylist)
mylist = wordcount(mylist)

for word,count in mylist.items():
  print >>open('output.txt', 'a'), count , ":", word.encode('utf-8')
