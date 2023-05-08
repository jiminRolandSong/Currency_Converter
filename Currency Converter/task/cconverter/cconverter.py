# write your code here!
# coins = input()
# print("I have {} conicoins".format(coins))
# print("{} conicoins cost {} dollars".format(coins, int(coins) * 100))
# print("I am rich! Yippee!")
#conicoins = input("Please, enter the number of conicoins you have:")
#rate = input("Please, enter the exchange rate:")
#print("The total amount of dollars: {}".format(float(conicoins)*float(rate)))

#currencies= {"RUB": 2.98, "ARS": 0.82, "HNL": 0.17, "AUD": 1.9622, "MAD": 0.208}

#coni = float(input())
#for key in currencies:
#   coni_change = round(currencies[key] * coni,2)
#  print("I will get {} {} from the sale of {} conicoins".format(coni_change,key,coni))
import requests
currency = input().lower()
url = " http://www.floatrates.com/daily/{}.json".format(currency)
f = requests.get(url).json()
cache = {}
if currency == 'usd':
    cache = {'eur' : f['eur']['rate']}
elif currency == 'eur':
    cache = {'usd' : f['usd']['rate']}
else:
    cache = {'usd' : f['usd']['rate'],'eur' : f['eur']['rate']}
exchange = input()
money = int(input())
while (exchange != "" ):
    print("Checking the cache...")
    if (exchange.lower() in cache.keys()):
        print("Oh! It is in the cache!")
        get = round(cache[exchange.lower()] * money,2)
        print("You received {} {}".format(str(get), exchange))
    else:
        print("Sorry, but it is not in the cache!")
        cache[exchange.lower()] = f[exchange.lower()]['rate']
        get = round(cache[exchange.lower()] * money,2)
        print("You received {} {}".format(str(get), exchange))
    exchange = input()
    if exchange == "":
        break
    money = int(input())
