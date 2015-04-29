__author__ = 'andi'

from functional_collections import *

if __name__ == "__main__":
	Cat = caseclass("Cat", [
		("name", basestring),
		("age", int),
		("height", float),
		("length", float),
		("width", float)
	])
	cats = [Cat("Terry",
				3,
				22.5, 35.2, 15.7),
			Cat("Bob",
				6,
				21.7, 34.1, 14.6),
			Cat("Marge",
				9,
				25.5, 33.7, 18.6)]
	# extract names
	names = cats.map(lambda c: c.name)
	print names
	# sort by age
	sorted_cats = cats.sorted(key = lambda c: c.age)
	print cats
	# calculate volumes
	volumes = cats.map(lambda c: c.height * c.length * c.width)
	print volumes
	# calculate cumulative volume
	volume = cats.fold(0)(lambda a,c: a+(c.height * c.length * c.width))
	print volume

