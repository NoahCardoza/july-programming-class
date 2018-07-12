# Exercise 2: Lesson

## Things you will need to know:

### Using ascii:

```py
ord('A') # 65
ord('B') # 66
ord('C') # 67
chr(97)  # 'a'
chr(98)  # 'b'
chr(99)  # 'c'
```

### The `string` module:

```py
from string import ascii_letters, punctuation
print (ascii_letters) # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print (punctuation)   # '!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'

# NOTE: punctuation + ' '
```

### Getting the `len`gth of a `list`, `str`, `dict`, or `tuple`:

```py
len([1, 2, 3])          # 3
len("bobby")            # 5
len({ 'key': 'value' }) # 1
len((1, 2, 3))          # 3
```

### Getting the `index` of an item in a list:

```py
x = [1, 2, 3, 4, 5] #
x.index(1)          # 0
x.index(5)          # 4
y = 'abcdef'        #
y.index('c')        # 2
```

### Wrapping a list using the `modulo` operator (`%`) index:

```py
mylist = list(range(3)) # First lets make a list.   => [0, 1, 2]
mylistlen = len(mylist) # Next lets get the length. => 3
mylistlen               # 3
mylist[0]               # 0
mylist[1]               # 1
mylist[0 % mylistlen]   # 0
mylist[1 % mylistlen]   # 1
3 % mylistlen           # 0
mylist[3 % mylistlen]   # 0
```
