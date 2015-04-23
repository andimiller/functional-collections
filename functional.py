from forbiddenfruit import curses
from itertools import chain

@curses(list, "map")
def listmap(self, func):
    return map(func, self)

@curses(list, "filter")
def listfilter(self, func):
    return filter(func, self)

@curses(list, "reduce")
def listreduce(self, func):
    return reduce(func, self)

@curses(list, "zip")
def listzip(self, other):
    return zip(self, other)

@curses(list, "flatten")
def listflatten(self):
    return list(chain.from_iterable(self))

@curses(list, "join")
def listjoin(self, string):
    return string.join(self)
