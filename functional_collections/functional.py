from forbiddenfruit import curses
from itertools import chain, groupby, permutations, combinations
from functools import reduce
import random
import types
import six

class Option(object):
    @staticmethod
    def empty():
        return Option(None)

    def __init__(self, x):
        self.value = x

    def map(self, fn):
        if self.value != None:
            return Option(fn(self.value))
        else:
            return Option(None)

    def isEmpty(self):
        return self.value == None

    def isDefined(self):
        return self.value != None

    def getOrElse(self, f):
        if self.value != None:
            return self.value
        else:
            return f

    def flatten(self):
        assert(isinstance(self.value, Option))
        return self.value

    def flatMap(self, fn):
        return self.map(fn).flatten()

    def filter(self, fn):
        if self.value == None:
            return Option(None)
        else:
            if fn(self.value):
                return self
            else:
                return Option(None)

    def __str__(self):
        return self.map(lambda x:"Some("+str(x)+")").getOrElse("None")

    def __repr__(self):
        return self.map(lambda x:"Some("+x.__repr__()+")").getOrElse("None")

@curses(object, "wrapOption")
def wrapOption(self):
    return Option(self)

@curses(object, "pipe")
def thrush(self, fn):
    return fn(self)

@curses(object, "tap")
def tap(self, fn):
    fn(self)
    return self

@curses(list, "map")
def listmap(self, fn):
    """
    postfix map method, allows you to call map on a list
    :param fn: transform to apply to the list
    :return: new list with the transform applied
    """
    return list(map(fn, self))

@curses(list, "filter")
def listfilter(self, fn):
    """
    postfix filter method, allows you to call filter on a list
    :param fn: filter to apply to the list
    :return: new list with the filter applied
    """
    return list(filter(fn, self))

@curses(list, "filterNot")
def listfilternot(self, fn):
    """
    postfix filter method with a negation, allows you to call the inverse of a filter on a list
    :param fn: inverse filter to apply to the list
    :return: new list with the inverse filter applied
    """
    return list(filter(lambda x: not fn(x), self))

@curses(list, "reduce")
def listreduce(self, fn):
    """
    postfix reduce method, allows you to call reduce on a list
    :param fn: function to reduce the list by
    :return: result of the reduction method being called along the list
    """
    return reduce(fn, self)

@curses(list, "zip")
def listzip(self, *args):
    """
    postfix zip method, allows you to call zip on a list
    :param args: iterable to zip onto the list zip is being called on
    :return: result of zipping the two iterables
    """
    return list(zip(self, *args))

@curses(list, "flatten")
def listflatten(self):
    """
    postfix flatten method, flattens the list by 1 depth
    :return: the list with sublists flattened into the top level list
    """
    return list(chain.from_iterable(self))

@curses(list, "mkString")
@curses(list, "join")
def listjoin(self, string=""):
    """
    allows you to join the list by transforming all items into strings and interlacing them with the argument
    :param string: string to be inserted between each item
    :return: a string representing the list with an optional string inserted between each item
    """
    return string.join(self.map(str))

@curses(list, "toDict")
def listodict(self):
    """
    transforms this list into a dictionary, expects it to be of the form [[k,v],[k,v]...]
    :return: dictionary created from this list
    """
    return dict(self)

@curses(list, "len")
@curses(list, "length")
@curses(list, "size")
def listsize(self):
    """
    measures the length of this list
    :return: int, length of list
    """
    return len(self)

@curses(list, "enumerate")
def listenumerate(self):
    """
    enumerate the list, zipping it with range(0,len(self))
    :return: enumerated list
    """
    return enumerate(self)

@curses(list, "iter")
@curses(list, "iterate")
def listiter(self):
    """
    create iterator to iterate over list
    :return: iterator
    """
    return iter(self)

@curses(list, "max")
def listmax(self, *a, **kw):
    """
    Passthrough to max builtin
    """
    return max(self, *a, **kw)

@curses(list, "min")
def listmin(self, *a, **kw):
    """
    Passthrough to min builtin
    """
    return min(self, *a, **kw)

@curses(list, "toSet")
def listtoset(self):
    """
    transforms list into set, same as calling set(mylist)
    :return: set
    """
    return set(self)

@curses(list, "sorted")
def listsorted(self, *args, **kwargs):
    """
    Passthrough to sorted builtin, used for sorting
    """
    return sorted(self, *args, **kwargs)

@curses(list, "sum")
def listsum(self, *args):
    """
    Passthrough to sum builtin, used to add together lists
    """
    return sum(self, *args)

@curses(list, "toTuple")
def listtotuple(self):
    """
    Transform list to tuple (fixed-length list)
    :return: tuple representation of list
    """
    return tuple(self)

@curses(list, "distinct")
def listdistinct(self):
    """
    Find all distinct items in list
    :return: list containing all distinct items from original list
    """
    return list(self.toSet())

@curses(list, "find")
def listfind(self, fn):
    """
    Find the first item in the list that matches the function
    :param fn: function to test list with
    :return: first item found that matches fn, or None
    """
    for item in self:
        if fn(item):
            return item
    return None

@curses(list, "exists")
def listexists(self, fn):
    """
    See if an item in this list matches the supplied function
    :param fn: function to test list with
    :return: bool, whether a match was found
    """
    for item in self:
        if fn(item):
            return True
    return False

