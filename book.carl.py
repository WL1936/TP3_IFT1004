# # Fichier / Charger
# def charger(file):
#     """Affiche à l'écran le contenu d'un fichier ayant une extension '.txt'.
#     :param file (str): Nom du fichier avec l'extension.
#     :return: Les chaînes de caractères constituant le fichier entré en argument.
#     """
#     of = open(file, 'r')
#     lt = of.readlines()
#     of.close()
#
#     for i in range(1,len(lt)):  # Je ne suis pas sûr qu'il faille tenir compte de la première entrée: on dirait plutôt un cas générique.
#         lt[i] = lt[i].replace(",", " ")
#         print(lt[i], end="")  # J'ai ajouté le end="" pour éviter l'interligne double.
#
# charger('livre1.txt')
#
# class Book():
#     "Définie la structure des livres de la collection"
#     def __init__(self, self, cote, titre, pages, prix):


######## COPY SERGE