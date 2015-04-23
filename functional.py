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

@curses(list, "mkString")
@curses(list, "join")
def listjoin(self, string=None):
    if string == None:
        return "".join(self.map(str))
    else:
        return string.join(self.map(str))


    return string.join(self)
