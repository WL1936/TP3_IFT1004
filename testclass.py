class Livre:
    def __init__(self, nom_fichier=""):
        self.nom_fichier = nom_fichier
    def recup_livre(self, nom_fichier):
        # nom_fichier = "livre1.txt"
        livre = open(nom_fichier, "r")
        entrees_str = livre.readlines()
        livre.close()
        liste_entrees = []
        for i in range(len(entrees_str)):  # Permet de créer une liste 2D (liste des attributs de chaque entrée).
            entree = entrees_str[i].split(",")
            liste_entrees.append(entree)
            liste_entrees = liste_entrees
        return liste_entrees

    def recup_entree(self, liste):
        for entree in liste:
            cote = entree[0]
            titre = entree[1]
            pages = entree[2]
            prix = entree[3]
            return cote, titre, pages, prix



if __name__ == "__main__":
     nom_fichier = "livre1.txt"
     livre1 = Livre.recup_livre(Livre(), nom_fichier)
     print(livre1)






