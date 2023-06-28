from tkinter import*
from tkinter import filedialog as fd

# Initialisation de la fenêtre principale.
root = Tk()
root.title("Gestion de livres")
root.geometry("800x800")
root.mainloop()

# Création du menu principal (mais je ne le vois pas : quelque chose que j'oublie ?).
menu_principal = Menu(root)
root.config(menu=menu_principal)

def ma_commande():  # En attendant que l'on crée les fonctions pour chacun des items du menu.
    pass

fichier_menu = Menu(root)
menu_principal.add_cascade(label="Fichier", menu=fichier_menu)
fichier_menu.add_command(label="Charger", command=ma_commande)  # Définir chacune des fonctions plus tard.
fichier_menu.add_command(label="Sauvegarder", command=ma_commande)
fichier_menu.add_command(label="Effacer", command=ma_commande)
fichier_menu.add_separator()
fichier_menu.add_command(label="Quitter", command=fenetre.quit)

trier_menu = Menu(root)
menu_principal.add_cascade(label="Trier", menu=trier_menu)
trier_menu.add_command(label="Cote", command=ma_commande)
trier_menu.add_command(label="Titre", command=ma_commande)
trier_menu.add_command(label="Pages", command=ma_commande)
trier_menu.add_command(label="Prix", command=ma_commande)

recherche_menu = Menu(root)
menu_principal.add_cascade(label="Recherche", menu=recherche_menu)
recherche_menu.add_command(label="Cote", command=ma_commande)
recherche_menu.add_command(label="Titre", command=ma_commande)

aide_menu = Menu(root)
# Créer une fenêtre "À propos"

def charger_fichier():
    fichier = fd.askopenfilename(title="Sélectionnez un fichier")
    os.startfile(os.path.abspath(fichier))

charger_fichier(0)


