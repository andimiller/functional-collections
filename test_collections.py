__author__ = 'andi'

from functional_collections import *

def test_map():
	assert([1,2,3].map(lambda x:x*2) == [2,4,6])
