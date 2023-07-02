from tkinter import *
from tkinter import messagebox
import datetime

# Initialisation de la fenêtre principale (root).
root = Tk()
root.title("Gestion de livres")
root.geometry("600x600")  # Dimensions de la fenêtre principale.

# Définition et configuration du menu principal.
menu_principal = Menu(root)
root.config(menu=menu_principal)

# Menu "Fichier"
fichier_menu = Menu(menu_principal)  # L'item "Fichier" relève du menu principal.
menu_principal.add_cascade(label="Fichier", menu=fichier_menu)  # On rend l'item "Fichier" déroulant.
fichier_menu.add_command(label="Charger", command=lambda: print("charger"))
fichier_menu.add_command(label="Sauvegarder", command=lambda: print("sauvegarder"))
fichier_menu.add_command(label="Effacer", command=lambda: print("effacer"))
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

aide_menu.add_command(label="À propos", command=aide_box)

root.mainloop()
root.destroy()
