# A more advanced bot.
# This cannot be uploaded to the server as is.
# This is a demonstration of how you might test your code before you upload it.

import re # RegEx -> Regular Expressions
# Check out: https://regexr.com/

me = 'a'

def getMyPos(b):
    clean = '' # create a new string
    for c in b: # loop through each character
        # if the character is not someone's health (a number) and it is either a
        # tile (an upper case character) or us (our lower case 'a')
        if not c.isnumeric() and (c.isupper() or c == me):
            clean += c # append it to the end of our string
    # clean == 'DDDDDDDDBBBBBBBBBBBBBBBBBBBBBBBBBBBBAACAACACAaACCCCCCCCCCXXXXBDDD'
    # Next: we get the position of our player and subtract one since he comes
    # after the tile he is on.
    return clean.index(me) - 1

def getMyHealth(board):
    # create an expression: look for an 'a' followed by numbers [0-9]
    search = re.search(me + r'(\d+)', board)
    if search: # if we found a match
        # group(1) gets us all the characters matched inside the (\d+) of the
        # expression
        return int(search.group(1))
    else:
        return 0

def run(board):
    health = getMyHealth(board)
    print(getMyPos(board))

# manualy passing the board so we can easily test without having to run the code 
# on the server
print(run('De50DDDDDd355DDBBBBBBBBBBBBBBBBBBBBBBBb189BBBBBAACAACc77ACAa78ACCCCCCCCCCXXXXBDDD'))
