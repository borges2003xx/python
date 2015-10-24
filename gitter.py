import requests
from bs4 import BeautifulSoup


markup_str = requests.get("https://gitter.im/numenta/public/archives/2015/08/19").content
soup = BeautifulSoup(markup_str, 'html.parser')

chat_container = soup.find(id='chat-container')
chat_items = chat_container.find_all(class_='chat-item')

for chat_item in chat_items:
    msg = chat_item.find(class_='chat-item__text').get_text().strip()
    poster = chat_item.find(class_='chat-item__from').get_text().strip()
    posted_at = chat_item.find(class_='chat-item__time').get_text().strip()
    print "({}) {}: {}".format(posted_at, poster, msg)
