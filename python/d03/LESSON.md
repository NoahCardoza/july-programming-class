# Classes:
> Classes provide a means of bundling data and functionality together. Creating
a new class creates a new type of object, allowing new instances of that type
to be made. Each class instance can have attributes attached to it for
maintaining its state. Class instances can also have methods
(defined by its class) for modifying its state.
>
> — Python Docs

## IRL Example: [`requests.Session`](http://docs.python-requests.org/en/master/user/advanced/)

We didn't really talk about exactly what `requests.Session` did except that it
saved us some typing. We can actually have two instances of `requests.Session`.

One of the nice things that this session keeps track of is cookies. Kind of like
your browser, but we aren't using cookies, we are using a `Bearer Token`.

## Maybe some more helpful examples:

```py
class Person:
  type = 'human'
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def birthday(self):
    self.age += 1

people = [
  Person('Noah', 17),
  Person('Ethan', 14),
  Person('Christopher', 15),
  Person('Nicholas', 14),
  Person('Aishah', 14),
  Person('Tyler', 13),
  Person('Anthony', 11)
]

for p in people:
  p.birthday()

[p.age for p in people]
```
