from tkinter import messagebox
import datetime
from tkinter import messagebox
from book_serge3 import *

# Initialisation de la fenêtre principale "root".
root = Tk()
root.title("Gestion de livres")
root.geometry("600x800")  # Dimensions de la fenêtre principale.

# Définition et configuration du menu principal.
menu_principal = Menu(root)
root.config(menu=menu_principal)

# FONCTIONS D'AFFICHAGE
def entree_align():
    """Récupère la liste de listes générée par "charger()" et affiche les entrées dans la fenêtre principale.

    Returns:
        None
    """
    liste = charger()
    for i in range(len(liste)):
        Label(root, text=liste[i][0]).grid(row=i, column=1, sticky=W, padx=10, pady=0)
        Label(root, text=liste[i][1]).grid(row=i, column=2, sticky=W, padx=10, pady=0)
        Label(root, text=liste[i][2]).grid(row=i, column=3, sticky=E, padx=10, pady=0)
        Label(root, text=float(liste[i][3])).grid(row=i, column=4, sticky=E, padx=10, pady=0)


def aide_box():
    """Affiche le message "À propos".
    Returns:
        None
    """
    message = "Gestion de livres v1.0.0"
    today = datetime.date.today().year
    auteurs = "Carl Villeneuve-Lepage\net\nSerge Lacasse"
    message_total = "{}\n{}\n{}".format(message, today, auteurs)
    return messagebox.showinfo('À propos', message_total, parent=root)

########################
# Menu "Fichier"
fichier_menu = Menu(menu_principal)  # L'item "Fichier" relève du menu principal.
menu_principal.add_cascade(label="Fichier", menu=fichier_menu)  # On rend l'item "Fichier" déroulant.
fichier_menu.add_command(label="Charger", command=entree_align)
fichier_menu.add_command(label="Sauvegarder", command=lambda: print("sauvegarder"))
fichier_menu.add_command(label="Effacer", command=lambda: print("effacer"))
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
recherche_menu.add_command(label="Cote", command=lambda: print("Cote"))
recherche_menu.add_command(label="Titre", command=lambda: print("titre"))

# Menu "Aide"
aide_menu = Menu(menu_principal)
menu_principal.add_cascade(label="Aide", menu=aide_menu)
aide_menu.add_command(label="À propos", command=aide_box)

root.mainloop()
root.destroy()