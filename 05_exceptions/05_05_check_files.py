# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

file_name = 'integers.txt'

try:
    with open(file_name, 'r') as f:
        first_line = f.readline().strip()
        number = int(first_line)
except IOError:
    print(f"Erreur : impossible d'ouvrir le fichier '{file_name}'.")
except ValueError:
    print(f"Erreur : '{first_line}' n'est pas un entier valide.")
else:
    result = number * 2
    print(f"Premier nombre : {number} → multiplié par 2 = {result}")
