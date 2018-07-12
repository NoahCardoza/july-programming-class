from string import ascii_letters, punctuation

ascii_letters_len = len(ascii_letters)
unshiftable = punctuation + " "

def encode(s):
    ascii_converted = []
    for c in s:
        if c not in unshiftable:
            index = ascii_letters.index(c) + shift
            ascii_chr = ascii_letters[index % ascii_letters_len]
            ascii_converted.append(ascii_chr)
        else:
            ascii_converted.append(c)
    return "".join(ascii_converted)

def decode(s):
    english_converted = []
    for c in s:
        if c not in unshiftable:
            index = ascii_letters.index(c) - shift
            ascii_chr = ascii_letters[index % ascii_letters_len]
            english_converted.append(ascii_chr)
        else:
            english_converted.append(c)
    return "".join(english_converted)

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
            break
    except ValueError:
        print ("Wow! Numbers please!")
