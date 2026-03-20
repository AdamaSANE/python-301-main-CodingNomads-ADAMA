import unittest
import game


# Suite de tests unitaires pour la logique du jeu de devinette.
class TestJeuNombre(unittest.TestCase):

    def setUp(self):
        """Configuration initiale avant chaque test."""
        self.nombre_secret = 50

    def test_devinette_trop_basse(self):
        """Vérifie que le jeu détecte quand c'est trop bas."""
        # 10 est inférieur au nombre secret (50).
        resultat = game.verifier_devinette(self.nombre_secret, 10)
        self.assertEqual(resultat, "Trop bas")

    def test_devinette_trop_haute(self):
        """Vérifie que le jeu détecte quand c'est trop haut."""
        # 90 est supérieur au nombre secret (50).
        resultat = game.verifier_devinette(self.nombre_secret, 90)
        self.assertEqual(resultat, "Trop haut")

    def test_devinette_gagnante(self):
        """Vérifie la détection de la victoire."""
        # Même valeur que le nombre secret: le joueur gagne.
        resultat = game.verifier_devinette(self.nombre_secret, 50)
        self.assertEqual(resultat, "Gagné")

    def test_gestion_vies_fin_partie(self):
        """Vérifie que 0 vie signifie bien la fin de partie."""
        # Frontière métier: 0 vie => terminé, 1 vie => continue.
        self.assertTrue(game.est_partie_terminee(0))
        self.assertFalse(game.est_partie_terminee(1))

    def test_erreur_type_donnee(self):
        """Vérifie que le code lève une exception si on n'envoie pas un entier."""
        # Validation d'entrée: une chaîne doit lever TypeError.
        with self.assertRaises(TypeError):
            game.verifier_devinette(50, "texte")

    def tearDown(self):
        """Nettoyage après le test (optionnel ici)."""
        pass

if __name__ == '__main__':
    unittest.main()