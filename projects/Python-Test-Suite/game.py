import random


def verifier_devinette(nombre_secret, devinette):
    """Compare la devinette au nombre secret et retourne le feedback."""
    # Validation: s'assurer que la devinette est bien un entier.
    if not isinstance(devinette, int):
        raise TypeError("La devinette doit être un nombre entier.")
    
    # Logique de comparaison avec feedback approprié.
    if devinette < nombre_secret:
        return "Trop bas"
    elif devinette > nombre_secret:
        return "Trop haut"
    else:
        return "Gagné"

def est_partie_terminee(vies):
    """Vérifie si le joueur a épuisé toutes ses vies."""
    # Retourne True si vies <= 0 (partie perdue).
    return vies <= 0

def jouer():
    """Boucle principale du jeu (la partie non-testée directement)."""
    print("--- Bienvenue au Jeu du Nombre Secret ---")
    # Initialisation: nombre entre 1 et 100, 5 vies.
    secret = random.randint(1, 100)
    vies = 5
    
    # Boucle de jeu: continue tant que le joueur a des vies.
    while not est_partie_terminee(vies):
        try:
            essai = int(input(f"Il vous reste {vies} vies. Votre choix : "))
            # Appel à la fonction testable pour obtenir le feedback.
            resultat = verifier_devinette(secret, essai)
            print(resultat)
            
            # Si gagné, quitter la boucle.
            if resultat == "Gagné":
                break
            vies -= 1
        except ValueError:
            print("Erreur : Entrez un nombre valide.")
            
    # Message de fin en cas de défaite.
    if vies == 0:
        print(f"Perdu ! Le nombre était {secret}.")

if __name__ == "__main__":
    jouer()