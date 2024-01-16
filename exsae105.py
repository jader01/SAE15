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

def affichage():
    f = open("composants.csv", "r") #on ouvre le fichier en 1 et on "r" lis le fichier
    liste=[] #on creer une liste pour y stoquer les part 1 du csv trouver
    
    for elt in f: #pour tout element dans f
        elmgauche=elt.split(";")
    
        liste.append(elmgauche[0]) #on ajoute a la liste trouver précédement les element en premier que l'on a separer
    
        
        elmligne=elt.split("\n") #a est = aux elements separer par un espace


        print(elmgauche[0],"=", elmligne)


#####################################################################################
#                       sortie des infos marque
####################################################################################


def nbrmarque() :

    f = open("composants.csv", "r") #on ouvre le fichier en 1 et on "r" lis le fichier
    marque=[]
    marquesansdouble=[]
    liste=[]

    #pour afficher la collone 3
    for elt in f :
        colonneC=elt.split(";")
        marque.append(colonneC[2])


    #pour enlever les doublon :
    for elt in marque : #pour tous les élement dans marque
        if elt not in marquesansdouble : #si ils ne sont pas dans la liste sans doublons
            marquesansdouble.append(elt) #la liste    .append = on rajoute dans la liste     ()=l'élement que on veut rajouter dans la liste


    #dans la liste avec double combien de fois retrouve t on des element de la liste SANS DOUBLE :
    for elt in marquesansdouble : #pour chaque element de la liste sans double
        x=marque.count(elt) #la liste avec les double       .count = on compte     quelle sont les elt
        liste.append(x)
    print("nbr :")
    print(liste) #dans le graph : ord


    #le graph :
    xpoints= np.array(marquesansdouble[1:]) #[1:] = a partir de l'élement 2 d'indice 1 jusqu'a la fin peut importe la fin (donc enlève math)
    ypoints= np.array(liste[1:])
    plt.bar(xpoints, ypoints)
    plt.show()    







###############################################################################
#                     apl fonction
##############################################################################

affichage()

nbrmarque()
