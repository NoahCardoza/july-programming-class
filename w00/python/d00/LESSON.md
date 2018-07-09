# Data Types:
These are all of the basic types of data you will deal with in Python.
## Integers

> A whole number; a number that is not a fraction.

```py
int()           #
1 + 1           # 2
8 - 1           # 7
10 * 2          # 20
35 / 5          # 7.0
10 / 3          # 3.33333
5 // 3          # 1
7 % 3           # 1
2**3            # 8
5 + '5'         # TypeError
str(5) + '5'    # '55'
type(1)         # <class 'int'>
```
## Floats (decimals)

Any decimal number.

```py
float()         #
5.4 + 3         #  8.3
type(.1)        #  <class 'float'>
x = 0.5 + 0.5   #
x               #  1.0
type(x)         #  <class 'float'>
x == 1          #  True
x is 1          #  False
int(x) == 1     #  True
```

## Lists

An indexed collection of items.

```py
list()          #
a = [1, 2, 3]   #
b = [4]         #
b.append(5)     #
b               # [4, 5]
c = b + 6       # TypeError
c = b + [6]     #
b               # [4, 5]
c               # [4, 5, 6]
a + c           # [1, 2, 3, 4, 5, 6]
a.extend(c)     #
a               # [1, 2, 3, 4, 5, 6]
c               # [4, 5, 6]
len(a)          # 6
a.pop()         # 6
a.pop(0)        # 1
a               # [2, 3, 4, 5]
a[0]            # 2
a[-1]           # 5
a[1:]           # [3, 4, 5]
a[1:3]          # [3, 4]
```
## Strings

Basically a list of charters with a few extra methods.

```py

'Hello World!'                # 'Hello World!'
's' + 'h' * 20 + '!'          # 'shhhhhhhhhhhhhhhhhhhh!'
s = """
This
is
a
multiline
String!"""                    # 'This\nis\na\nmultiline\nstring!\n'
print(s)                      #
type(s)                       # <type 'str'>
x = 42                        #
type(x)                       # <type 'int'>
type(str(x))                  # <type 'str'>
```
## Dictionaries

A collection of key, value pairs.

```py
dict()                                #
person = {'name': 'Noah', 'age': 17}  #
person['name']                        # 'Noah'
person['age']                         # 17
```

## Booleans (True/False)

```py
True                      # True
False                     # False
bool(42)                  # True
bool(0)                   # False
bool("string")            # True
bool("")                  # False
bool((1, 2, 3))           # True
bool(())                  # False
bool([1, 2, 3])           # True
bool([1, 2, 3])           # False
bool({ 'name': 'Noah' })  # True
bool({})                  # False
```

# Loops:

Loops are one of your most powerful tools. Much of programming is based on loops, doing repetitive tasks one after the other.

## While

The most basic loop.

```py
while condition:
  pass
```
Example:
```py
x = 10
while x > 0:
  print(x)
  x -= 1
# 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```
### For

A special type of loop that passes each item of an iterable to the block of code defined with in it.

```py
for value in iterable:
  pass
```
Examples:
```py
x = [3, 4, 5]
for i in x:
  print(i)
# 3, 4, 5
```
Using `range()`
```py
for i in range(3):
  print(i)
# 0, 1, 2
```
Inline For Loop:
```py
[(x, x * 2) for x in range(1, 11)]
# [(1, 2), (2, 4), (3, 6), (4, 8), (5, 10), (6, 12), (7, 14), (8, 16), (9, 18), (10, 20)]
```
