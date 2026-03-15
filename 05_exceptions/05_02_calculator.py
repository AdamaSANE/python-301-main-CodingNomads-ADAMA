# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.

try:
    a = float(input("Entrez le dividende : "))
    b = float(input("Entrez le diviseur : "))
    result = a / b
    print(f"{a} / {b} = {result}")
except ValueError:
    print("Erreur : veuillez entrer un nombre valide.")
except ZeroDivisionError:
    print("Erreur : la division par zéro est impossible.")
