# Modificateurs d'accès: Public, Private, Proctected

# public: accès depuis l'intérieur et l'extérieurvde la classe

# private: accès depuis l'intérieur de la classe (__a)

# protected: accès depuis l'intérieur de la classe et des classes dérivées (_a)

class Personne:
    def __init__(self, nom):
        self._nom = nom

    def se_presenter(self):
        print(f"Je m'appelle {self._nom}")


class Etudient(Personne):
    def se_presenter(self):
        print(f"Je suis étudient, je m'appelle {self._nom}")


personne1 = Etudient("Jean")
# personne1._nom = "Toto"
personne1.se_presenter()

print(personne1.__dict__)