@curses(list, "flatMap")
def listflatmap(self, fn):
    """
    Perform 1 level of flattening on the list, then transform it with the supplied function
    :param fn: function to transform flattened list with
    :return: transformed flattened list
    """
    return self.flatten().map(fn)

@curses(list, "fold")
@curses(list, "foldRight")
def listfold(self, initial):
    """
    fold the list, this generates a partial function with the initial value and data loaded
    :param initial: initial value to fold from
    :return: partial function that expects the fold function
    """
    def innerfold(fn):
        """
        partial function containing an initial fold value and data to fold over
        :param fn: function to apply the fold with
        :return: the result of applying the fold across the data, using the initial value
        """
        return reduce(fn, self, initial)
    return innerfold

@curses(list, "foldLeft")
def listfoldleft(self, initial):
    """
    fold the list backwards, this generates a partial function with the initial value and data loaded
    :param initial: initial value to fold from
    :return: partial function that expects the fold function
    """
    def innerfold(fn):
        """
        partial function containing an initial fold value and data to fold over backwards
        :param fn: function to apply the fold with
        :return: the result of applying the fold across the data backwards, using the initial value
        """
        return reduce(fn, self.reversed(), initial)
    return innerfold

@curses(list, "forAll")
@curses(list, "forall")
def listforall(self, fn):
    """
    Test whether every item in the list meets a condition
    :param fn: condition to test the list with
    :return: bool, whether every item in the list matched the function
    """
    for item in self:
        if not fn(item):
            return False
    return True

@curses(list, "groupBy")
def listgroupby(self, *args):
    """
    Actually have no idea what this does, yet
    :param args:
    :return:
    """
    return groupby(self, *args)

@curses(list, "grouped")
def listgrouped(self, l):
    """
    Gather the list into l-sized chunks
    :param l: size of each chunk
    :return: iterator which will output l-sized chunks from the list
    """
    for i in range(0, len(self), l):
        v = self[i:i+l]
        if len(v) == l:
            yield v

@curses(list, "intersect")
def listintersect(self, t):
    """
    Output a set of the items contained in the calling list and the target list
    :param t: target iterable to find the intersection with
    :return: set of items contained in self and target
    """
    return set(self) & set(t)

@curses(list, "empty")
def listempty(self):
    """
    Ask whether the list is empty
    :return: bool, whether list is empty
    """
    return len(self)==0

@curses(list, "nonEmpty")
def listempty(self):
    """
    Ask whether the list is nonEmpty
    :return: bool, whether the list is nonEmpty
    """
    return not len(self)==0

@curses(list, "combinations")
def listcombinations(self, l):
    """
    Return all combinations of items in list that are l-length
    :param l: length of combinations
    :return: all combinations of items in list that are l-length
    """
    return combinations(self, l)

@curses(list, "permutations")
def listpermutations(self, *a):
    """
    Calculate every permutation of the list
    :return: all permutations of items in list
    """
    return permutations(self, *a)

@curses(list, "reversed")
def listreversed(self):
    """
    :return: copy of the current list that has been reversed
    """
    return self[::-1]

@curses(list, "shuffle")
def listshuffle(self):
    """
    :return: copy of the current list that has been shuffled
    """
    n = list(self)
    random.shuffle(n)
    return n

from collections import defaultdict

@curses(list, "collect")
def listcollect(self, fn):
    """
    Collect items in this list into multiple lists based on the supplied key function
    :param fn: key function used to classify items
    :return: dict of key->list, where all items in the current list have been sorted into the new lists based on key
    """
    r = defaultdict(list)
    for item in self:
        r[fn(item)].append(item)
    return r

@curses(list, "match")
def listmatch(self, d, default=None, exhaustive=False):
    """
    Perform a pattern match on the list, running different code for each match type
    :param d: dict describing how to run the match, keys can be:
            type: item is checked against this type
            class: item is checked to see if it's an instance of this class
            function: item is checked to see if this function returns True
        If a key shows an item as a match, the associated function in it's value is run with the item as it's argument
    :param default: function to feed all non-matching items to
    :param exhaustive: toggles a default-default that will throw an exception if an item is not matched
    :return: None

    Example:
        >>> numbers = []
        >>> text = []
        >>> [42, "12"].match{int: numbers.append, basestring: text.append}
        >>> numbers
        [42]
        >>> text
        ["12"]

        In this example a match is done based on type, it sorts the list into two new lists based on type
    """
    if default == None:
        if exhaustive:
            def exhaustive_failure(item):
                raise ValueError("Unable to match item %s" % item)
            default = exhaustive_failure
        else:
            default = lambda x:x
    for item in self:
        for k,v in d.items():
            # raw types
            if isinstance(k, type) and isinstance(item, k):
                v(item)
            # classes
            elif isinstance(k, six.class_types) and isinstance(item, k):
                v(item)
            # functions
            elif isinstance(k, types.FunctionType) and k(item):
                v(item)
            # default
            else:
                default(item)


@curses(types.GeneratorType, "toList")
def generatortolist(self):
    """
    Adds a toList function to all generators that turns them into lists (generally a bad idea)
    :returns: List containing all items that came out of the generator
    """
    return list(self)
