# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".

import os


class PrinceException(Exception):
	"""Raised when the word 'Prince' appears in the first 100 chars of a book."""


books_dir = os.path.join(os.path.dirname(__file__), "books")
book_files = [
	"war_and_peace.txt",
	"pride_and_prejudice.txt",
	"crime_and_punishment.txt",
]

for book in book_files:
	path = os.path.join(books_dir, book)
	try:
		with open(path, "r", encoding="utf-8") as f:
			first_100 = f.read(100)

		if "Prince" in first_100:
			raise PrinceException(f"'Prince' trouvé dans {book} (100 premiers caractères).")

		print(f"OK: pas de 'Prince' au début de {book}.")
	except PrinceException as e:
		print(f"PrinceException: {e}")
	except IOError as e:
		print(f"Erreur fichier pour {book}: {e}")
