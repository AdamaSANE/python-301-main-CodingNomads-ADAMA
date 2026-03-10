# CLASSES AND INHERITANCE
# =======================
# 1) Define an empty `Movie()` class.
# 2) Add a dunder init method that takes two arguments `year` and `title`
# 3) Create a sub-class called `RomCom()` that inherits from the `Movie()` class
# 4) Create another sub-class of the `Movie()` class called `ActionMovie()`
#     that overwrites the dunder init method of `Movie()` and adds another
#     instance variable called `pg` that is set by default to the number `13`.
# 5) Practice planning out and flushing out these classes even more.
#     Take notes in your notebook. What other attributes could a `Movie()` class
#     contain? What methods? What should the child classes inherit as-is or overwrite?


class Movie:
	"""Base class for all movie types."""

	def __init__(self, year, title):
		self.year = year
		self.title = title

	def __str__(self):
		return f"{self.title} ({self.year})"


class RomCom(Movie):
	"""Romantic comedy movie."""

	def recommend_for_date_night(self):
		print(f"{self.title} is a great date-night choice.")


class ActionMovie(Movie):
	"""Action movie with a default PG rating of 13."""

	def __init__(self, year, title, pg=13):
		super().__init__(year, title)
		self.pg = pg

	def __str__(self):
		return f"{self.title} ({self.year}) - PG-{self.pg}"


if __name__ == "__main__":
	romcom = RomCom(2003, "Love Actually")
	action = ActionMovie(2015, "Mad Max: Fury Road")

	print(romcom)
	romcom.recommend_for_date_night()

	print(action)
