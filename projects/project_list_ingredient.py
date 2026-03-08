import webbrowser

class Ingredient:
    """Modèle un ingrédient capable de rechercher sa propre biographie sur le web."""
    
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def get_info(self):
        """Construit l'URL Wikipédia et l'ouvre dans le navigateur."""
        # Wikipédia utilise souvent une majuscule pour les titres de pages
        formatted_name = self.name.capitalize()
        base_url = "https://en.wikipedia.org/wiki/"
        full_url = base_url + formatted_name
        
        print(f"Recherche d'informations pour : {formatted_name}...")
        webbrowser.open(full_url)

    def __str__(self):
        return f"{self.amount} de {self.name}"

# --- Test du Projet ---

if __name__ == "__main__":
    # Création d'une instance
    mon_ingredient = Ingredient("carrot", "500g")
    
    # Affichage de l'objet
    print(mon_ingredient)
    
    # Lancement de la recherche automatique
    mon_ingredient.get_info()