from tkinter import *
from tkinter import filedialog
import os
liste_totale = []
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
        liste_totale.append(entree)
        liste_locale.append(entree)
    print(liste_totale)
    return liste_totale

# charger()

def chercher_cote(cote):
    for entree in charger():
        if cote in entree[0]:
            print(entree[0])
            break
        else:
            print("Message d'erreur dans boîte")
            break





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
