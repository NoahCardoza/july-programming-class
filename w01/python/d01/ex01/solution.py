import random

go_again = 1
wins = 0
losses = 0
total = 0

print ('This is a game of heads vs tails. May the luckiest man (or machine) win!')

while go_again:
    user_choice = int(input('Choose heads (1), tails (2): '))
    if user_choice in [1, 2]:
        coin_flip = random.randint(1, 2)
        if coin_flip == user_choice:
            print ('You won!')
            wins += 1
        else:
            print ('You lost!')
            losses += 1
        total += 1
    else:
        print ('1 or 2 Bub. This is a coin toss!')

    print ('Your record is now ' + str(wins) + ' wins and ' + str(losses) + ' losses out of ' + str(total) + '.')
    go_again = int(input('Go again (1) or exit (0): '))
    print ()

print ('You had a win rate of ' + str(round(wins / total * 100, 2)) + '%')
print ('Good game!')
