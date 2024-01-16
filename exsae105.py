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


###############################################################################
#                     apl fonction
##############################################################################

affichage()
