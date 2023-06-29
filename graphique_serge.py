from tkinter import *

# Initialisation de la fenêtre principale (root).
root = Tk()
root.title("Gestion de livres")
root.geometry("600x600")  # Dimensions de la fenêtre principale.
frame_menu = Frame(root)
#
# Définition et configuration du menu principal.
menu_principal = Menu(root)
root.config(menu=menu_principal)

# Menu "Fichier"
fichier_menu = Menu(menu_principal)  # L'item "Fichier" relève du menu principal.
menu_principal.add_cascade(label="Fichier", menu=fichier_menu)  # On rend l'item "Fichier" déroulant.
# Options du menu déroulant.
fichier_menu.add_command(label="Charger", command=lambda: print("charger"))  # Permet de vérifier si ça fonctionne.
fichier_menu.add_command(label="Sauvegarder", command=lambda: print("sauvegarder"))
fichier_menu.add_command(label="Effacer", command=lambda: print("effacer"))
fichier_menu.add_command(label="Quitter", command=root.quit)
# Boutton associé avec cet item du menu.




# Menu "Trier"
trier_menu = Menu(menu_principal)
menu_principal.add_cascade(label="Trier", menu=trier_menu)
fichier_menu.add_command(label="Cote", command=lambda: print("cote"))
fichier_menu.add_command(label="Titre", command=lambda: print("titre"))
fichier_menu.add_command(label="Pages", command=lambda: print("pages"))
fichier_menu.add_command(label="Prix", command=lambda: print("prix"))


# Menu "Recherche"
recherche_menu = Menu(menu_principal)
menu_principal.add_cascade(label="Recherche", menu=recherche_menu)
fichier_menu.add_command(label="Cote", command=lambda: print("cote"))
fichier_menu.add_command(label="Titre", command=lambda: print("titre"))


# Menu "Aide"
aide_menu = Menu(menu_principal)
menu_principal.add_cascade(label="Aide", menu=aide_menu)
# Ouvrira une fenêtre d'information.

root.mainloop()
