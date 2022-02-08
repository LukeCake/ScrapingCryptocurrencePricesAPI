# https://github.com/LukeCake
# crypto scraper v 1.02
# API pro.coinmarketcap.com
# check www.potato.codes

from requests import Request, Session
import json
import time
from datetime import datetime, date

now = datetime.now()
today = date.today()

f = open("ScrapedData.txt", "w+") #find or create .txt file
f.write("%s" % today)
f.write("\nwww.potato.codes")

f.write("\nTime;"
        "BTC_price;BTC_MC;BTC_MCD;BTC_Vol24;"
        "ETH_price;ETH_MC;ETH_MCD;ETH_Vol24;"
        "BNB_price;BNB_MC;BNB_MCD;BNB_Vol24;"
        "\n")
for x in range(0, 5): #repeat 5+1  times = 6 min


    def getInfo():  # Function to get the info

        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'  # Coinmarketcap API url

        parametersBTC = {'slug': 'bitcoin',
                      'convert': 'USD'}  # API parameters to pass in for retrieving specific cryptocurrency data
        parametersETH = {'slug': 'ethereum',
                      'convert': 'USD'}  # API parameters to pass in for retrieving specific cryptocurrency data
        parametersBNB = {'slug': 'bnb',
                         'convert': 'USD'}  # API parameters to pass in for retrieving specific cryptocurrency data

        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'YOUR_API_KEY' # Replace 'YOUR_API_KEY' with the API in your pro.coinmarketcap.com 333 / day free
        }

        now = datetime.now()
        current_time = now.strftime("%H:%M")
        print("Current Time =", current_time)


        session = Session()
        session.headers.update(headers)

        responseBTC = session.get(url, params=parametersBTC)
        responseETH = session.get(url, params=parametersETH)
        responseBNB = session.get(url, params=parametersBNB)

        infoBTC = json.loads(responseBTC.text)['data']['1']['quote']['USD']['price'] # BTC price
        MCBTC = json.loads(responseBTC.text)['data']['1']['quote']['USD']['market_cap'] # BTC market cap
        DomBTC = json.loads(responseBTC.text)['data']['1']['quote']['USD']['market_cap_dominance'] # BTC market cap domination
        Vol24BTC = json.loads(responseBTC.text)['data']['1']['quote']['USD']['volume_24h'] # BTC 24hour volume


        infoETH = json.loads(responseETH.text)['data']['1027']['quote']['USD']['price']
        MCETH = json.loads(responseETH.text)['data']['1027']['quote']['USD']['market_cap']
        DomETH = json.loads(responseETH.text)['data']['1027']['quote']['USD']['market_cap_dominance']
        Vol24ETH = json.loads(responseETH.text)['data']['1027']['quote']['USD']['volume_24h']


        infoBNB = json.loads(responseBNB.text)['data']['1839']['quote']['USD']['price']
        MCBNB = json.loads(responseBNB.text)['data']['1839']['quote']['USD']['market_cap']
        DomBNB = json.loads(responseBNB.text)['data']['1839']['quote']['USD']['market_cap_dominance']
        Vol24BNB = json.loads(responseBNB.text)['data']['1839']['quote']['USD']['volume_24h']


        allPrice = infoBTC,infoETH,infoBNB
        print(allPrice)

        f.write("%s" % current_time)
        f.write(";%d" % infoBTC)
        f.write(";%d" % MCBTC)
        f.write(";%d" % DomBTC)
        f.write(";%d" % Vol24BTC)

        f.write(";%d" % infoETH)
        f.write(";%d" % MCETH)
        f.write(";%d" % DomETH)
        f.write(";%d" % Vol24ETH)

        f.write(";%d" % infoBNB)
        f.write(";%d" % MCBNB)
        f.write(";%d" % DomBNB)
        f.write(";%d" % Vol24BNB)


        f.write("\n")

        time.sleep(60) # 60s = the price is written every minute

    getInfo()  # Calling the function to get the statistics

f.close()