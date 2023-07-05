# Initialisation de la fenêtre principale (root).
class App():
    def __init__(self):
        self.root = Tk()
        self.root.title("Gestion de livres")
        self.root.geometry("600x600")  # Dimensions de la fenêtre principale.

        # Définition et configuration du menu principal.
        self.menu_principal = Menu(self.root)
        self.root.config(menu=self.menu_principal)



        ########################
        # Menu "Fichier"
        self.fichier_menu = Menu(self.menu_principal)  # L'item "Fichier" relève du menu principal.
        self.menu_principal.add_cascade(label="Fichier", menu=self.fichier_menu)  # On rend l'item "Fichier" déroulant.
        self.fichier_menu.add_command(label="Charger", command=self.entree_align)
        self.fichier_menu.add_command(label="Sauvegarder", command=lambda: print("sauvegarder"))
        self.fichier_menu.add_command(label="Effacer", command=self.effacer)
        self.fichier_menu.add_separator()
        self.fichier_menu.add_command(label="Quitter", command=self.root.quit)
        # Boutton associé avec cet item du menu.


        # Menu "Trier"
        self.trier_menu = Menu(self.menu_principal)
        self.menu_principal.add_cascade(label="Trier", menu=self.trier_menu)
        self.trier_menu.add_command(label="Cote", command=lambda: print("cote"))
        self.trier_menu.add_command(label="Titre", command=lambda: print("titre"))
        self.trier_menu.add_command(label="Pages", command=lambda: print("pages"))
        self.trier_menu.add_command(label="Prix", command=lambda: print("prix"))

        # Menu "Recherche"
        self.recherche_menu = Menu(self.menu_principal)
        self.menu_principal.add_cascade(label="Recherche", menu=self.recherche_menu)
        self.recherche_menu.add_command(label="Cote", command=lambda: print("cote"))
        self.recherche_menu.add_command(label="Titre", command=lambda: print("titre"))

        # Menu "Aide"
        self.aide_menu = Menu(self.menu_principal)
        self.menu_principal.add_cascade(label="Aide", menu=self.aide_menu)
        self.aide_menu.add_command(label="À propos", command=aide_box)

        self.root.mainloop()
        # self.root.destroy()

    def entree_align(self):
        """Récupère la liste de listes générées par "recup_livre()".
        Args:
            liste(list): Liste constituée d'une liste d'entrées de livres comportant chacune 4 éléments.

        Returns:
            None
        """
        global liste_init
        for l in self.root.grid_slaves():
            l.grid_forget()
        liste = charger()
        if liste_init == list[any]:
            liste_init = liste.copy()
        else:
            warn = False
            for i in range(len(liste)):
                ind = 0
                for j in range(len(liste_init)):
                    if liste[i].cote == liste_init[j].cote:
                        ind += 1
                        warn = True
                if ind == 0:
                    liste_init.append(liste[i])
            # if warn == 1:
            #     return messagebox.showinfo('Attention !!!', "Les éléments déjà affichés ne le seront pas une seconde fois")
        for i in range(len(liste_init)):
            Label(self.root, text=liste_init[i].cote).grid(row=i, column=1, sticky=W, padx=10, pady=0)
            Label(self.root, text=liste_init[i].titre).grid(row=i, column=2, sticky=W, padx=10, pady=0)
            Label(self.root, text=liste_init[i].pages).grid(row=i, column=3, sticky=E, padx=10, pady=0)
            Label(self.root, text=float(liste_init[i].prix)).grid(row=i, column=5, sticky=E, padx=10, pady=0)


    def effacer(self):
        """Efface le contenu de l'interface.
        Returns:
            None
        """
        for i in self.root.grid_slaves():
            i.grid_forget()
        global liste_init
        liste_init = []




if __name__ == '__main__':
    from tkinter import *
    from book_carl import *
    f = App()
