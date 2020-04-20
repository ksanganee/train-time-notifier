import requests
import pprint
import json
from bs4 import BeautifulSoup
from pushover import init, Client
from collections import OrderedDict
import time
import datetime


def job():
    ts = time.time()

    st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M')
    print(st)
    url = 'http://traintimes.org.uk/Meldreth/Cambridge/0800/today'


    r1 = requests.post(url)


    soup = BeautifulSoup(r1.text, 'lxml')

    soup_str = str(soup.ul)
    soup_list = (soup_str).split('\n')

    line1 = soup_list[0]
    line2 = soup_list[1]

    line1_list = line1.split()
    line2_list = line2.split()

    time1 = str(line1_list[2])
    time1 = time1[-5:]

    time2 = str(line1_list[4])


    soup1 = soup.find(id='result0')

    soup_text = soup1.get_text()

    soup_list = list(str(soup_text))

    t = ''

    for i in range(0,13):
        t = t + str(soup_list[i])

    if soup_list[22] == 'l':
        if str(soup_list[11]).isdigit() == True:
            message = t + ' is delayed by ' + str(soup_list[11]) + ' mins'
    else:
        if soup_list[23] == 'l':
            td = (int(soup_list[15]) * 10) + int(soup_list[16])
            message = t + ' is delayed by ' + str(td) + ' mins'
        else:
            if str(soup_list[15]) == 'c':
                message = 'Check app'
            else:
                message = t
    a = st + ' Traintimes'

    token = 'aqea1ttcxmcty1pkmgpviwbah54tv8'

    key = 'unvkmu5bskjfyko57qwg2e7txq87vy'
    client = Client(key, api_token=token)
    client.send_message(message, title=st)



job()
