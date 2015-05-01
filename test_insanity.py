__author__ = 'andi'

from functional_collections import *

def test_hyperduck_insanity():
	"""This test uses:
		* caseclass to create type-checked immutable tuples to store our data in
		* functional collections to build the animals
		* hyperduck to duck-type Dogs as Ducks during the map
	"""
	# Define our data storage classes
	Dog = caseclass("Dog", [("name", str), ("age", int)])
	Duck = caseclass("Duck", [("name", str), ("age", int), ("eggs", bool)])

	# register an implicit converter for Dog->Duck
	@implicit(Dog, Duck)
	def dog2duck(d):
		# Dogs wearing Duck costumes cannot lay eggs, but they can be checked for eggs
		return Duck(d.name, d.age, False)

	# write a function that checks ducks for eggs
	@takes(Duck)
	def check_for_eggs(duck):
		return duck.eggs

	# construct our dogs and ducks
	dogs = [("Matthew", 7), ("Barry", 4), ("Ted", 2)].map(Dog._make)
	ducks = [("Gertrude", 3, True), ("Matilda", 2, True)].map(Duck._make)

	# mix the dogs and ducks together
	dogs_and_ducks = (dogs + ducks).shuffle()

	# check them all for eggs, automatically casting the Dogs into ducks
	eggresults = dogs_and_ducks.map(check_for_eggs)

	# ensure our stats are correct
	stats = get_hyperduck_stats(check_for_eggs)
	assert(stats.transformed == 3)
	assert(stats.passthrough == 2)

	# try to implicitly convert all Dogs into Ducks using a lambda
	converted_ducks = dogs_and_ducks.map(takes(Duck)(lambda x:x))
	assert(converted_ducks.forAll(lambda x: isinstance(x, Duck)))


if __name__ == "__main__":
	test_hyperduck_insanity()