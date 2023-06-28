#### Premier jet


# Fichier / Charger
def charger(file):
    """
    Affiche à l'écran le contenu d'un fichier ayant une extension '.txt'
    :param file (str): nom du fichier avec l'extension
    :return: Les chaînes de caractères constituant le fichier entré en argument
    """
    of = open(file, 'r')
    lt = of.readlines()
    of.close()

    for i in range(len(lt)):
        lt[i] = lt[i].replace(",", " ")
        print(lt[i])

charger('livre1.txt')

# Vraiment besoin de finir de lire le chap. 8 + probablement 14, j'ai vu que beaucoup de trucs avec class et widget
# y était présent!
############################################

# class Book():
#     "Définie la structure des livres de la collection"
#     def __init__(self, self, cote, titre, pages, prix):