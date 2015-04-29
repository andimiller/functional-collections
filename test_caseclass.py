__author__ = 'andi'

from functional_collections import *

def test_empty_class():
	caseclass("Empty", [])

def test_basic_types():
	IntWrapper = caseclass("IntWrapper", [("i", int)])
	i = IntWrapper(42)
	assert(i.i == 42)
	try:
		i2 = IntWrapper("not an int")
		assert False, "didn't throw the correct exception"
	except TypeError as e:
		assert e.message == "i must be of type int"

class FooInt():
	def __init__(self, i):
		self.i = i

def test_class_types():
	FooIntWrapper = caseclass("FooIntWrapper", [("i", FooInt)])
	i = FooIntWrapper(FooInt(42))
	assert(i.i.i == 42)
	try:
		i2 = FooIntWrapper("not an int")
		assert False, "didn't throw the correct exception"
	except TypeError as e:
		assert e.message == "i must be of type FooInt"

test_class_types()

def test_hashcode():
	IntWrapper = caseclass("IntWrapper", [("i", int)])
	i = IntWrapper(78)
	i2 = IntWrapper(78)
	i3 = IntWrapper(77)
	assert(i == i2)
	assert(i != i3)

