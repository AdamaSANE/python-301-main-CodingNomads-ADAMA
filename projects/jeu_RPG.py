import random
import time


# ---------------------------------------------------------------------------
# Classes Héros (héritage côté joueur)
# ---------------------------------------------------------------------------

class Hero:
    """Héros de base : équilibré."""

    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.hp = 100

    def attack(self, opponent):
        """Inflige des dégâts à l'adversaire. Retourne les dégâts."""
        damage = random.randint(3, 8) + self.level
        opponent.hp -= damage
        print(f"⚔️  {self.name} attaque {opponent.name} et inflige {damage} dégâts.")
        print(f"   {opponent.name} : {max(0, opponent.hp)} PV restants.")
        return damage

    def __str__(self):
        return f"{self.name} (Niv.{self.level} | PV: {self.hp})"


class Warrior(Hero):
    """Guerrier : accumule de la rage à chaque attaque pour frapper plus fort."""

    def __init__(self, name, level):
        super().__init__(name, level)
        # Attribut propre au guerrier, absent dans Hero.
        self.rage = 0

    def attack(self, opponent):
        # La rage grandit à chaque coup et augmente les dégâts.
        self.rage += 1
        damage = random.randint(4, 10) + self.level + self.rage * 2
        opponent.hp -= damage
        print(f"⚔️  {self.name} attaque avec RAGE x{self.rage} et inflige {damage} dégâts !")
        print(f"   {opponent.name} : {max(0, opponent.hp)} PV restants.")
        return damage


class Mage(Hero):
    """Mage : sorts puissants mais mana limitée."""

    def __init__(self, name, level):
        super().__init__(name, level)
        # Attribut propre au mage, absent dans Hero.
        self.mana = 50

    def attack(self, opponent):
        if self.mana >= 10:
            self.mana -= 10
            # 30 % de chance de critique.
            critical = random.random() < 0.3
            damage = random.randint(4, 12) + self.level
            if critical:
                damage *= 2
                print(f"✨ CRITIQUE ! {self.name} lance un sort dévastateur ({self.mana} mana restant).")
            else:
                print(f"🔮 {self.name} lance un sort ({self.mana} mana restant).")
            opponent.hp -= damage
            print(f"   {opponent.name} subit {damage} dégâts. PV restants : {max(0, opponent.hp)}")
            return damage
        else:
            # Plus de mana : repli sur l'attaque physique de Hero.
            print(f"💨 {self.name} n'a plus de mana ! Attaque de base.")
            return super().attack(opponent)


# ---------------------------------------------------------------------------
# Classes Adversaire (héritage côté ennemi)
# ---------------------------------------------------------------------------

class Opponent:
    """Adversaire de base : niveau et PV proportionnels au niveau."""

    def __init__(self, name, level):
        self.name = name
        self.level = level
        # Les PV augmentent avec le niveau.
        self.hp = 20 + level * 4

    def attack(self, hero):
        """Contre-attaque le héros. Retourne les dégâts infligés."""
        damage = random.randint(2, 5) + self.level // 2
        hero.hp -= damage
        print(f"💥 {self.name} riposte et inflige {damage} dégâts à {hero.name}.")
        print(f"   {hero.name} : {max(0, hero.hp)} PV restants.")
        return damage

    def __str__(self):
        return f"{self.name} (Niv.{self.level} | PV: {self.hp})"


class WeakOpponent(Opponent):
    """Adversaire faible : attaque légère, rate souvent."""

    def __init__(self, name, level):
        # Le niveau est plafonné à 3 pour garantir qu'il reste faible.
        super().__init__(name, min(level, 3))

    def attack(self, hero):
        # 40 % de chance de rater complètement.
        if random.random() < 0.4:
            print(f"😅 {self.name} trébuche et rate son attaque !")
            return 0
        damage = random.randint(1, 3)
        hero.hp -= damage
        print(f"🐛 {self.name} griffe faiblement {hero.name} pour {damage} dégâts.")
        print(f"   {hero.name} : {max(0, hero.hp)} PV restants.")
        return damage


