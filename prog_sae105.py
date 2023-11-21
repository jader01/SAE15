

def shearchip():
    f = open("controltower_reduit.log", "r") #on ouvre le fichier en 1 et on "r" lis le fichier
    listead=[] #on creer une liste pour y stoquer les ip trouver
    for elt in f: #pour tout element dans f
        a=elt.split(" ") #a est egalau element separer par un espace
        listead.append(a[0]) #on ajoute a la liste trouver précédement les element en premier que l'on a separer
    print(listead) #affichage de la liste ip mise a jours

shearchip()
