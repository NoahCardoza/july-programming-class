#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string as String
from random import randint
import sys
import time

def ascii_animition(ascii):
    numbers = "123456789"
    for i in ascii:
        ii = randint(0 , 10)
        sys.stdout.write(start + i + "\r")

def encode(string):
    ascii_converted = []
    ascii_out = ""
    for i in string:
        if i not in String.punctuation + " ":
            index = String.ascii_letters.index(i) + shift
            ascii_chr = String.ascii_letters[index % len(String.ascii_letters)]
            fancy_append = " (" + i + "->" + ascii_chr + ") : "
            ascii_out += ascii_animition(ascii_out + fancy_append, ord(ascii_chr)) + " "
            ascii_converted.append(ascii_chr)
        else:
            ascii_converted.append(i)
    print (ascii_out + " " * len(fancy_append))
    return "".join(ascii_converted)

def decode(ascii_converted):
    english_converted = []
    ascii_out = ""
    for i in ascii_converted:
        if i not in String.punctuation + " ":
            index = String.ascii_letters.index(i) - shift
            ascii_chr = String.ascii_letters[index % len(String.ascii_letters)]
            fancy_append = " (" + i + "->" + ascii_chr + ") : "
            ascii_out += ascii_animition(ascii_out + fancy_append, ord(ascii_chr)) + " "
            english_converted.append(ascii_chr)
        else:
            english_converted.append(i)
    print (ascii_out + " "*len(fancy_append))
    return "".join(english_converted)

def ascii_animition(prepend, ascii):
    ascii = str(ascii)
    numbers = "123456789"
    prev_out = ""
    for i in ascii:
        if i == "0":
            prev_out += i
            continue
        while True:
            guess = numbers[randint(0 , 8)]
            sys.stdout.write(str(":"+prepend+prev_out + guess + "\r"))
            time.sleep(.01)
            sys.stdout.flush()
            if guess == i:
                prev_out += i
                break
    return prev_out

print ("Wellcome to the Seizure Cipher. \nWith this ground breaking technology anyone without a key to your message will be struck with a mind blowing seizure! \nWhat is your shift?")
while True:
    try:
        shift = int(input(">>> "))
    except NameError as e:
        print ("Wow! Numbers please!")
    else:
        break

print ("Would you like to encode (1), decode (2), or exit (3)?")
while True:
    try:
        c = int(input(">>> "))
        if c == 1:
            print ("What is your plain text?")
            t = input(">>> ")
            print (encode(t))
        elif c == 2:
            print ("What is your encoded text?")
            t = input(">>> ")
            print (decode(t))
        elif c == 3:
            print ("Good Bye.")
            print ("© 2016 Galac-tech, Studios")
            break
    except ValueError:
        print ("Wow! Numbers please!")
