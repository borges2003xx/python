import requests
from bs4 import BeautifulSoup
import datetime


def riporta(giorno):
    richiesta="https://gitter.im/PX4/VTOL/archives/"+giorno
    print richiesta
    markup_str = requests.get(richiesta).content
    soup = BeautifulSoup(markup_str, 'html.parser')

    chat_container = soup.find(id='chat-container')
    chat_items = chat_container.find_all(class_='chat-item')

    for chat_item in chat_items:
        msg = chat_item.find(class_='chat-item__text').get_text().strip()
        msg=msg.encode('ascii', 'ignore')
        poster = chat_item.find(class_='chat-item__from').get_text().strip()
        poster=poster.encode('ascii', 'ignore')
        posted_at = chat_item.find(class_='chat-item__time').get_text().strip()
        posted_at=posted_at.encode('ascii', 'ignore')
        pulitura= "({}) {}: {}".format(posted_at, poster, msg)
        
        print pulitura





a = datetime.datetime.today()
numdays = 100
dateList = []
for x in range (0, numdays):
    t=(a - datetime.timedelta(days = x))
    t1=t.strftime('%Y/%m/%d')
    dateList.append(t1)

for x in dateList:
    riporta(x)





