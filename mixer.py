
from xml.etree import ElementTree
import feedparser
import unicodedata

indirizzi=[]

with open('feedly.opml', 'rt') as f:
    tree = ElementTree.parse(f)
    
for node in tree.findall('.//outline'):
    url = node.attrib.get('xmlUrl')
    if url:
        mu=url
        print (mu)
        indirizzi.append(mu)
        
print ("---------------------------------------------")        
        
print (indirizzi[42])


d = feedparser.parse(indirizzi[42])

print (d['feed']['title'])
print (d['feed']['link'])
print (d.feed.subtitle)
print (len(d['entries']))
print (d['entries'][0]['title'])
print (d.entries[0]['link'])

for post in d.entries:
    ex=post.title + "-> "+post.link+"\n"
    print (unicodedata.normalize('NFKD', ex).encode('ascii','ignore'))
    