class BossOpponent(Opponent):
    """Boss final : énormes PV + un pouvoir spécial déclenché à mi-vie."""

    def __init__(self, name, level, special_power):
        super().__init__(name, level)
        # Attribut propre au Boss, absent dans Opponent.
        self.special_power = special_power
        # Le boss a beaucoup plus de PV qu'un Opponent normal.
        self.hp = 80 + level * 6
        self._max_hp = self.hp
        # Le pouvoir spécial ne peut s'utiliser qu'une seule fois.
        self._special_used = False

    def attack(self, hero):
        # Déclenche le pouvoir spécial quand les PV tombent sous 50 %.
        if not self._special_used and self.hp <= self._max_hp // 2:
            self._special_used = True
            damage = random.randint(18, 28) + self.level
            hero.hp -= damage
            print(f"💀 {self.name} active '{self.special_power}' et inflige {damage} dégâts !!!")
            print(f"   {hero.name} : {max(0, hero.hp)} PV restants.")
            return damage
        return super().attack(hero)

    def __str__(self):
        return (f"[BOSS] {self.name} (Niv.{self.level} | PV: {self.hp})"
                f" — Pouvoir: {self.special_power}")


# ---------------------------------------------------------------------------
# Sélection du héros
# ---------------------------------------------------------------------------

def choose_hero():
    """Permet au joueur de choisir sa classe de héros."""
    print("=== CHOISISSEZ VOTRE CLASSE ===")
    print("1. Guerrier  (rage croissante à chaque attaque)")
    print("2. Mage      (sorts critiques, mana limitée)")
    print("3. Héros     (équilibré)")
    choix = input("Votre choix (1/2/3) : ").strip()
    name = input("Votre nom de héros : ").strip() or "Adama"
    if choix == "1":
        return Warrior(name, 5)
    elif choix == "2":
        return Mage(name, 5)
    else:
        return Hero(name, 5)


# ---------------------------------------------------------------------------
# Boucle de jeu
# ---------------------------------------------------------------------------

def combat_round(hero, opponent):
    """Un round : le héros attaque, puis l'adversaire (s'il survit) riposte."""
    hero.attack(opponent)
    if opponent.hp > 0:
        opponent.attack(hero)


def game_loop():
    hero = choose_hero()
    print(f"\nBienvenue, {hero} ! Bonne chance.\n")

    ennemis = [
        WeakOpponent("Bug Mineur", 2),
        WeakOpponent("Glitch Aléatoire", 3),
        Opponent("Serveur HS", 6),
        BossOpponent("Paywall Ultime", 12, "Subscription Lock 💸"),
    ]

    while ennemis and hero.hp > 0:
        current_opp = ennemis[0]
        print(f"\n{'='*45}")
        print(f"Ennemi  : {current_opp}")
        print(f"Vous    : {hero}")
        print(f"{'='*45}")
        choix = input("(a)ttaquer | (s)'enfuir | (q)uitter : ").lower().strip()

        if choix == 'a':
            combat_round(hero, current_opp)

            if current_opp.hp <= 0:
                print(f"\n✅ {current_opp.name} est vaincu !")
                ennemis.pop(0)
                hero.level += 1
                print(f"🆙 {hero.name} passe au niveau {hero.level} !")

            if hero.hp <= 0:
                print(f"\n☠️  {hero.name} est tombé au combat...")
                break

        elif choix == 's':
            print("🏃 Vous fuyez... les ennemis se réorganisent.")
            random.shuffle(ennemis)

        elif choix == 'q':
            print("👋 Abandon de la partie.")
            return

        else:
            print("Commande invalide. (a), (s) ou (q).")

    if not ennemis and hero.hp > 0:
        print("\n🎉 Félicitations ! Tous les obstacles sont vaincus !")
    elif hero.hp <= 0:
        print("\n💀 Game Over. Réessayez !")


if __name__ == "__main__":
    game_loop()