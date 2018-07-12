from string import ascii_letters, punctuation

ascii_letters_len = len(ascii_letters)
punctuation += ' '

def encode(s, shift):
    encoded = ''
    for char in s:
        if char not in punctuation:
            index = ascii_letters.index(char)
            shifted_index = index + shift
            new_char = ascii_letters[shifted_index % ascii_letters_len]
            encoded += new_char
        else:
            encoded += char
    return encoded

def decode(s, shift):
    decoded = ''
    for char in s:
        if char not in punctuation:
            index = ascii_letters.index(char)
            shifted_index = index - shift
            new_char = ascii_letters[shifted_index % ascii_letters_len]
            decoded += new_char
        else:
            decoded += char
    return decoded


print ('Welcome to the Caesar Cipher Encoder/Decoder!')
print ('What is your shift?')
shift = int(input('>>> '))

while True:
    print ('Do you want to encode (1), decode (2), or exit (0)?')
    choice = int(input('>>> '))
    if not choice:
        break
    user_string = input('>>> ')
    if choice == 1: # encode
        print (encode(user_string, shift))
    elif choice == 2: # decode
        print (decode(user_string, shift))
    else:
        print ("That's not a valid input!")

print ('Thanks for your time. Bye.')
