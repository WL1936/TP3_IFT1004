from graphique_serge import *
class Livre:
    def __init__(self, cote, titre, pages, prix):
        self.cote = cote
        self.titre = titre
        self.pages = pages
        self.prix = prix


    def recup_livre(self, nom):
        self.livre = open(nom, "r")
        print(livre)
        entrees_str = livre.readlines()
        print(entrees_str)
        livre.close()
        liste_entrees = []
        for i in range(1, len(entrees_str)):  # Permet de créer une liste 2D (liste des attributs de chaque entrée).
            entree = entrees_str[i].split(",")
            liste_entrees.append(entree)
        for entree in liste_entrees:
            cote = entree[0]
            titre = entree[1]
            pages = int(entree[2])
            prix = float(entree[3])
            print(cote, titre, pages, prix)
            # return cote, titre, pages, prix





