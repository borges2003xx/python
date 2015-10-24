
from xml.etree import ElementTree

with open('feedly.opml', 'rt') as f:
    tree = ElementTree.parse(f)
    
#for node in tree.iter():
#   print (node.tag, node.attrib)

#for node in tree.iter('outline'):
#   name = node.attrib.get('text')
#    url = node.attrib.get('xmlUrl')
#    if name and url:
#       print ( name, url)
#    else:
#        print (name)
        
for node in tree.findall('.//outline'):
    url = node.attrib.get('xmlUrl')
    if url:
        mu=url
        print (mu)
        
print (mu)

