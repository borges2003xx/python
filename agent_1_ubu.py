import os
print "ciao max"+"\n"

question ='niente'
question = raw_input("cosa vuoi chiedere: ")

print "---------------------------------------------------------"
print ("puoi scegliere \n1 per scienze medicina \n 2 per programmazione \n 3 per droni.....")
tipo_agente=input("cosa vuoi chiedere: ")


specimen1='%20AND%20%28'+'site%3Abmj.com%20OR%20site%3Aarvix.org%20OR%20site%3Anature.com%20OR%20site%3Anationalgeographic.it'+'%29'
specimen2='%20AND%20%28'+'site%3Astackoverflow.com%20OR%20site%3Areddit.com%20OR%20site%3Azapier.com%20OR%20site%3Aappcrawlr.com'+'%29'
specimen3='%20AND%20%28'+'site%3Afpvlab.com%20OR%20site%3Arcgroups.com%20OR%20site%3Ahobbyking.com%20OR%20site%3Agithub.com%20OR%20site%3Aopenpilot.org%20OR%20site%3Ahelifreak.com'+'%29'


if  tipo_agente==1:
    stringa_sito=specimen1
elif tipo_agente==2:
    stringa_sito=specimen2
else:
    stringa_sito=specimen3

stringa_richiesta='/opt/google/chrome/chrome'+' www.google.it/search?q='+question +stringa_sito

print (stringa_richiesta)

os.system(stringa_richiesta)
