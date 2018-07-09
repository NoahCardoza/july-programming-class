# Extra

This is kinda weird and I didn't want to confuse anyone but, have fun:

```py
class MyClass:
  x = 5

MyClass.x       # 5
# Create a new instance
i = MyClass()
i.x             # 5
MyClass.x = 10
i.x             # 10
i.x = 0
MyClass.x       # 10
```
