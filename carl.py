import os
import datetime
from tkinter import messagebox, filedialog

# Book definition
class Book():
    def __init__(self, liste):
        self.cote = liste[0]
        self.titre = liste[1]
        self.pages = liste[2]
        self.prix = float(liste[3])
    # def __str__(self):
    #     return(self.cote, self.titre)


# FONCTIONS
def charger():
    """Ouvre une fenêtre pour choisir et ouvrir un fichier et crée une liste de listes.

    Returns: livre (list)
    """
    nom = os.path.basename(filedialog.askopenfilename())
    fichier = open(nom, "r")
    entrees_str = fichier.readlines()
    fichier.close()
    liste_livre = []
    for i in range(len(entrees_str)):  # Permet de créer une liste 2D (liste des attributs de chaque entrée).
        entree = entrees_str[i].split(",")
        liste_livre.append(entree)
    list_book = []
    for i in liste_livre:
        list_book.append(Book(i))
    return(list_book)






#
# def effacer():
#     """Efface le contenu de l'interface.
#     Returns:
#         None
#     """
#     for i in root.grid_slaves():
#         i.grid_forget()


def aide_box():
    """Affiche le message "À propos".
    Returns:
        None
    """
    message = "Gestion de livres v1.0.0"
    today = datetime.date.today().year
    auteurs = "Carl Villeneuve-Lepage\net\nSerge Lacasse"
    message_total = "{}\n{}\n{}".format(message, today, auteurs)
    return messagebox.showinfo('À propos', message_total)

