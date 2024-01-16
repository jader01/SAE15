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



###############################################################################
#                     apl fonction
##############################################################################

affichage()

nbrmarque()
