from random import random
from bisect import bisect
from collections import OrderedDict
from operator import itemgetter


def weighted_choice(choices):
    values, weights = zip(*choices)
    total = 0
    cum_weights = []
    for w in weights:
        total += w
        cum_weights.append(total)
    x = random() * total
    i = bisect(cum_weights, x)
    return values[i],weights[i]

def pulisce(servizio):
    servizio=servizio.split(' ')
    servizio=list(OrderedDict.fromkeys(servizio))
    servizio=' '.join(servizio)
    return servizio

def sanifica(servi):
    servi=(pulisce(servi[0]),servi[1])
    return servi  

def generate():
    father=weighted_choice(world)
    mother=weighted_choice(world)
    if (father != mother):
       son=(father[0]+" "+mother[0],(father[1]+mother[1])/2)
       return son
    else:
       return 

def unica(lista):
    lista=list(set(lista))
    return lista


 

world=[('raspberry',200),('python',100),('drone',100),('resource',200),('forum',100)]
caio=('mario giuseppe mario antonio', 300)
newworld=[]

for i in range(0,30):
    newworld.append(generate())

uscita=list(OrderedDict.fromkeys(newworld))
uscita.sort()
uscita.remove(None)
print uscita


print sanifica(caio)    


service=[('raspberry',1),('python',3),('drone',4),('resource',2),('forum',5)]
print sorted(service, key=itemgetter(1))


