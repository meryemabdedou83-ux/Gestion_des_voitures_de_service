class Employe:
    def __init__(self, numeroPermis, nom, prenom):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService = None

    def afficherInformations(self):
        print(self.nom, self.prenom, self.numeroPermis)

class Voiture:
    def __init__(self, matricule, annee, marque, kilometrage):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur = None

    def afficherInformations(self):
        print(self.marque, self.matricule, self.annee, self.kilometrage)

        from employe import Employe
        from voiture import Voiture

        e1 = Employe("A123", "Ali", "Samir")
        e2 = Employe("B456", "Sara", "Nadia")

        v1 = Voiture("123ABC", 2020, "Toyota", 10000)
        v2 = Voiture("456DEF", 2019, "Honda", 20000)
        e1.afficherInformations()
        e2.afficherInformations()

        v1.afficherInformations()
        v2.afficherInformations()