# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.

# Simulation d'une "base de données" sous forme de dictionnaire
database = {
    "alice": {"age": 30, "email": "alice@example.com"},
    "bob":   {"age": 25, "email": "bob@example.com"},
}

username = input("Entrez un nom d'utilisateur : ")

try:
    if username not in database:
        raise KeyError(username)
    user_data = database[username]
except KeyError as e:
    print(f"Erreur : l'utilisateur {e} n'existe pas dans la base de données.")
else:
    # Exécuté seulement si aucune exception n'a été levée
    print(f"Connexion réussie ! Données : {user_data}")
