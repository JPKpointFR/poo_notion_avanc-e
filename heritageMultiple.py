

class EtreVivant:
    def afficher_infos(self):
        print("Je suis un être vivant")


class Predateur():
    def chasser_manger_proie(self):
        print("Miam Miam")


class Lion(EtreVivant, Predateur):
    def afficher_infos(self):
        print(f"Je suis un Lion")


class Personne(EtreVivant):
    def afficher_infos(self):
        print(f"Je suis une personne")


lion = Lion()
lion.afficher_infos()
lion.chasser_manger_proie()
