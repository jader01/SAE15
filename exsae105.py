#####################################################################################
#                       import des librairie utiles
####################################################################################

import urllib.request #api de recup liste
import json #pour utiliser un fichier json
import time #pour faire des pause sinon l'api oskour

#import du proxy
import os #pour utiliser le proxy  
os.environ["HTTP_PROXY"] = "http://cache.univ-pau.fr:3128" 
os.environ["HTTPS_PROXY"] = "https://cache.univ-pau.fr:3128"

#import folium #import de la librairie permetant de générer la carte
import matplotlib.pyplot as plt #librairie pour des graphes
import numpy as np

#####################################################################################
#                       sortie des infos
####################################################################################

def composant1():
    f = open("composants.csv", "r") #on ouvre le fichier en 1 et on "r" lis le fichier
    refcomp=[] #on creer une liste pour y stoquer les part 1 du csv trouver
    #nomcomp=[] #on creer une liste ou on vas stocker le reste de la ligne
    #marque=[]
    #letype=[]
    
    for elt in f: #pour tout element dans f
        a=elt.split("\n") #a est = aux elements separer par un espace
        #print("a=",a)
        #print("a[0]=",a[0])
        b=elt.split(";")
        #print(b)
        refcomp.append(b[0]) #on ajoute a la liste trouver précédement les element en premier que l'on a separer
        print(b[0],"=", a)

    
#    for elt in f :
        
    
       
       
        #nomcomp.append(a[1])#dans ma liste resteligne on rajout les élément 2, 3,
        #marque.append(a[2])
        #letype.append(a[3])
    #print("la première colonne de chaque ligne est : \n")
    #print(refcomp) #affichage de la liste ip mise a jours
    #print("la colonne 2 : \n")
    #print(nomcomp)
    #print("la colonne 3: \n")
    #print(marque)
    #print("la colonne 4: \n")
    #print(letype)





###############################################################################
#                     apl fonction
##############################################################################

composant1()