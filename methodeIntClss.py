class Personne:
    TYPE = "Humain"

    def __init__(self, nom):
        self.nom = nom

    # Méthode d'instance
    def se_presenter(self):
        i = print(
            f"Je m'appelle {self.formater_chaine(self.nom)} - {self.TYPE}")

    # 1er caractère en maj puis min
    # méthode statiques
    @staticmethod
    def formater_chaine(a):
        return a[0].upper()+a[1:].lower()

    @classmethod
    def methode_de_classe(cls):
        print(f"Méthode de classe: {cls.TYPE}")


personne1 = Personne("jeAn")
personne1.se_presenter()
print(Personne.formater_chaine("toto"))

Personne.methode_de_classe()
