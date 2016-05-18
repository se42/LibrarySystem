import datetime

from Ledger import Ledger
from Order import Order

class Patron:
	"""docstring for Patron"""

	_card_numbers = [100]

	@classmethod
	def _next_card_number(cls):
		next_num = max(cls._card_numbers) + 1
		cls._card_numbers.append(next_num)
		return next_num

	def __init__(self, name, date_f=datetime.date.today):
		self.name = name
		self.address = None
		self.phone_number = None
		self.birthday = None
		self.card_number = self._next_card_number()
		self.card_issued = date_f()
		self.orders = []
		self.ledger = Ledger(self)

		self.commands = ['new_order', 'display']

	@property
	def age(self):
		years = datetime.date.today().year - self.birthday.year
		months = datetime.date.today().month - self.birthday.month
		days = datetime.date.today().day - self.birthday.day
		if months > 0:
			return years
		elif months == 0:
			if days >= 0:
				return years
			else:
				return years - 1
		elif months < 0:
			return years - 1

	def new_order(self, *args, **kwargs):
		self.orders.append(Order(self))

	def display(self, *args, **kwargs):
		print('Patron Number:', self.card_number)
		print('\tName:', self.name)
		print('\tBirthday:', self.birthday)
		print('\tAge:', self.age)
		print('\tDate Joined:', self.card_issued)
		print('\tOrders:', self.orders)

