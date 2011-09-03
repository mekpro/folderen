import nose
import unittest 
from getwordlist import * 

class test_getwordlist(unittest.TestCase):
  def setUp(self):
    "Initializing test"

  def tearDown(self):
    print "Finalizing test"

  def test_getSource(self):
    lines = getSource('input.txt')
    self.assertEqual(len(lines),7,"invalid input reader") 

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
