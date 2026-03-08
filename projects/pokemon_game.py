# Build a very basic Pokémon class that allows you to simulate battles
# in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#
# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `grass`
# - Implement a `battle()` method based on rock-paper-scissors that
#   decides who wins based only on the `primary_type`:
#       water > fire > grass > water
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`
# - If you call the `feed()` method on a Pokemon, they regain some `hp`


class Pokemon:
    def __init__(self, name, primary_type, max_hp):
        self.name = name
        self.primary_type = primary_type.lower()
        self.max_hp = max_hp
        self.hp = max_hp

    def feed(self):
        """Redonne 20 HP au Pokémon sans dépasser son max_hp."""
        if self.hp < self.max_hp:
            self.hp = min(self.hp + 20, self.max_hp)
            print(f"🍴 {self.name} a bien mangé ! HP actuels : {self.hp}")
        else:
            print(f"✨ {self.name} n'a pas faim, ses HP sont déjà au maximum.")

    def battle(self, other):
        """Détermine le vainqueur selon le triangle des types : Eau > Feu > Plante > Eau."""
        print(f"\n--- COMBAT : {self.name} ({self.primary_type}) VS {other.name} ({other.primary_type}) ---")

        # Cas d'égalité
        if self.primary_type == other.primary_type:
            print("🤝 Les deux Pokémon sont du même type. C'est un match nul !")
            return

        # Définition des règles de victoire (Gagnant : Perdant)
        rules = {
            "water": "fire",
            "fire": "grass",
            "grass": "water"
        }

        # Vérification du gagnant
        if rules[self.primary_type] == other.primary_type:
            # self gagne
            other.hp -= 30
            print(f"🏆 {self.name} gagne ! {other.name} est K.O. partiel (-30 HP).")
        else:
            # other gagne
            self.hp -= 30
            print(f"❌ {self.name} a perdu... Il perd 30 HP.")

    def __str__(self):
        return f"{self.name} | Type: {self.primary_type} | HP: {self.hp}/{self.max_hp}"

# --- Test du simulateur ---
if __name__ == "__main__":
    carapuce = Pokemon("Carapuce", "water", 100)
    salameche = Pokemon("Salameche", "fire", 100)

    carapuce.battle(salameche)
    print(salameche) # On vérifie la baisse de HP

    salameche.feed()
    print(salameche) # On vérifie la récupération