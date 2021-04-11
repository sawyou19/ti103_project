import random

id_ = 0





class Etudiant:




    """
    +==============+
    | Etudiant     |
    +==============+
    | nom          |
    | prenom       |
    | numero       |
    | adresse      |
    +==============+
    """

    def __init__(self, nom, prenom, adresse):
        self.nom = nom
        self.prenom = prenom
        self.numero = id_
        self.adresse = adresse
        self.x = random.randint(1, 15)

    def email(self):
        return self.prenom + "." + self.nom + "@usb.ca"

jean_dupont = Etudiant("Dupont", "Jean", "N/A")
jeanne_dupont = Etudiant("Dupont", "Jeanne", "N/A")
guillaume_mantelet = Etudiant("Mantelet", "Guillaume", "N/A")

print(jean_dupont.nom)
print(jeanne_dupont.numero)
print(jeanne_dupont.email())