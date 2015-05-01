__author__ = 'andi'

from functional_collections import *

def test_hyperduck():
	Dog = caseclass("Dog", [("name", str), ("age", int)])

	@implicit(Dog, int)
	def dog2int(d):
		return d.age

	@takes(int)
	def multiply_int_by_2(i):
		assert(type(i) == int)
		return i*2

	result = multiply_int_by_2(Dog("Matthew", 13))
	assert(result == 26)

def test_hyperduck_stats():
	Dog = caseclass("Dog", [("name", str), ("age", int)])

	@implicit(Dog, int)
	def dog2int(d):
		return d.age

	@takes(int)
	def multiply_int_by_2(i):
		assert(type(i) == int)
		return i*2

	result = multiply_int_by_2(Dog("Matthew", 13))
	assert(result == 26)

	print get_hyperduck_stats(multiply_int_by_2)


if __name__ == "__main__":
	test_hyperduck()
	test_hyperduck_stats()