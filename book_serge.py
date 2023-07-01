# from graphique_serge import *
class Livre:
    def __init__(self, cote: str, titre: str, pages: int, prix: float):
        self.cote = cote
        self.titre = titre
        self.pages = pages
        self.prix = prix


class Gestion:
    def __init__(self, nom_fichier):
        self.nom_fichier = nom_fichier


    # def recup_livre(self, nom):
    #     # nom = input("Entrez le nom du fichier : ")
    #     livre = open("nom", "r")
    #     entrees_str = livre.readlines()
    #     livre.close()
    #     liste_entrees = []
    #     for i in range(1, len(entrees_str)):  # Permet de créer une liste 2D (liste des attributs de chaque entrée).
    #         entree = entrees_str[i].split(",")
    #         liste_entrees.append(entree)
    #     for entree in liste_entrees:
    #         cote = entree[0]
    #         titre = entree[1]
    #         pages = int(entree[2])
    #         prix = float(entree[3])
    #     print(cote, titre, pages, prix)
            # return cote, titre, pages, prix

    # nom = input("Entrez nom du fichier : ")
    # print(nom)

# if __name__ == "__main__":
