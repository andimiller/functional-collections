# Functional Python Utilities

## Functional Collection Extensions

*TL;DR: this library lets you write transforms left to right in stead of wrapping stuff in brackets and writing right to left*

These take the form of extensions to the base python types, the general idea behind these is to emulate the scala collections library to give an Object Oriented yet composable interface.

You get all the basic building blocks to help you express monadic transforms in python in a sensible way:

### So which wrappers does this even include?

* transforms: map, flatMap
* filters: filter, filterNot, distinct, intersect
* ordering tools: sorted, reversed, shuffle
* reducers: reduce, fold, foldLeft, foldRight, join, mkString, forAll, sum, find, exists, min, max
* shaping tools: zip, flatten, groupBy, grouped, collect, enumerate, combinations, permutations, collect, match
* utilities: empty, nonEmpty, toSet, toDict, toTuple, iter

### Why would you do this?

I got fed up of wrapping everything in brackets and writing right-to-left code, after coding a lot of scala for work it became more and more painful to come back to python and not be able to compose my code nicely.

I do not recommend doing any of the things this library does in a production environment, nor do I consider any of it good practice, I just felt like doing it.

### Well give me some examples then

### Basic Example: Multiply some numbers by 2

#### Classic Python

```python
>>> map(lambda x:x*2, range(1,10))
[2, 4, 6, 8, 10, 12, 14, 16, 18]
```

#### Functional Python

```python
>>> range(1,10).map(lambda x:x*2)
[2, 4, 6, 8, 10, 12, 14, 16, 18]
```

### Intermediate Example: Full filter/map/reduce

Range from 0 to 10, filter on even numbers, multiply by 3, add together with reduce

#### Classic Python

```python
>>> reduce(lambda x,y: x+y, map(lambda x:x*3, filter(lambda x:x%2==0, range(0,10))))
60
```

#### Functional Python

```python
>>> range(0,10).filter(lambda x:x%2==0).map(lambda x:x*3).reduce(lambda x,y:x+y)
60
```

### Expert Example: stupidly long pipeline with a lot of transforms

Take the numbers 1 to 100, filter on multiples of 7, multiply by 42, shuffle, group into sets of 2, sum the sublists, remove duplicates, sort, fold into a string


#### Classic Python
```python
>>> r = map(lambda x:x*42, filter(lambda x:x%7==0, range(0,100)))
>>> random.shuffle(r)
>>> reduce(lambda acc,x: acc+str(x), sorted(set(map(lambda x:x[0]+x[1], zip(r[::2], r[1::2])))), "")
'5884116441052926762'
```

#### Functional Python
```python
>>> range(0,100)\
...     .filter(lambda x:x%7==0)\
...     .map(lambda x:x*42)\
...     .shuffle()\
...     .grouped(2)\
...     .toList()\
...     .map(lambda x:x[0]+x[1])\
...     .distinct()\
...     .sorted()\
...     .fold("")(lambda acc,x: acc+str(x))
'14702352470452926174'
```

## Okay I can get behind the left-to-right composition stuff, but what do I store my data in? classes?

Introducing caseclass, my extension of the python namedtuple to add typesafety and a couple of extra features.

It's (kind of) type-safe, (mostly) immutable, and (sometimes) easy to work with!

### Typical Data Record Code

#### Classic Python
```python
>>> class Cat:
...     name = None
...     age = None
...     def __init__(self, name, age):
...             assert(isinstance(name, basestring))
...             assert(isinstance(age, int))
...             self.name = name
...             self.age = age
...
```

#### Functional Python
```python
>>> Cat = caseclass("Cat", [("name", basestring), ("age", int)])
```

### Boy that sure looks like a lot less code, what else does it do?

#### acts like a tuple and object at the same time!

```python
>>> bob = Cat("Bob", 8)
>>> bob.age
8
>>> bob[1]
8
```

#### nice strings if you print them!

`Cat(name='Terry', age=7)` vs `<__main__.Cat instance at 0x101012170>`

#### free hash function and comparisons!

```python
>>> Cat("Terry", 7) == Cat("Terry", 7)
True
```

#### transform lists of tuples/dicts into objects with minimum hastle!

```python
>>> [("Terry", 7), ("Bob", 5), ("Marge", 2)].map(Cat._make)
[Cat(name='Terry', age=7), Cat(name='Bob', age=5), Cat(name='Marge', age=2)]
```

#### immutable copy function!

```python
>>> bob = Cat("Bob", 7)
>>> # oh no, bob is 8, not 7!
>>> bob = bob.copy(age=8)
>>> bob
Cat(name='Bob', age=8)
```

#### transform objects back into tuples/dicts for ease of use!

```python
>>> [("Terry", 7), ("Bob", 5), ("Marge", 2)].map(Cat._make).sorted(key=lambda x:x.age).map(tuple)
[('Marge', 2), ('Bob', 5), ('Terry', 7)]
```

## Combinators

This now includes implementations of the T (Thrush) and K (Kestrel) combinators, which patch themselves onto all objects, allowing you to use `pipe` and `tap` on any object

Note: you will need to wrap integers in brackets if you're starting off on a literal integer, because `2.` is a valid float in python for some reason!

```python
>>> (2).pipe(lambda x:x*2).tap(print).pipe(lambda x:x*2)
4
8
```

## Hyperduck

*If I can find a way to make it quack then it's a duck*

This module allows you to register implicit type conversions and automatically cast all arguments to a function to match a desired function signature.

```python
>>> Dog = caseclass("Dog", [("name", str), ("age", int)])
>>> @implicit(Dog, int)
... def dog2int(d):
...     return d.age
...
>>> @takes(int)
... def multiply_int_by_2(i):
...     return i*2
...
>>> multiply_int_by_2(Dog("Matthew", 13))
26
>>> get_hyperduck_stats(multiply_int_by_2)
HyperduckStats(transformed=1, failed=0, passthrough=0)
```
