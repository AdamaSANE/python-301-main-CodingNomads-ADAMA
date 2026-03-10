# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.


class Vehicle:
	"""Base class for vehicles."""

	def __init__(self, brand, year):
		self.brand = brand
		self.year = year

	def start_engine(self):
		print(f"{self.brand} engine started.")

	def describe(self):
		return f"{self.brand} ({self.year})"


class Truck(Vehicle):
	"""Child class of Vehicle for trucks."""

	def __init__(self, brand, year, max_payload_kg):
		super().__init__(brand, year)
		self.max_payload_kg = max_payload_kg

	def load(self, kg):
		if kg <= self.max_payload_kg:
			print(f"Loaded {kg} kg.")
		else:
			print(f"Too heavy: max payload is {self.max_payload_kg} kg.")

	def describe(self):
		return f"Truck: {self.brand} ({self.year}), payload {self.max_payload_kg} kg"


class PickupTruck(Truck):
	"""Grandchild class: Vehicle -> Truck -> PickupTruck."""

	def __init__(self, brand, year, max_payload_kg, cabin_type):
		super().__init__(brand, year, max_payload_kg)
		self.cabin_type = cabin_type

	def tow(self):
		print(f"{self.brand} pickup is towing with a {self.cabin_type} cabin.")

	def describe(self):
		return (
			f"Pickup: {self.brand} ({self.year}), {self.cabin_type} cabin, "
			f"payload {self.max_payload_kg} kg"
		)


class Motorcycle(Vehicle):
	"""Another child class of Vehicle."""

	def __init__(self, brand, year, has_sidecar=False):
		super().__init__(brand, year)
		self.has_sidecar = has_sidecar

	def wheelie(self):
		print(f"{self.brand} does a wheelie!")

	def describe(self):
		sidecar_text = "with sidecar" if self.has_sidecar else "without sidecar"
		return f"Motorcycle: {self.brand} ({self.year}), {sidecar_text}"


if __name__ == "__main__":
	truck = Truck("Volvo", 2021, 18000)
	pickup = PickupTruck("Ford", 2024, 1200, "double")
	moto = Motorcycle("Yamaha", 2022)

	truck.start_engine()
	print(truck.describe())
	truck.load(15000)

	pickup.start_engine()
	print(pickup.describe())
	pickup.load(900)
	pickup.tow()

	moto.start_engine()
	print(moto.describe())
	moto.wheelie()
