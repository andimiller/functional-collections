# Functional Python Utilities

## Functional Collection Extensions 

*TL;DR: this library lets you write transforms left to right in stead of wrapping stuff in brackets and writing right to left*

These take the form of extensions to the base python types, the general idea behind these is to emulate the scala collections library to give an Object Oriented yet composable interface.

You get all the basic building blocks to help you express monadic transforms in python in a sensible way:

### So which wrappers does this even include?

* transforms: map, flatMap
* filters: filter, filterNot, distinct, intersect, find, exists, min, max
* ordering tools: sorted, reversed, shuffle 
* reducers: reduce, fold, foldLeft, foldRight, join, mkString, forAll, sum
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

