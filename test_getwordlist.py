import nose
import unittest 
import sys
import os
from getwordlist import * 

class test_getwordlist(unittest.TestCase):
  def setUp(self):
    "Initializing test"

  def tearDown(self):
    print "Finalizing test"

  def test_getSource(self):
    lines = getSource('input.txt')
    self.assertEqual(len(lines),7,"invalid input reader") 

  def test_wordcut(self):
    words = wordcut("[a] b")
    self.assertEqual(words,["a","b"],"invalid wordcut")

  def test_uniquify(self):
    mylist = [1,1,1,2,2,3]
    newlist = uniquify(mylist)
    self.assertEqual(newlist,[1,2,3],"invalid uniquify")
    pass

  def test_wordcount(self):
    mylist = [1,1,1,2,2,3]
    newlist = wordcount(mylist)
    self.assertEqual(newlist,{1:3,2:2,3:1},"invalid wordcount")
    pass

  def test_getUnicodeName(self):
    w = u'latin'
    unicodeName = getUnicodeName(w)
    self.assertEqual(unicodeName,'LATIN', "invalid unicodeName")
    pass

  def test_write_result(self):
    mydict = {'a' : 'x','b' : 'y'}
    mylist = {'a' : 1, 'b' : 2 }
    output_file = "test_output.txt"
    write_result(mylist,mydict,output_file)
    f = open(output_file)
    line1 = f.readline()
    self.assertEqual(line1,"1:a:x","invalid line1 "+line1+"!= 1:a:x")
    line2 = f.readline()
    self.assertEqual(line2,"2:b:y","invalid line1")

  
