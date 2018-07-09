# Modules:
Since we are going to create a BTC trading bot, we are going to need to make web requests. For that we will be using the `requests` module.

## Installing
While there are a few ways to install a module, I find the easiest method is using `pip`.

To start, open up a Terminal (Mac) or Command Prompt (Windows):
```bash
pip -V    # pip 7.1.2 from /Library/Python/2.7/site-packages (python 2.7)
pip3 -V   # pip 10.0.1 from /usr/local/lib/python3.6/site-packages/pip (python 3.6)
```
Depending on how Python was installed the output above could be different. Use whichever command returns `(python 3.6)`.
```
pip3 install --user requests
```
## Importing
Have you ever heard the saying:
>  Don't reinvent the wheel.

That is exactly why we use modules. No need to recreate a whole army of functions that work near perfectly to make and seed HTTP requests when we could just `pip3 install requests`... This way we can spend more time on our own project.

Using an installed module is as easy as:
```py
import requests
```
Done.
## Using
Here is the [docs page](http://docs.python-requests.org/en/master/) for the module.

Here are a few of the methods:
```py
requests.get(...)
requests.post(...)
requests.put(...)
requests.delete(...)
####################
requests.Session()
```
## Importing Your Own Files
This is really helpful when managing big projects. It is really hard to find a certain line of code in 1k+ lines of code.

It is a much better practice to section off your code into smaller files with meaningful names.

`/config.py`
```py
name = 'Noah'
age = 17
pythonIsGreat = True
```

`/main.py`
```py
import config
print ('My name is {}. I am {} years old.'.format(config.name, config.age))
if config.pythonIsGreat:
  print ('Python is great!')
else:
  print ('Python is pretty great.')
```
