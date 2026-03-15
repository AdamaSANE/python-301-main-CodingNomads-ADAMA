# class AgeError(Exception):
#     def __init__(self, age):
#         self.age = age


# age = int(input("Age: "))

# try:
#     if age < 0:
#         raise AgeError(age)
# except AgeError as ae:
#     print(f"Pssst... This might be a miracle. They say they're {ae.age} years old.")

# class AgeError(Exception):
#     def __init__(self, age):
#         self.age = age
#         self.message = f"You'll be born in {abs(self.age)} years."


# age = int(input("Age: "))

# try:
#     if age < 0:
#         raise AgeError(age)
# except AgeError as ae:
#     print(ae.message)


# animals_of_africa = {
#     "aardvark": "a nocturnal badger-sized burrowing mammal",
#     "zebra": "a wild horse with black-and-white stripes"
#     }

# animal = input("Animal to look up: ")

# try:
#     print(animals_of_africa[animal])
# except KeyError:
#     print("This animal is not in the database")
# animals_of_africa = {
#     "aardvark": "a nocturnal badger-sized burrowing mammal",
#     "zebra": "a wild horse with black-and-white stripes"
#     }

# animal = input("Animal to look up: ")

# print(animals_of_africa.get(animal, "This animal is not in the database"))
