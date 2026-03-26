"""Simple implementation of a FIFO queue (First In, First Out)."""


class Queue:
	"""Custom queue implementation using a Python list as storage."""

	def __init__(self):
		# Front of queue is index 0, rear is the end of the list.
		self._items = []

	def enqueue(self, item):
		"""Add an item to the rear of the queue."""
		self._items.append(item)

	def dequeue(self):
		"""Remove and return the front item.

		Raises:
			IndexError: If the queue is empty.
		"""
		if self.is_empty():
			raise IndexError("Cannot dequeue from an empty queue.")
		return self._items.pop(0)

	def peek(self):
		"""Return the front item without removing it.

		Raises:
			IndexError: If the queue is empty.
		"""
		if self.is_empty():
			raise IndexError("Cannot peek an empty queue.")
		return self._items[0]

	def is_empty(self):
		"""Return True when the queue contains no items."""
		return len(self._items) == 0

	def size(self):
		"""Return the number of items in the queue."""
		return len(self._items)

	def __repr__(self):
		return f"Queue({self._items})"


if __name__ == "__main__":
	# Small usage demo: add 3 elements, inspect front, then dequeue.
	queue = Queue()
	queue.enqueue("first")
	queue.enqueue("second")
	queue.enqueue("third")

	print("Current queue:", queue)
	print("Front item:", queue.peek())
	print("Dequeued item:", queue.dequeue())
	print("Queue size:", queue.size())
	print("Is empty:", queue.is_empty())
