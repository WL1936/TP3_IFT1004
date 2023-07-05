from tkinter import messagebox
from tkinter.ttk import Treeview, Style
from tkinter import *
from book_serge3 import charger
import datetime

# Initialisation de la fenêtre principale "root".
root = Tk()
root.title("Gestion de livres")
root.geometry("600x800")  # Dimensions de la fenêtre principale.

# Définition et configuration du menu principal.
menu_principal = Menu(root)
root.config(menu=menu_principal)


# FONCTIONS D'AFFICHAGE

def tableau():
    """Création d'un tableau qui intégrera la liste des livres et initialisation de ses paramètres.

    Returns:
        None
    """
    columns = ("cote", "titre", "pages", "prix")
    table = Treeview(root, columns=columns, show="", height=50)
    style = Style(root)
    font_table = ("Menlo", 12)
    style.configure("Treeview", background="", fieldbackground="", foreground="black", font=font_table, pady=3)
    table.column(0, width=60)
    table.column(1, width=180)
    table.column(2, width=60, anchor=E)
    table.column(3, width=60, anchor=E)

    # Intégration des données de la liste dans le tableau.
    entrees = charger()
    for entree in entrees:
        table.insert('', END, values=entree)

    # def selection_item(event):
    #     for item_tableau in table.selection():
    #         item = table.item(item_tableau)
    #         fiche = item['values']
    #         # show a message
    #         showinfo(title='Information', message=','.join(str(fiche)), parent= root)
    # table.bind('<<TreeviewSelect>>', selection_item)

    table.grid(row=0, column=0, sticky=E)


def effacer():
    """Efface le contenu de l'interface et de la liste actuellement chargée.
    Returns:
        None
    """
    for i in root.grid_slaves():
        i.grid_forget()
    global liste_init
    liste_init = []


def saisir_cote():
    """Ouvre une fenêtre pour récupérer la cote soumise par l'utilisateur et la retourne.

    Returns:
        cote_saisie(str): Cote saisie par l'utilisateur.

    """
    # Création de la fenêtre de saisie.
    fen = Toplevel()
    fen.title("Chercher par cote")
    fen.geometry("250x100")
    label_format = Label(fen, text="\nFormat : XX000")
    label_format.grid(padx=30, row=1, sticky=W)
    entree_box = Entry(fen)
    entree_box.grid(padx=30)

    # Traitement de la saisie
    def get_cote():
        cote = entree_box.get()
        fen.destroy()
        return cote

    bouton_ok = Button(fen, text="   OK  ", command=get_cote)
    bouton_ok.grid(row=3, sticky=W, padx=30)
    bouton_annuler = Button(fen, text="Annuler", command=fen.destroy)
    bouton_annuler.grid(row=3, sticky=E, padx=30)






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
fichier_menu.add_command(label="Charger", command=tableau)
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
recherche_menu.add_command(label="Cote", command=saisir_cote)
recherche_menu.add_command(label="Titre", command=lambda: print("titre"))

# Menu "Aide"
aide_menu = Menu(menu_principal)
menu_principal.add_cascade(label="Aide", menu=aide_menu)
aide_menu.add_command(label="À propos", command=aide_box)

root.mainloop()
root.destroy()
