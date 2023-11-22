import urllib.request
import json
import time

#import du proxy
import os
os.environ["HTTP_PROXY"] = "http://cache.univ-pau.fr:3128" 
os.environ["HTTPS_PROXY"] = "https://cache.univ-pau.fr:3128"

#####################################################################################
#                       Generation d'ip
####################################################################################

def shearchip():
    f = open("controltower_reduit.log", "r") #on ouvre le fichier en 1 et on "r" lis le fichier
    listead=[] #on creer une liste pour y stoquer les ip trouver
    for elt in f: #pour tout element dans f
        a=elt.split(" ") #a est egalau element separer par un espace
        listead.append(a[0]) #on ajoute a la liste trouver précédement les element en premier que l'on a separer
    print(listead) #affichage de la liste ip mise a jours
    return listead #renvois la valeur en dehor de la fontion


##################################################################################
#                         optention lat, long
#################################################################################

def gene_lat_lon(liste) : #on creer une foncction avec un paramettre pour le changer plus tard
    tab=[] # on creer un tableau vide
    url = "http://ip-api.com/json/" #on associe l'url de l'api a un nom de variable
    for ip in liste: #pour toute les ip dans le parrametre
        time.sleep(1) #on met un temps de pause sinon l'api en panique
        response = urllib.request.urlopen (url + ip) #on associe a reponse, grace a la librairie (urllib), une requete et on l'ouvre (url open) et dendant on assosie l'url à l'ip trouver
        data = response.read() #on lit la reponse (.read) precedante et on l'associe à data 
        values = json.loads(data) #(json.load) on creer un fichier json dans le quelle on met toute les data
        lati=values['lat'] #dans l'ati on assosie la valeur lat du fichier json
        longi=values['lon'] #dans longi on associe la valeur lon du fichier json
        tab.append([ip,lati,longi])#dans le tableau on rajoute les 3 valeur precedent
        print([ip,lati,longi]) 
    return(tab)



###############################################################################
#                     apl fonction
##############################################################################


shearchip()
gene_lat_lon(listead)
