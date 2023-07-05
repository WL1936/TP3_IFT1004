import datetime
import os
from tkinter import *
from tkinter import filedialog

import graphique_serge3

liste_totale = []

class Book():
    def __init__(self, liste):
        self.cote = liste[0]
        self.titre = liste[1]
        self.pages = int(liste[2])
        self.prix = float(liste[3])

def charger():
    """Ouvre une fenêtre pour choisir et ouvrir un fichier et crée une liste de listes.
    Ajoute également une liste lorsque différente.

    Returns: livre (list)
    """
    nom = os.path.basename(filedialog.askopenfilename())
    fichier = open(nom, "r")
    entrees_str = fichier.readlines()
    fichier.close()
    liste_locale = []
    global liste_totale
    for i in range(len(entrees_str)):  # Permet de créer une liste 2D (liste des attributs de chaque entrée).
        entree = entrees_str[i].split(",")
        liste_locale.append(entree)
        if entree not in liste_totale:
            liste_totale.append(entree)
    return liste_totale

# charger()

def chercher_cote():
    cote = graphique_serge3.saisir_cote()
    print(cote)
    for i in range(len(liste_totale)):
        if cote == liste_totale[i][0]:
            print("TRUE")
            return TRUE
        else:
            print("FALSE")
            return FALSE
