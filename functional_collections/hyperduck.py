__author__ = 'andi'

# Have you ever looked at python's type model and wished it had even more duck?
# introducing hyperduck, a registry for duck transform functions that can automatically transform objects
# this emulates scala implicit conversions by using decorators to duct tape a type system and implicit modifier on top of python

from collections import namedtuple, defaultdict

HyperduckStats = namedtuple("HyperduckStats", ["transformed", "failed", "passthrough"])

global hyperduckstorage
hyperduckstorage = {} # map of (in, out) -> function(in) -> out
global hyperduckstats
hyperduckstats = defaultdict(lambda: HyperduckStats(0,0,0))
global hyperduck_function_mapper
hyperduck_function_mapper = {}

def _inc(key, stat, inc):
	hyperduckstats[key] = hyperduckstats[key]._replace(**{stat: hyperduckstats[key]._asdict().get(stat)+inc})

def implicit(intype, outtype):
	def innerimplicit(fn):
		# register the hyperduck transform in hyperduck storage
		hyperduckstorage[(intype, outtype)] = fn
		# return so it can be decorated further or stored somewhere
		return fn
	return innerimplicit

def applyhyperducktransform(fn, input, wanted_type):
	lookuptuple = (type(input), wanted_type)
	# TODO add chain resolution here perhaps
	if lookuptuple in hyperduckstorage:
		_inc(fn, "transformed", 1)
		return hyperduckstorage[lookuptuple](input)
	else:
		_inc(fn, "failed", 1)
		return input


# simple implementation for one-argument functions
def takes(intype):
	def innertakes(fn):
		def wrappedfn(arg):
			if not isinstance(arg, intype):
				return fn(applyhyperducktransform(fn, arg, intype))
			else:
				_inc(fn, "passthrough", 1)
				return fn(arg)
		hyperduck_function_mapper[wrappedfn] = fn
		return wrappedfn
	return innertakes

def get_hyperduck_stats(fn):
	return hyperduckstats[hyperduck_function_mapper[fn]]