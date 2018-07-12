# print(['fewlgh-' + str(qwerty) + '-fewlgh' for qwerty in ['hello', 30, 325.875]])

import requests
import json
import time
from urllib.parse import urljoin

# class ClassName(object):
#     def __init__(self, arg):
#         super(, self).__init__()
#         self.arg = arg


# press ctrl-c to quit

# get your token at http://51.38.128.213:3000/ unless you want to make me money
token = '3f53fd3ad126c655a28b29e62cb32585'

# used to evaluate a profitable buy or sell

# looks really complicated and really might be a little more work than it's woth
# but it is more about the consept. Plus I copied most of it 😂

class SessionWithUrlBase(requests.Session):
    def __init__(self, *args, base_url=None, **kwargs):
        super(SessionWithUrlBase, self).__init__(*args, **kwargs)
        self.base_url = base_url

    def request(self, method, url, **kwargs):
        modified_url = urljoin(self.base_url, url)
        return super(SessionWithUrlBase, self).request(method, modified_url, **kwargs)


class BtcBot:
    """docstring for BtcBot."""
    def __init__(self, id, percentageThreshold, token):
        self.percentageThreshold = percentageThreshold
        self.lastSellPrice = 0
        self.lastPurchasePrice = 0

        self.id = id
        self.s = SessionWithUrlBase(base_url='http://51.38.128.213:3000')
        self.s.headers.update({'authorization': 'Bearer ' + token})

        self.balance = self.getBalance()
        self.btc = self.getBtc()

        self.log('Balance:', self.balance)
        self.log('BTC:', self.btc)

        if self.btc:
            self.lastSellPrice = self.getPrice()
            self.sellBtc(self.btc)
            print ('Selling your inital {} BTC for ${}.'.format(self.btc, self.btc * self.lastSellPrice))
            self.balance += self.btc * self.lastSellPrice
            self.btc = 0

    def log(self, *args):
        msg = ' '.join([str(a) for a in args])
        print("{}: {}".format(self.id, msg))


    def getPrice(self):
        return self.s.get('/price').json()['value']


    def getBalance(self):
        return self.s.get('/balance').json()['value']


    def getBtc(self):
        return self.s.get('/btc').json()['value']


    def buyBtc(self, amount):
        return self.s.get('/buy', params={
            'amount': amount
        })


    def sellBtc(self, amount):
        return self.s.get('/sell', params={
            'amount': amount
        })

    def connect(self):
        price = self.getPrice()
        if not self.btc: # time to buy btc
            btcToBuy = self.balance / price
            cost = self.balance
            if self.lastSellPrice:
                self.log('Could buy at a gain of {}%'.format(round(100 - (price / self.lastSellPrice * 100), 2)))
            if not self.lastSellPrice or price * (1 + self.percentageThreshold) < self.lastSellPrice:
                if self.buyBtc(btcToBuy).status_code == 200:
                    if self.lastSellPrice:
                        self.log('Bought {amount} BTC for {cost} at {price} per BTC. Bought for {percentage}% than it was sold for.'.format(
                            amount=btcToBuy,
                            cost=cost,
                            price=price,
                            percentage=round(100 - (price / self.lastSellPrice * 100), 2)
                        ))
                    else:
                        self.log('Made first purchase of {amount} BTC for {cost} at {price} per BTC.'.format(
                            amount=btcToBuy,
                            cost=cost,
                            price=price,
                        ))
                    self.balance -= cost
                    self.btc += btcToBuy
                    self.lastPurchasePrice = price
                else:
                    self.log('Error trying to buy BTC.')
        else: # time to sell btc
            profit = self.btc * price
            if self.lastPurchasePrice:
                self.log('Could sell at a gain of {}%'.format(round(100 - (self.lastPurchasePrice / price * 100))))
            if price * (1 - self.percentageThreshold) > self.lastPurchasePrice:
                if self.sellBtc(self.btc).status_code == 200:
                    if self.lastPurchasePrice:
                        self.log('Sold {amount} BTC for {profit} at {price} per BTC. Sold for {percentage}% more than it was purchased for.'.format(
                            amount=self.btc,
                            profit=profit,
                            price=price,
                            percentage=round(100 - (self.lastPurchasePrice / price * 100))
                        ))
                    else:
                        self.log('Made first sale of {amount} BTC for {profit} at {price} per BTC.'.format(
                            amount=self.btc,
                            profit=profit,
                            price=price
                        ))
                    self.balance += profit
                    self.btc = 0
                    self.lastSellPrice = price
                else:
                    self.log('Error trying to sell BTC.')

botList = [
    # BtcBot('BOT 1', 10 / 100, '3f53fd3ad126c655a28b29e62cb32585'),
    # BtcBot('BOT 2', 5 / 100, '8ad8b998867bf0891c7ff8d7edcd1ee0'),
    BtcBot('BOT 3', -1 / 100, '27318c228da9d5c7fde6afa47d4b592e')
]

try:
    while True:
        for b in botList:
            b.connect()
        time.sleep(.1)
except KeyboardInterrupt:
    print("Good bye!")
