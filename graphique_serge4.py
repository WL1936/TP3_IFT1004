
# Initialisation de la fenêtre principale (root).
class App():
    def __init__(self):
        self.root = Tk()
        self.root.title("Gestion de livres")
        self.root.geometry("600x600")  # Dimensions de la fenêtre principale.
        self.root.config(bg="white")

        # Définition et configuration du menu principal.
        self.menu_principal = Menu(self.root)
        self.root.config(menu=self.menu_principal)

        # Création d'un tableau vide.
        # self.empty_table = Treeview(self.root, show="", height=600)



        ########################
        # Menu "Fichier"
        self.fichier_menu = Menu(self.menu_principal)  # L'item "Fichier" relève du menu principal.
        self.menu_principal.add_cascade(label="Fichier", menu=self.fichier_menu)  # On rend l'item "Fichier" déroulant.
        self.fichier_menu.add_command(label="Charger", command=self.tableau)
        self.fichier_menu.add_command(label="Sauvegarder", command=self.save)
        self.fichier_menu.add_command(label="Effacer", command=self.effacer)
        self.fichier_menu.add_separator()
        self.fichier_menu.add_command(label="Quitter", command=self.root.quit)
        # Boutton associé avec cet item du menu.


        # Menu "Trier"
        self.trier_menu = Menu(self.menu_principal)
        self.menu_principal.add_cascade(label="Trier", menu=self.trier_menu)
        self.trier_menu.add_command(label="Cote", command=self.tri_aff_cote)
        self.trier_menu.add_command(label="Titre", command=self.tri_aff_titre)
        self.trier_menu.add_command(label="Pages", command=self.tri_aff_pages)
        self.trier_menu.add_command(label="Prix", command=self.tri_aff_prix)

        # Menu "Recherche"
        self.recherche_menu = Menu(self.menu_principal)
        self.menu_principal.add_cascade(label="Recherche", menu=self.recherche_menu)
        self.recherche_menu.add_command(label="Cote", command=self.saisir_cote)
        self.recherche_menu.add_command(label="Titre", command=self.saisir_titre)

        # Menu "Aide"
        self.aide_menu = Menu(self.menu_principal)
        self.menu_principal.add_cascade(label="Aide", menu=self.aide_menu)
        self.aide_menu.add_command(label="À propos", command=aide_box)

        self.root.mainloop()
        # self.root.destroy()

    def tableau(self):
        """Création d'un tableau qui intégrera la liste des livres et initialisation de ses paramètres.

        Returns:
            None
        """
        columns = ("cote", "titre", "pages", "prix")
        table = Treeview(self.root, columns=columns, show="", height=600)
        style = Style(self.root)
        font_table = ("Menlo", 12)
        style.configure("Treeview", background="white", fieldbackground="white", foreground="black", font=font_table, pady=3)
        table.column(0, width=60)
        table.column(1, width=180)
        table.column(2, width=60, anchor=E)
        table.column(3, width=60, anchor=E)

        # Intégration des données de la liste dans le tableau.
        global liste_init

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
        iter_list = convert_book_to_list(liste_init)
        for l in self.root.grid_slaves():
            l.grid_forget()
        for livre in iter_list:
            table.insert('', END, values=livre)
        table.grid(row=0, column=0, sticky=E)


    def effacer(self):
        """Efface le contenu de l'interface.
        Returns:
            None
        """
        for i in self.root.grid_slaves():
            i.grid_forget()
        global liste_init
        liste_init = []

    def save(self):
        file = filedialog.asksaveasfilename(filetypes=[("txt file", ".txt")],defaultextension=".txt")
        sauvegarder(liste_init, file)


    def saisir_cote(self):
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
        entree_box.focus()

        def chercher_cote(cote):
            global liste_init
            fen.destroy()
            livre = ""
            for i in liste_init:
                if cote == i.cote:
                    livre = str(i.cote) + " " + str(i.titre) + " " + str(i.pages) + " " + str(i.prix)
            if len(livre) != 0:
                messagebox.showinfo("Livre", livre, parent=self.root)
            else:
                messagebox.showinfo("Absent!", "Cote non trouvée", parent=self.root)

        def valider_cote():
            # Validation de l'entrée (Format valide ou non).
            cote_raw = entree_box.get()
            if (len(cote_raw) == 0) or (len(cote_raw) < 5) or (len(cote_raw) > 5) or \
                    (cote_raw[1:2].isnumeric()) or not (cote_raw[2:].isnumeric()):
                fen.destroy()
                messagebox.showinfo("Erreur!", "Format non valide\nFormat : XX000", parent=self.root)
            else:
                cote_format_ok = cote_raw.upper()
                chercher_cote(cote_format_ok)

        bouton_ok = Button(fen, text="   OK  ", command=valider_cote)
        bouton_ok.grid(row=3, sticky=W, padx=30)
        bouton_annuler = Button(fen, text="Annuler", command=fen.destroy)
        bouton_annuler.grid(row=3, sticky=E, padx=30)

    def saisir_titre(self):
        """Ouvre une fenêtre pour récupérer la cote soumise par l'utilisateur et la retourne.

        Returns:
            cote_saisie(str): Cote saisie par l'utilisateur.
        """
        # Création de la fenêtre de saisie.

        fen = Toplevel()
        fen.title("Chercher par titre")
        fen.geometry("250x100")
        label_format = Label(fen, text="\nEntrez titre")
        label_format.grid(padx=30, row=1, sticky=W)
        entree_box = Entry(fen)
        entree_box.grid(padx=30)
        entree_box.focus()

        def chercher_titre(titre_soumis):
            global liste_init
            fen.destroy()
            end = len(titre_soumis)
            livres_trouves = []
            livres = ""
            for i in liste_init:
                if titre_soumis == i.titre[0:end]:
                    livres_trouves.append(str(i.cote) + " " + str(i.titre) + " " + str(i.pages) + " " + str(i.prix))
            if len(livres_trouves) != 0:
                for j in range(len(livres_trouves)):
                    livres += (livres_trouves[j]) + "\n"
                messagebox.showinfo("Livres", livres, parent=self.root, )
            else:
                messagebox.showinfo("Absent!", "Cote non trouvée", parent=self.root)

        def valider_titre():
            # Validation de l'entrée (Format valide ou non).
            titre_raw = entree_box.get()
            titre_rech = titre_raw.upper()
            if (str(titre_rech) == ""):
                fen.destroy()
                messagebox.showinfo("Erreur!", "Entrée non valide :\nAucun titre soumis", parent=self.root)
                return None
            else:
                chercher_titre(titre_rech)

        bouton_ok = Button(fen, text="   OK  ", command=valider_titre)
        bouton_ok.grid(row=3, sticky=W, padx=30)
        bouton_annuler = Button(fen, text="Annuler", command=fen.destroy)
        bouton_annuler.grid(row=3, sticky=E, padx=30)

    def tri_aff_cote(self):
        columns = ("cote", "titre", "pages", "prix")
        table = Treeview(self.root, columns=columns, show="", height=600)
        style = Style(self.root)
        font_table = ("Menlo", 12)
        style.configure("Treeview", background="white", fieldbackground="white", foreground="black", font=font_table, pady=3)
        table.column(0, width=60)
        table.column(1, width=180)
        table.column(2, width=60, anchor=E)
        table.column(3, width=60, anchor=E)

        # Intégration des données de la liste dans le tableau.
        global liste_init
        iter_list = convert_book_to_list(tri_cote(liste_init))
        for l in self.root.grid_slaves():
            l.grid_forget()
        for livre in iter_list:
            table.insert('', END, values=livre)
        table.grid(row=0, column=0, sticky=E)

    def tri_aff_titre(self):
        columns = ("cote", "titre", "pages", "prix")
        table = Treeview(self.root, columns=columns, show="", height=600)
        style = Style(self.root)
        font_table = ("Menlo", 12)
        style.configure("Treeview", background="white", fieldbackground="white", foreground="black", font=font_table,
                        pady=3)
        table.column(0, width=60)
        table.column(1, width=180)
        table.column(2, width=60, anchor=E)
        table.column(3, width=60, anchor=E)

        # Intégration des données de la liste dans le tableau.
        global liste_init
        iter_list = convert_book_to_list(tri_titre(liste_init))
        for l in self.root.grid_slaves():
            l.grid_forget()
        for livre in iter_list:
            table.insert('', END, values=livre)
        table.grid(row=0, column=0, sticky=E)

    def tri_aff_pages(self):
        columns = ("cote", "titre", "pages", "prix")
        table = Treeview(self.root, columns=columns, show="", height=600)
        style = Style(self.root)
        font_table = ("Menlo", 12)
        style.configure("Treeview", background="white", fieldbackground="white", foreground="black", font=font_table,
                        pady=3)
        table.column(0, width=60)
        table.column(1, width=180)
        table.column(2, width=60, anchor=E)
        table.column(3, width=60, anchor=E)

        # Intégration des données de la liste dans le tableau.
        global liste_init
        iter_list = convert_book_to_list(tri_pages(liste_init))
        for l in self.root.grid_slaves():
            l.grid_forget()
        for livre in iter_list:
            table.insert('', END, values=livre)
        table.grid(row=0, column=0, sticky=E)

    def tri_aff_prix(self):
        columns = ("cote", "titre", "pages", "prix")
        table = Treeview(self.root, columns=columns, show="", height=600)
        style = Style(self.root)
        font_table = ("Menlo", 12)
        style.configure("Treeview", background="white", fieldbackground="white", foreground="black", font=font_table,
                        pady=3)
        table.column(0, width=60)
        table.column(1, width=180)
        table.column(2, width=60, anchor=E)
        table.column(3, width=60, anchor=E)

        # Intégration des données de la liste dans le tableau.
        global liste_init
        iter_list = convert_book_to_list(tri_prix(liste_init))
        for l in self.root.grid_slaves():
            l.grid_forget()
        for livre in iter_list:
            table.insert('', END, values=livre)
        table.grid(row=0, column=0, sticky=E)



if __name__ == '__main__':
    from tkinter import *
    from book_serge4 import *
    from tkinter.ttk import Treeview, Style
    f = App()
