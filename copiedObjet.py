import copy
# shallow copy / deep copy


class Personne:
    def __init__(self, nom, age, amis):
        self.nom = nom
        self.age = age
        self.amis = amis

    def AffichezInfos(self):
        print(f"Je m'appelle {self.nom}, j'ai {self.age} ans")
        print(f"Amis: {self.amis}")

    def __eq__(self, other):
        return self.nom == other.nom and self.age == other.age


personne1 = Personne("Jean", 20, ["claire", "Marc", "Emilie"])
personne1.AffichezInfos()

personne2 = copy.deepcopy(personne1)
# personne1.nom = "Toto"
personne1.amis[0] = "Chantale"
personne2.AffichezInfos()


print()
print(personne1 == personne2)
print(personne1 is personne2)
print(personne1.__dict__ == personne2.__dict__)
