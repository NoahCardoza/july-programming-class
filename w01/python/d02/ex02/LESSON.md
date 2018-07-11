# Exercise 2: Lesson

## Things you will need to know:

### Another way to `repeat` a block of code:
The `for` loop.

There are two ways to end a while loop
1. When the condition equals `True`:
    ```py
    for x in [1, 2, 3]:
      print (x)

    print ("END LOOP")
    ```
2.  Or by `break`ing the loop:
    ```py
    for x in [1, 2, 3]:
      if x == 2:
        break
      print (x)

    print ("END LOOP")
    ```

### The `range` function:

The `range` function creates lists and is usually used in `for` loops:
```py
list(range(10))       # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
len(range(10))        # 10
list(range(2, 5))     # [2, 3, 4]
list(range(0, 10, 2)) # [0, 2, 4, 6, 8]
```
