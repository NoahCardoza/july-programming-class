import requests
import json
import time
from math import floor


# press ctrl-c to quit

# get your token at http://51.38.128.213:3000/
token = ''

percentageThreshold = 5 / 100 # 5%
lastSellPrice = 0
lastPurchasePrice = 0

s = requests.Session()
s.headers.update({
    'authorization': 'Bearer ' + token
})

def url(path):
    return 'http://51.38.128.213:3000' + path

def getPrice():
    return s.get(url('/price')).json()['value']

def getBalance():
    return s.get(url('/balance')).json()['value']

def getBtc():
    return s.get(url('/btc')).json()['value']

def buyBtc(amount):
    return s.get(url('/buy'), params={
        'amount': amount
    })

def sellBtc(amount):
    return s.get(url('/sell'), params={
        'amount': amount
    })

balance = getBalance()
btc = getBtc()

print ('Balance:', balance)
print ('BTC:', btc)

if btc:
    lastSellPrice = getPrice()
    sellBtc(btc)
    print ('Selling your inital {} BTC for ${}.'.format(btc, btc * lastSellPrice))
    balance += btc * lastSellPrice
    btc = 0

while True:
    price = getPrice()
    if not btc: # time to buy btc
        btcToBuy = balance / price
        cost = balance
        if lastSellPrice:
            print ('Could buy at a gain of {}%'.format(round(100 - (price / lastSellPrice * 100), 2)))
        if not lastSellPrice or price * (1 + percentageThreshold) < lastSellPrice:
            if buyBtc(btcToBuy).status_code == 200:
                if lastSellPrice:
                    print ('Bought {amount} BTC for {cost} at {price} per BTC. Bought for {percentage}% than it was sold for.'.format(
                        amount=btcToBuy,
                        cost=cost,
                        price=price,
                        percentage=round(100 - (price / lastSellPrice * 100), 2)
                    ))
                else:
                    print ('Made first purchase of {amount} BTC for {cost} at {price} per BTC.'.format(
                        amount=btcToBuy,
                        cost=cost,
                        price=price,
                    ))
                balance -= cost
                btc += btcToBuy
                lastPurchasePrice = price
            else:
                print ('Error trying to buy BTC.')
    else: # time to sell btc
        profit = btc * price
        if lastPurchasePrice:
            print ('Could sell at a gain of {}%'.format(round(100 - (lastPurchasePrice / price * 100))))
        if price * (1 - percentageThreshold) > lastPurchasePrice:
            if sellBtc(btc).status_code == 200:
                if lastPurchasePrice:
                    print ('Sold {amount} BTC for {profit} at {price} per BTC. Sold for {percentage}% more than it was purchased for.'.format(
                        amount=btc,
                        profit=profit,
                        price=price,
                        percentage=round(100 - (lastPurchasePrice / price * 100))
                    ))
                else:
                    print ('Made first sale of {amount} BTC for {profit} at {price} per BTC.'.format(
                        amount=btc,
                        profit=profit,
                        price=price
                    ))
                balance += profit
                btc = 0
                lastSellPrice = price
            else:
                print ('Error trying to sell BTC.')
    time.sleep(1)
