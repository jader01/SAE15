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

import folium #import de la librairie permetant de générer la carte


#####################################################################################
#                       Generation d'ip
####################################################################################

def shearchip():
    f = open("controller_reduit.log", "r") #on ouvre le fichier en 1 et on "r" lis le fichier
    listead=[] #on creer une liste pour y stoquer les ip trouver
    for elt in f: #pour tout element dans f
        a=elt.split(" ") #a est egalau element separer par un espace
        listead.append(a[0]) #on ajoute a la liste trouver précédement les element en premier que l'on a separer
    print("la liste des ip est : \n")
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
        print("generation du tableau en cours...\n")
    print('voici un tableau avec pour chaque partie l ip la lat et la long : \n')
    print([ip,lati,longi]) 
    return(tab)


##################################################################################
#                         affichage de la carte et placement des ip
#################################################################################

def create_map(ip) :
    carte=folium.Map(location=[0, 0]) #creation de la carte ; la partie location sert a s'avoir le pts de creation de la carte
    for tab in ip : #pour tous les tableau dans le parametre 
        folium.Marker([tab[1], tab[2]], icon=folium.Icon(color='red')).add_to(carte) #on creer un marker avec dedant la loc un point+sa couleur et on l'ajoute a notre variable carte
        #tabe 1 et tab 2 etant les "sous partie" du tableau qui nous interesse cad lat et long
    carte.save('maptest5.html') #la carte est sauvegarder dans un fichier html (si le chemin n'est pas préciser il sera creer dans )



###############################################################################
#                     apl fonction
##############################################################################

tabip=gene_lat_lon(shearchip()) #on affecte à la variable tableau ip la fonction d'optention de la latitude et la longitude avec en paramètre la liste des IP et cela nous donnc un tableau comportant pour chaque partie : ip, lat, long

print(tabip) #on affiche la fonction de gération de tableau d'ip creer precedment

print(create_map(tabip)) #on apl la fonction de génération de map avec le tableau générer précédement dans la fonction
