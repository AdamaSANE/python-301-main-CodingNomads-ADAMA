def tagify(nom_balise):
    # Étage 1 : La Fabrique (reçoit "p", "div", "h1", etc.)
    def decorateur(fonction_initiale):
        # Étage 2 : Le Décorateur (reçoit la fonction greet ou lorem)
        def wrapper(*args, **kwargs):
            # Étage 3 : Le Wrapper (reçoit les arguments comme "Bessy")
            
            # 1. On récupère le texte généré par la fonction d'origine
            resultat_texte = fonction_initiale(*args, **kwargs)
            
            # 2. On l'emballe dans les balises HTML
            return f"<{nom_balise}>{resultat_texte}</{nom_balise}>"
            
        return wrapper
    return decorateur

# --- Tests du projet ---

@tagify("p")
def greet(name):
    return f"Hello, {name}"

@tagify("div")
def lorem():
    return "Lorem ipsum dolor sit amet, ..."

print(greet("Bessy"))  # OUTPUT: <p>Hello, Bessy</p>
print(lorem())         # OUTPUT: <div>Lorem ipsum dolor sit amet, ...</div>