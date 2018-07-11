# Exercise 1: Lesson

## Things you will need to know:

### How to `repeat` a block of code:
The `while` statement.

There are two ways to end a while loop
1. When the condition equals `True`:
    ```py
    counter = 0
    while (counter < 10):
      print (counter)
      counter += 1
    ```
2.  Or by `break`ing the loop:
    ```py
    counter = 0
    while True:
      if (counter < 10):
        print (counter)
      else:
        break
      counter += 1
    ```

### Generating random numbers:

First we will need to `import` a module. Using an installed module is as easy as:
```py
import random
```
Done.

Next we need to get a random number:
```py
import random
random.randint(0, 10) # could be any int x where 0 <= x <= 10
```

### How to `round` a `Float`:

The function is literally named `round`.
```py
import math
round(math.pi, 2) # 3.14
```

### The `in` operator:

The `in` is operator used quite a bit but it is mostly used to check if an item exists in a list.

```py
1 in [1, 2, 3]                  # True
9 in [1, 2, 3]                  # False
"shel" in "bookshelf"           # True
"boat" in "bookshelf"           # False
"keyName" in { 'keyName': 42 }  # True
42 in { 'keyName': 42 }         # False
```

## Note:

If any of that loop stuff is till a little confusing, check out [Python Tutor's Visualizer](http://www.pythontutor.com/visualize.html#mode=edit)
