#####################################################################################
#                       sortie des infos
####################################################################################

def composant1():
    f = open("composants.csv", "r") #on ouvre le fichier en 1 et on "r" lis le fichier
    refcomp=[] #on creer une liste pour y stoquer les part 1 du csv trouver

    
    for elt in f: #pour tout element dans f
        a=elt.split("\n") #a est = aux elements separer par un espace

        b=elt.split(";")
        refcomp.append(b[0]) #on ajoute a la liste trouver précédement les element en premier que l'on a separer
        print(b[0],"=", a)

 
###############################################################################
#                     apl fonction
##############################################################################

composant1()
