import requests
import json
import time


# press ctrl-c to quit

# get your token at http://51.38.128.213:3000/
token = ''

percentageThreshold = 1 / 100 # 10%
lastSellProfit = 0
lastPurchaseCost = 0

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
    print(s.get(url('/buy'), params={
        'amount': amount
    }).json()['message'])

def sellBtc(amount):
    print(s.get(url('/sell'), params={
        'amount': amount
    }).json()['message'])

balance = getBalance()
btc = getBtc()

print ('Balance:', balance)
print ('BTC:', btc)

if btc:
    sellBtc(btc)
    lastSellProfit = getPrice()
    btc = 0

while True:
    price = getPrice()
    if not btc:
        btcToBuy = round(price / balance, 2)
        cost = btcToBuy * price
        if not lastSellProfit or cost * (1 + percentageThreshold) < lastSellProfit:
            buyBtc(btcToBuy)
            balance -= cost
            btc += btcToBuy
            lastPurchaseCost = cost # 5000
    else:
        profit = btc * price
        if profit * (1 - percentageThreshold) > lastPurchaseCost:
            sellBtc(btc)
            balance += profit
            btc = 0
            lastSellProfit = profit
    time.sleep(1)
