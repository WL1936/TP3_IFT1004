# Importation
import datetime
import os
from tkinter import *
from tkinter import messagebox, filedialog
import book_sans_classe

# Initialisation de la fenêtre principale (root).
root = Tk()
root.title("Gestion de livres")
root.geometry("600x600")  # Dimensions de la fenêtre principale.

# Définition et configuration du menu principal.
menu_principal = Menu(root)
root.config(menu=menu_principal)

# FONCTIONS
def ouvrir_fichier():
    """Ouvre une fenêtre pour choisir et ouvrir un fichier.

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
    return(liste_livre)


def entree_align(liste):
    """Récupère la liste de listes générées par "recup_livre()".
    Args:
        liste(list): Liste constituée d'une liste d'entrées de livres comportant chacune 4 éléments.

    Returns:
        None
    """
    for i in range(len(liste)):
        cote = Label(root, text=liste[i][0])
        titre = Label(root, text=liste[i][1])
        pages = Label(root, text=liste[i][2])
        prix = Label(root, text=float(liste[i][3]))

        cote.grid(row=i, column=1, sticky=W, padx=10, pady=0)
        titre.grid(row=i, column=2, sticky=W, padx=10, pady=0)
        pages.grid(row=i, column=3, sticky=E, padx=10, pady=0)
        prix.grid(row=i, column=5, sticky=E, padx=10, pady=0)


def effacer():
    """Efface le contenu de l'interface.
    Returns:
        None
    """
    for i in root.grid_slaves():
        i.grid_forget()


def aide_box():
    """Affiche le message "À propos".
    Returns:
        None
    """
    message = "Gestion de livres v1.0.0"
    today = datetime.date.today().year
    auteurs = "Carl Villeneuve-Lepage\net\nSerge Lacasse"
    message_total = "{}\n{}\n{}".format(message, today, auteurs)
    messagebox.showinfo("À propos", message_total, parent=root)


########################
# Menu "Fichier"
fichier_menu = Menu(menu_principal)  # L'item "Fichier" relève du menu principal.
menu_principal.add_cascade(label="Fichier", menu=fichier_menu)  # On rend l'item "Fichier" déroulant.
fichier_menu.add_command(label="Charger", command=book_sans_classe.charger)
fichier_menu.add_command(label="Sauvegarder", command=lambda: print("sauvegarder"))
fichier_menu.add_command(label="Effacer", command=effacer)
fichier_menu.add_separator()
fichier_menu.add_command(label="Quitter", command=root.quit)
# Boutton associé avec cet item du menu.


# Menu "Trier"
trier_menu = Menu(menu_principal)
menu_principal.add_cascade(label="Trier", menu=trier_menu)
trier_menu.add_command(label="Cote", command=lambda: print("cote"))
trier_menu.add_command(label="Titre", command=lambda: print("titre"))
trier_menu.add_command(label="Pages", command=lambda: print("pages"))
trier_menu.add_command(label="Prix", command=lambda: print("prix"))

# Menu "Recherche"
recherche_menu = Menu(menu_principal)
menu_principal.add_cascade(label="Recherche", menu=recherche_menu)
recherche_menu.add_command(label="Cote", command=lambda: print("cote"))
recherche_menu.add_command(label="Titre", command=lambda: print("titre"))

# Menu "Aide"
aide_menu = Menu(menu_principal)
menu_principal.add_cascade(label="Aide", menu=aide_menu)
aide_menu.add_command(label="À propos", command=aide_box)


root.mainloop()
root.destroy()