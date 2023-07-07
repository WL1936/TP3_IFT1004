import os
import datetime
from tkinter import messagebox, filedialog
# import graphique_serge4
from typing import List, Any


# Book definition
class Book():
    def __init__(self, liste):
        self.cote = liste[0]
        self.titre = liste[1]
        self.pages = liste[2]
        self.prix = float(liste[3])

# global liste_init
liste_init = list[any]

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


def effacer():
    """Efface le contenu de l'interface.
    Returns:
        None
    """
    return []


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

def sauvegarder(liste, nom_fichier):
    """
    Sauvegarde le contenu d'une liste dans un fichier texte
    :param liste (list): liste d'objets "Book"
    :param nom_fichier (str): nom du fichier désiré
    :return:
    """
    f = open(nom_fichier, "w")
    for livre in liste:
        f.write("{},{},{},{}\n".format(livre.cote, livre.titre, livre.pages, livre.prix))
    f.close()

def tri_cote(liste):
    nl = []
    for i in liste:
        nl.append(i.cote)
    lt = []
    for i in sorted(nl):
        lt.append(liste[nl.index(i)])
    return lt

def tri_titre(liste):
    nl = []
    for i in liste:
        nl.append(i.titre)
    lt = []
    for i in sorted(nl):
        lt.append(liste[nl.index(i)])
    return lt

def tri_pages(liste):
    nl = []
    for i in liste:
        nl.append(int(i.pages))
    nlstr = []
    for i in liste:
        nlstr.append(i.pages)
    tempo_list = []
    for i in sorted(nl):
        tempo_list.append(str(i))
    lt = []
    for i in tempo_list:
        lt.append(liste[nlstr.index(i)])
    return lt

def tri_prix(liste):
    nl = []
    for i in liste:
        nl.append(i.prix)
    lt = []
    for i in sorted(nl):
        lt.append(liste[nl.index(i)])
    return lt

def convert_book_to_list(liste_init):
    iter_list = []
    for livre in liste_init:
        tempo_list = []
        for j in [livre.cote, livre.titre, livre.pages, livre.prix]:
            tempo_list.append(j)
        iter_list.append(tempo_list)
    return iter_list
