import requests
import lxml
from lxml import html


def job():
    url = "http://traintimes.org.uk/Meldreth/Cambridge/0800/today"

    r = requests.get(url)
    tree = html.fromstring(r.content)

    traintime = tree.xpath('//*[@id="result0"]/strong/text()')
    possibledelayed = tree.xpath('//*[@id="result0"]/a[1]/text()')

    times = traintime[0].split()
    departuretime = times[0]
    arrivaltime = times[2]

    if possibledelayed[0] == 'iCal':
        message = "The " + departuretime + \
            " is not delayed and will arrive at " + arrivaltime
    else:
        message = "The " + departuretime + " is " + possibledelayed[0]

    print(message)

    from pushover import init, Client
    token = 'aqea1ttcxmcty1pkmgpviwbah54tv8'
    key = 'unvkmu5bskjfyko57qwg2e7txq87vy'
    client = Client(key, api_token=token)
    client.send_message(message)


job()

# scrapes information about the 1st train from meldreth to cambridge after 8am and also notifies me of this information via a phone notification
