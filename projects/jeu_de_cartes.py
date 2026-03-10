"""
Jeu de cartes en ligne de commande — La Bataille
=================================================
Classes :
  Card    → une seule carte (valeur + couleur)
  Deck    → un jeu de 52 cartes mélangées
  Hand    → la main d'un joueur (hérite de Deck)
  Battle  → coordonne la partie entre deux joueurs
"""

import random


# ---------------------------------------------------------------------------
# Classe Card : modélise une carte individuelle
# ---------------------------------------------------------------------------

class Card:
    """Représente une carte à jouer (ex : As de Cœur)."""

    # Valeurs disponibles dans un jeu standard.
    VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
              "J", "Q", "K", "A"]

    # Couleurs disponibles.
    SUITS  = ["♣ Trèfle", "♦ Carreau", "♥ Cœur", "♠ Pique"]

    def __init__(self, value, suit):
        self.value = value
        self.suit  = suit
        # Force numérique : position dans VALUES (0 = 2, 12 = As).
        self.strength = Card.VALUES.index(value)

    def __str__(self):
        return f"{self.value} de {self.suit}"

    def __repr__(self):
        return f"Card('{self.value}', '{self.suit}')"

    # Opérateurs de comparaison basés sur la force de la carte.
    def __lt__(self, other):
        return self.strength < other.strength

    def __gt__(self, other):
        return self.strength > other.strength

    def __eq__(self, other):
        return self.strength == other.strength


# ---------------------------------------------------------------------------
# Classe Deck : jeu complet de 52 cartes
# ---------------------------------------------------------------------------

class Deck:
    """Représente un jeu de 52 cartes."""

    def __init__(self):
        # Génère toutes les combinaisons valeur × couleur.
        self.cards = [Card(v, s) for s in Card.SUITS for v in Card.VALUES]

    def shuffle(self):
        """Mélange le jeu en place."""
        random.shuffle(self.cards)
        print("🔀 Jeu mélangé.")

    def draw(self):
        """Pioche la carte du dessus. Lève une erreur si le jeu est vide."""
        if not self.cards:
            raise IndexError("Le jeu est vide !")
        return self.cards.pop(0)

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return f"Deck ({len(self)} cartes restantes)"


# ---------------------------------------------------------------------------
# Classe Hand : main d'un joueur (hérite de Deck)
# ---------------------------------------------------------------------------

class Hand(Deck):
    """
    La main d'un joueur.
    Hérite de Deck mais part d'une liste vide (pas les 52 cartes).
    """

    def __init__(self, owner):
        # On ne veut PAS les 52 cartes ici : on part vide.
        self.cards = []
        self.owner = owner

    def receive(self, card):
        """Ajoute une carte à la main."""
        self.cards.append(card)

    def play_top(self):
        """Joue la première carte de la main."""
        if not self.cards:
            return None
        return self.cards.pop(0)

    def __str__(self):
        return f"Main de {self.owner} ({len(self)} cartes)"


# ---------------------------------------------------------------------------
# Classe Battle : gère une partie de La Bataille
# ---------------------------------------------------------------------------

class Battle:
    """
    La Bataille : deux joueurs retournent chacun une carte,
    le plus fort gagne les deux. Premier à court de cartes a perdu.
    """

    def __init__(self, player1_name, player2_name):
        # On prépare et mélange un jeu neuf.
        deck = Deck()
        deck.shuffle()

        self.hand1 = Hand(player1_name)
        self.hand2 = Hand(player2_name)

        # Distribution : chaque joueur reçoit 26 cartes.
        for _ in range(26):
            self.hand1.receive(deck.draw())
            self.hand2.receive(deck.draw())

        print(f"\n🃏 Partie entre {player1_name} et {player2_name} — chacun reçoit 26 cartes.\n")

    def play_round(self):
        """Joue un round et retourne True si la partie doit continuer."""
        if not self.hand1.cards or not self.hand2.cards:
            return False

        c1 = self.hand1.play_top()
        c2 = self.hand2.play_top()

        print(f"  {self.hand1.owner:15} → {c1}")
        print(f"  {self.hand2.owner:15} → {c2}")

        if c1 > c2:
            # Le gagnant récupère les deux cartes en bas de sa main.
            self.hand1.receive(c1)
            self.hand1.receive(c2)
            print(f"  ✅ {self.hand1.owner} remporte ce round ! "
                  f"({len(self.hand1)} vs {len(self.hand2)})")
        elif c2 > c1:
            self.hand2.receive(c2)
            self.hand2.receive(c1)
            print(f"  ✅ {self.hand2.owner} remporte ce round ! "
                  f"({len(self.hand1)} vs {len(self.hand2)})")
        else:
            # Égalité : chaque joueur reprend sa carte.
            self.hand1.receive(c1)
            self.hand2.receive(c2)
            print("  🤝 Égalité ! Chacun reprend sa carte.")

        return True

    def winner(self):
        """Retourne le nom du gagnant, ou None si la partie n'est pas terminée."""
        if not self.hand1.cards:
            return self.hand2.owner
        if not self.hand2.cards:
            return self.hand1.owner
        return None

    def play(self, max_rounds=100):
        """Lance la partie jusqu'à ce qu'un joueur soit à cours de cartes."""
        round_num = 0
        while self.hand1.cards and self.hand2.cards and round_num < max_rounds:
            round_num += 1
            print(f"\n--- Round {round_num} ---")
            input("Appuyez sur Entrée pour jouer... ")
            self.play_round()

        w = self.winner()
        print(f"\n{'='*40}")
        if w:
            print(f"🏆 Victoire de {w} !")
        else:
            print(f"⏱️  Limite de {max_rounds} rounds atteinte — match nul !")
        print(f"{'='*40}")


# ---------------------------------------------------------------------------
# Lancement
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=== JEU DE LA BATAILLE ===")
    p1 = input("Nom du joueur 1 : ").strip() or "Alice"
    p2 = input("Nom du joueur 2 : ").strip() or "Bob"
    game = Battle(p1, p2)
    game.play()
