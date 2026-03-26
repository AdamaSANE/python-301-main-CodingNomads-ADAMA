"""Simple implementation of a LIFO stack (Last In, First Out)."""


class Stack:
	"""Custom stack implementation using a Python list as storage."""

	def __init__(self):
		# Internal list: the end of the list is the top of the stack.
		self._items = []

	def push(self, item):
		"""Add an item to the top of the stack."""
		self._items.append(item)

	def pop(self):
		"""Remove and return the top item.

		Raises:
			IndexError: If the stack is empty.
		"""
		if self.is_empty():
			raise IndexError("Cannot pop from an empty stack.")
		return self._items.pop()

	def peek(self):
		"""Return the top item without removing it.

		Raises:
			IndexError: If the stack is empty.
		"""
		if self.is_empty():
			raise IndexError("Cannot peek an empty stack.")
		return self._items[-1]

	def is_empty(self):
		"""Return True when the stack contains no items."""
		return len(self._items) == 0

	def size(self):
		"""Return the number of items in the stack."""
		return len(self._items)

	def __repr__(self):
		return f"Stack({self._items})"


if __name__ == "__main__":
	# Small usage demo: push 3 elements, then inspect/pop the top.
	stack = Stack()
	stack.push("book")
	stack.push("notebook")
	stack.push("laptop")

	print("Current stack:", stack)
	print("Top item:", stack.peek())
	print("Popped item:", stack.pop())
	print("Stack size:", stack.size())
	print("Is empty:", stack.is_empty())
