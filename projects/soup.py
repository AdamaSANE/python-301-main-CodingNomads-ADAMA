import webbrowser


# ---------------------------------------------------------------------------
# Classes de base : Ingredient et Spice
# ---------------------------------------------------------------------------

class Ingredient:
    """Modelise un aliment utilise comme ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        # Affichage lisible quand on print() un ingredient.
        return f"{self.amount} x {self.name}"


class Spice(Ingredient):
    """Une epice est un ingredient avec un profil de gout."""

    def __init__(self, name, amount, taste):
        # On recupere name et amount depuis Ingredient.
        super().__init__(name, amount)
        self.taste = taste

    def __str__(self):
        return f"{self.amount}g de {self.name} ({self.taste})"


# ---------------------------------------------------------------------------
# Classe principale : Soup
# ---------------------------------------------------------------------------

class Soup:
    """
    Modelise une soupe composee d'ingredients et d'epices.

    *ingredients accepte un nombre illimite d'objets Ingredient ou Spice
    directement a l'instanciation.
    """

    def __init__(self, title, *ingredients):
        self.title = title
        # *args : on convertit le tuple en liste pour pouvoir y ajouter apres.
        self.ingredients = list(ingredients)

    def add(self, *ingredients):
        """Ajoute un ou plusieurs ingredients apres l'instanciation."""
        self.ingredients.extend(ingredients)
        for ing in ingredients:
            print(f"+ {ing.name} ajoute a '{self.title}'.")

    def cook(self):
        """Lance une recherche Google de recette avec tous les ingredients."""
        if not self.ingredients:
            print("Votre soupe est vide. Ajoutez des ingredients avec .add().")
            return

        # On construit la requete en concatenant les noms des ingredients.
        noms = [ing.name for ing in self.ingredients]
        requete = "+".join(noms)
        url = f"https://www.google.com/search?q=recette+soupe+{requete}"

        print(f"\n--- {self.title} ---")
        for ing in self.ingredients:
            # __str__ de chaque objet donne name + amount.
            print(f"  {ing}")
        print(f"\nRecherche : {url}")
        webbrowser.open(url)

    def __str__(self):
        noms = ", ".join(ing.name for ing in self.ingredients)
        return f"Soup('{self.title}' | ingredients : [{noms}])"


# ---------------------------------------------------------------------------
# Bonus : classes enfants de Soup
# ---------------------------------------------------------------------------

class CreamSoup(Soup):
    """Soupe veloutee : ajoute automatiquement de la creme a l'instanciation."""

    def __init__(self, title, *ingredients):
        super().__init__(title, *ingredients)
        # La creme est un ingredient interne de chaque soupe veloutee.
        self.ingredients.append(Ingredient("cream", "200ml"))

    def cook(self):
        print("[Veloute] Mixage en cours...")
        # On reutilise entierement le cook() de Soup.
        super().cook()


class ClearSoup(Soup):
    """Soupe claire : ajoute du bouillon et adapte le message de cuisson."""

    def __init__(self, title, *ingredients):
        super().__init__(title, *ingredients)
        self.ingredients.append(Ingredient("bouillon", "1L"))

    def cook(self):
        print("[Soupe claire] Mijotage leger...")
        super().cook()


# ---------------------------------------------------------------------------
# Demonstration
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # Creation des ingredients.
    carrot = Ingredient("carrot", 3)
    onion = Ingredient("onion", 1)
    pepper = Spice("pepper", 5, "hot")

    # *args : on passe plusieurs ingredients directement a l'instanciation.
    soup = Soup("Ma soupe maison", carrot, onion)
    soup.add(pepper)        # On peut aussi ajouter apres coup.
    print(soup)
    soup.cook()

    print()

    # Classe enfant : la creme est ajoutee automatiquement.
    zucchini = Ingredient("zucchini", 2)
    veloute = CreamSoup("Veloute de courgette", zucchini)
    print(veloute)
    veloute.cook()