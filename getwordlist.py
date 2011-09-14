#!/usr/bin/python
# -*- coding: utf8 -*-
import unicodedata
import codecs 
import os
import pprint
from mydict import mydict

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

def wordcut(line):
  wordlist = []
  words = line.split()
  for word in words:
    w = word.replace('[','')
    w = w.replace(']','')
    w = w.strip()
    wordlist.append(w)
  return wordlist

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

def isJapanese(w):
  code = getUnicodeName(w)
  if (code == 'KATAKANA') or (code == 'HIRAGANA') or (code == 'CJK'):
    return True
  else:
    return False

def filtering(mylist):
  newlist = []
  for w in mylist:
    if isJapanese(w):
      newlist.append(w)
  return newlist 

def write_result(mylist,mydict,output_file):
  import sys
  os.popen('rm ' + output_file)
  for word,count in mylist.items():
    word = word.encode('utf-8')
    if (word in mydict):
      line = str(count)+":"+word+":"+mydict[word]
      print >>open(output_file, 'a'),line 
    else:
      line = str(count)+":"+word+":"
      print >>open(output_file, 'a'),line


def showProgress(mylist,mydict):
  translated_word = 0
  translated_dict = 0
  total_word = 0
  total_dict = 0
  for word,count in mylist.items():
    word = word.encode('utf-8')
    if (word in mydict):
      total_word += count
      total_dict += 1 
      translated_word += count 
      translated_dict += 1 
    else:
      total_word += count
      total_dict += 1 
  percent_word = float(float(translated_word)/float(total_word))*100
  percent_dict = float(float(translated_dict)/float(total_dict))*100
  print "Total translated word: " ,translated_word,"/", total_word, "(",percent_word,"%)"
  print "Total translated dict: " ,translated_dict,"/", total_dict, "(",percent_dict,"%)" 
  

input_file  = 'full_input2.txt' 
output_file = 'output.txt'

if __name__ == '__main__':
  mylist = []
  lines = getSource(input_file)
  for line in lines:
    wordlist = wordcut(line)
    for word in wordlist:
      mylist.append(word)

  mylist = filtering(mylist)
  mylist = wordcount(mylist)
  write_result(mylist,mydict,output_file)
  showProgress(mylist,mydict)
