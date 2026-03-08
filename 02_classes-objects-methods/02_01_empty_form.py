# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.


class FormulaireMedical:
    
    """Blueprint (Plan) représentant un formulaire vide chez le médecin."""

    def __init__(self, nom_complet, date_naissance, groupe_sanguin):
        # Ces placeholders sont maintenant remplis avec des données spécifiques
        self.patient = nom_complet
        self.naissance = date_naissance
        self.sang = groupe_sanguin
        self.est_rempli = True

    def __repr__(self):
        # Une représentation technique pour le médecin (le développeur)
        return f"FormulaireMedical(patient='{self.patient}', sang='{self.sang}')"
    
    def __str__(self):
        # Une version lisible pour l'accueil du cabinet
        return f"Dossier Patient : {self.patient}| né(e) le : {self.naissance}| groupe sanguin {self.sang}"
    
# Instanciation de quelques formulaires remplis
form1 = FormulaireMedical("Alice Dupont", "1990-05-15", "A+")
form2 = FormulaireMedical("Bob Martin", "1985-11-30", "O-")
form3 = FormulaireMedical("Charlie Bernard", "1995-08-20", "B+")

# Affichage des formulaires
print(form1)  # Utilise __str__
print(repr(form1))  # Utilise __repr__
print(f" Le groupe sanguin de {form2.patient} est {form2.sang}.")  # Accès direct aux attributs
print(f" Le groupe sanguin de {form3.patient} est {form3.sang}.")  # Accès direct aux attributs