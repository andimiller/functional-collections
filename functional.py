from forbiddenfruit import curses
from itertools import chain, groupby, permutations, combinations
from functools import partial

@curses(list, "map")
def listmap(self, fn):
    return map(fn, self)

@curses(list, "filter")
def listfilter(self, fn):
    return filter(fn, self)

@curses(list, "filterNot")
def listfilternot(self, fn):
    return filter(lambda x: not fn(x), self)


@curses(list, "reduce")
def listreduce(self, fn):
    return reduce(fn, self)

@curses(list, "zip")
def listzip(self, *args):
    return zip(self, *args)

@curses(list, "flatten")
def listflatten(self):
    return list(chain.from_iterable(self))

@curses(list, "mkString")
@curses(list, "join")
def listjoin(self, string=""):
    return string.join(self.map(str))

@curses(list, "toDict")
def listodict(self):
    return dict(self)

@curses(list, "len")
@curses(list, "length")
@curses(list, "size")
def listsize(self):
    return len(self)

@curses(list, "enumerate")
def listenumerate(self):
    return enumerate(self)

@curses(list, "iter")
@curses(list, "iterate")
def listiter(self):
    return iter(self)

@curses(list, "max")
def listmax(self, *a, **kw):
    return max(self, *a, **kw)

@curses(list, "min")
def listmin(self, *a, **kw):
    return min(self, *a, **kw)

@curses(list, "toSet")
def listtoset(self):
    return set(self)

@curses(list, "sorted")
def listsorted(self, *args, **kwargs):
    return sorted(self, *args, **kwargs)

@curses(list, "sum")
def listsum(self, *args):
    return sum(self, *args)

@curses(list, "toTuple")
def listtotuple(self):
    return tuple(self)

@curses(list, "toSet")
def listset(self):
    return set(self)

@curses(list, "distinct")
def listdistinct(self):
    return list(self.toSet())

@curses(list, "find")
def listfind(self, fn):
    for item in self:
        if fn(item):
            return item
    return None

@curses(list, "exists")
def listexists(self, fn):
    for item in self:
        if fn(item):
            return True
    return False

@curses(list, "flatMap")
def listflatmap(self, fn):
    return self.flatten().map(fn)

@curses(list, "fold")
@curses(list, "foldRight")
def listfold(self, initial):
    def innerfold(fn):
        return reduce(fn, self, initial)
    return innerfold

@curses(list, "forall")
def listforall(self, fn):
    for item in self:
        if not fn(item):
            return False
    return True

@curses(list, "groupBy")
def listgroupby(self, *args):
    return groupby(self, *args)

@curses(list, "grouped")
def listgrouped(self, size):
    for i in range(0, len(self), size):
        v = self[i:i+n]
        if len(v) == n:
            yield v

@curses(list, "intersect")
def listintersect(self, t):
    return set(self) & set(t)

@curses(list, "empty")
def listempty(self):
    return len(self)==0

@curses(list, "nonEmpty")
def listempty(self):
    return not len(self)==0

@curses(list, "combinations")
def listcombinations(self, l):
    return combinations(self, l)

@curses(list, "permutations")
def listpermutations(self, *a):
    return permutations(self, *a)

@curses(list, "reversed")
def listreversed(self):
    return self[::-1]
