# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?

import os

books_dir = os.path.join(os.path.dirname(__file__), 'books')

# 1) Lire tout le contenu de war_and_peace.txt
with open(os.path.join(books_dir, 'war_and_peace.txt'), 'r', encoding='utf-8') as f:
    war_and_peace_content = f.read()

print(f"'War and Peace' lu ({len(war_and_peace_content)} caractères).")

# 2) Écraser crime_and_punishment.txt avec une chaîne vide
with open(os.path.join(books_dir, 'crime_and_punishment.txt'), 'w', encoding='utf-8') as f:
    f.write('')

print("'Crime and Punishment' vidé.")

# 3) Parcourir les trois fichiers et afficher le premier caractère de chacun
# Exception attendue : ValueError ("read from empty file" / "I/O operation on empty file")
# ou simplement une chaîne vide — on gère les deux cas.
book_files = [
    'war_and_peace.txt',
    'pride_and_prejudice.txt',
    'crime_and_punishment.txt',
]

for book in book_files:
    path = os.path.join(books_dir, book)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            first_char = f.read(1)
            if not first_char:
                raise ValueError(f"Le fichier '{book}' est vide.")
            print(f"{book} → premier caractère : {repr(first_char)}")
    except IOError as e:
        print(f"Erreur d'accès au fichier '{book}' : {e}")
    except ValueError as e:
        print(f"Erreur de contenu : {e}")
