from __future__ import print_function
__author__ = 'andi'

if __name__=="__main__":
	from functional_collections import *
	# 1 to 10 mapped _*2, reduced on _+_
	range(1,10).map(lambda x:x*2).reduce(lambda a,b: a+b)
	# flatten a list and regroup it
	r = [[1,2], [3,4], [5,6]].flatten().grouped(3).toList()
	print(r)
	# scala style partial folds
	r = range(0,9).reversed().foldRight("")(lambda x,y:x+str(y))
	print(r)
	r = range(0,9).foldLeft("")(lambda x,y:x+str(y))
	print(r)
	# shuffle, group into lists of 2 length, sort by sublist total, map total, filter on even results, reduce on sum
	r = range(0,100)\
		.shuffle()\
		.grouped(2)\
		.toList()\
		.sorted(key=lambda x: x[0]+x[1])\
		.map(lambda x:x[0]+x[1])\
		.filter(lambda x:x%2==0)\
		.reduce(lambda x,y: x+y)
	print(r)
	# collect
	r = range(0,100).collect(lambda x:x%2)
	print(r)
	# my closest approximation of pattern matching
	class Bar():
		pass
	import types
	["foo", 42, Bar()].match(
		{
			types.StringType: lambda x:print("I got a string: "+x),
			types.IntType: lambda x:print("I got an int: %d" % x),
			Bar: lambda x:print("I got a Bar")
		}
	)
	# collect with type
	r = ["foo", 42, Bar()].collect(lambda x:type(x))
	print(r)
	# collect with class
	r = ["foo", 42, Bar()].collect()
