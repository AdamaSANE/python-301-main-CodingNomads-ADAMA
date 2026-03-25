# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.

import time
from functools import wraps


def log_execution_time(func):
	# wraps preserve le nom et la docstring de la fonction originale.
	@wraps(func)
	def wrapper(*args, **kwargs):
		# perf_counter donne une mesure precise pour calculer une duree.
		start_time = time.perf_counter()

		# On execute la fonction originale avec ses arguments.
		result = func(*args, **kwargs)

		# On mesure le temps de fin puis on calcule la duree totale.
		end_time = time.perf_counter()
		elapsed = end_time - start_time

		# On affiche un message de logging lisible dans la console.
		print(f"{func.__name__} completed in {elapsed:.6f} seconds")

		# On retourne le resultat initial pour ne pas changer le comportement.
		return result

	return wrapper


# Exemple d'utilisation du decorateur de timing.
@log_execution_time
def process_data():
	# sleep simule un traitement un peu long.
	time.sleep(0.5)
	return "Processing done"


# L'appel affiche le resultat puis le temps d'execution.
print(process_data())
