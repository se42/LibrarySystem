import datetime

from Ledger import Ledger
from Order import Order

class Patron:
	"""docstring for Patron"""

	_card_numbers = [100]

	def __init__(self, name, date_f=datetime.date.today):
		self.name = name
		self.address = None
		self.phone_number = None
		self.birthday = None
		self.card_number = self._next_card_number()
		self.card_issued = date_f()
		self.orders = []
		self.ledger = Ledger(self)

	@classmethod
	def _next_card_number(cls):
		next_num = max(cls._card_numbers) + 1
		cls._card_numbers.append(next_num)
		return next_num

	def new_order(self):
		self.orders.append(Order(self))


