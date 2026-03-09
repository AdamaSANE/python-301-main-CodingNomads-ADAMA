import random
import time

class Hero:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.hp = 100

    def attack(self, opponent):
        print(f"⚔️ {self.name} attaque {opponent.name} !")
        
        # Simulation d'un jet de dé (1 à 6) ajouté au niveau
        hero_roll = random.randint(1, 6) + self.level
        opp_roll = random.randint(1, 6) + opponent.level
        
        print(f"Jet de {self.name} : {hero_roll} | Jet de {opponent.name} : {opp_roll}")

        if hero_roll >= opp_roll:
            print(f"✅ Victoire ! {opponent.name} est vaincu.")
            return True
        else:
            print(f"❌ Défaite... {self.name} doit récupérer.")
            return False

class Opponent:
    def __init__(self, name, level):
        self.name = name
        self.level = level

# --- Initialisation du Jeu ---
mon_heros = Hero("Adama l'Admin", 10)
ennemis = [
    Opponent("Bug Critique", 5),
    Opponent("Serveur HS", 12),
    Opponent("Paywall Géant", 8)
]

def game_loop():
    while ennemis and mon_heros.hp > 0:
        current_opp = ennemis[0]
        print(f"\nVous faites face à : {current_opp.name} (Niveau {current_opp.level})")
        choix = input("Voulez-vous (a)ttaquer ou (s)'enfuir ? ").lower()

        if choix == 'a':
            success = mon_heros.attack(current_opp)
            if success:
                ennemis.pop(0) # On retire l'adversaire vaincu
                mon_heros.level += 1 # Le héros progresse
                print(f"Bravo ! Vous passez au niveau {mon_heros.level}")
            else:
                print("⏳ Vous êtes essoufflé... attente de 3 secondes.")
                time.sleep(3) # Conséquence de la défaite
        elif choix == 's':
            print("🏃 Vous fuyez courageusement vers un autre serveur.")
            random.shuffle(ennemis) # On change l'ordre des ennemis
        else:
            print("Commande invalide.")

    if not ennemis:
        print("\n🎉 Félicitations ! Tous les obstacles informatiques sont levés !")

if __name__ == "__main__":
    game_loop()