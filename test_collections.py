__author__ = 'andi'

from functional_collections import *

def test_listmap():
	assert([1,2,3].map(lambda x:x*2) == [2,4,6])

def test_listfilter():
	assert([1,2,3].filter(lambda x:x%2!=0) == [1,3])

def test_listfilterNot():
	assert([1,2,3].filterNot(lambda x:x%2==0) == [1,3])

def test_listreduce():
	assert([1,2,3].reduce(lambda x,y: x+y) == 6)
	assert(["a", "b", "c"].reduce(lambda x,y: x+y) == "abc")

def test_listzip():
	assert([1,3,5].zip([2,4,6]) == [(1,2),(3,4),(5,6)])

def test_listflatten():
	assert([(1,2),(3,4),(5,6)].flatten() == [1,2,3,4,5,6])

def test_listjoin():
	assert([1,2,3].join(", ") == "1, 2, 3")
	assert([1,2,3].mkString(", ") == "1, 2, 3")

def test_listtoDict():
	assert([(1,2),(3,4)].toDict() == {1:2, 3:4})

def test_listlen():
	assert([1,2,3].len() == 3)
	assert([1,2,3,4].length() == 4)
	assert([1,2,3,4,5].size() == 5)

def test_listenumerate():
	assert(list(["a", "b", "c"].enumerate()) == [(0, "a"), (1, "b"), (2, "c")])

def test_listiter():
	i = [1,2,3].iter()
	assert(i.next() == 1)
	assert(i.next() == 2)
	assert(i.next() == 3)
	i = [1,2,3].iterate()
	assert(i.next() == 1)
	assert(i.next() == 2)
	assert(i.next() == 3)

def test_listmax():
	assert([1,7,2].max() == 7)

def test_listmin():
	assert([1,7,2].min() == 1)

def test_listtoSet():
	assert([1,1,2].toSet() == set([1,2]))

def test_listsorted():
	assert([2,1,7,5].sorted() == [1,2,5,7])

def test_listsim():
	assert([1,18,2].sum() == 21)

def test_listtotuple():
	assert([1,7,5].toTuple() == (1,7,5))

def test_listdistinct():
	assert([1,1,2,1].distinct() == [1,2])

def test_listfind():
	assert([1,2,3,4].find(lambda x:x==3) == 3)
	assert([1,2,3,4].find(lambda x:x==42) == None)
	assert([1,2,3,4].find(lambda x:x=="fish") == None)

def test_listexists():
	assert([1,2,3,"cat"].exists(lambda x:x=="cat") == True)

def test_list_flatMap():
	assert([(1,2),(3,4)].flatMap(lambda x:x*2) == [2,4,6,8])

def test_listfold():
	assert([1,2,3,4].fold(0)(lambda a,i: a+i) == 10)
	assert([1,2,3,4].foldRight([])(lambda a,i: a + [i, ""]) == [1,"",2,"",3,"",4, ""])

def test_listfoldleft():
	assert([1,2,3,4].foldLeft(0)(lambda a,i: a+i) == 10)
	assert([1,2,3,4].foldLeft([])(lambda a,i: a + [i, ""]) == [4,"",3,"",2,"",1, ""])

def test_list_forall():
	assert([1,2,3,4].forall(lambda x:x%2==0) == False)
	assert([2,4].forall(lambda x:x%2==0) == True)

def test_list_groupBy():
	"TODO work out what this does"

def test_list_grouped():
	assert(list([1,2,3,4,5,6].grouped(3)) == [[1,2,3],[4,5,6]])

def test_list_intersect():
	assert([1,2,3].intersect([2,3,4]) == set([2,3]))

def test_list_empty():
	assert([].empty() == True)
	assert([1].empty() == False)

def test_list_nonEmpty():
	assert([].nonEmpty() == False)
	assert([1].nonEmpty() == True)

def test_list_combinations():
	assert(list([1,2,3].combinations(2)) == [(1, 2), (1, 3), (2, 3)])

def test_list_permutations():
	assert(list([1,2,3].permutations()) == [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)])

def test_list_reversed():
	assert([1,2,3].reversed() == [3,2,1])

def test_list_collect():
	assert([1,2,3].collect(lambda x:x%2) == {0: [2], 1: [1, 3]})

def test_list_match():
	# types
	r = []
	i = []
	["foo", 42, 57.1].match({int: i.append, basestring: r.append})
	assert(r == ["foo"])
	assert(i == [42])
	# classes
	class F:
		pass
	r = []
	f = F()
	["foo", 42, 57.1, f].match({F: r.append})
	assert(r == [f])
	# functions
	r = []
	def isthree(n):
		return n==3
	[1,2,3,4,5].match({isthree: r.append})
	assert(r == [3])
	# exhaustive warnings
	r = []
	try:
		[1,3].match({isthree: r.append}, exhaustive=True)
		assert False, "Didn't throw exhaustive runtime error"
	except ValueError as e:
		assert(e.message == "Unable to match item 1")


