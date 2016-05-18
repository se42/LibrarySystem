import datetime

from Ledger import LedgerLineItem


class Order:
	"""docstring for Order"""

	_order_numbers = [10000]

	@classmethod
	def _next_order_number(cls):
		next_num = max(cls._order_numbers) + 1
		cls._order_numbers.append(next_num)
		return next_num

	def __init__(self, patron, date_f=datetime.date.today):
		self.patron = patron
		self.order_date = date_f()
		self.order_number = self._next_order_number()
		self.line_items = []

		self._next_line_number = 1

	def new_checkout(self):
		if self.checkout_approval():
			checkout = Checkout(self, self._next_line_number)
			self._next_line_number += 1
			self.line_items.append(checkout)
			return checkout
		else:
			return None

	def new_request(self):
		request = Request(self, self._next_line_number)
		self._next_line_number += 1
		self.line_items.append(request)
		return request

	def checkout_approval(self):
		# return True if approved; return False if not approved
		return True


class LineItem:
	"""docstring for LineItem"""
	def __init__(self, order, line_number):
		self.order = order
		self.line_number = line_number


class Checkout(LineItem):
	"""docstring for Checkout"""
	def __init__(self, *args, **kwargs):
		super(Checkout, self).__init__(*args, **kwargs)
		self.item = None
		self.due_date = None
		self.date_returned = None
		self.renewed = False
		self.ledger_line_item = self.order.patron.ledger.make_line_item(self)

	def is_overdue(self):
		return datetime.date.today() > self.due_date

	def renew(self):
		# must renew before due_date
		# can only renew for 1 week
		# cannot renew if there is an outstanding request for the item
		pass


class Request(LineItem):
	"""docstring for Request"""
	def __init__(self, *args, **kwargs):
		super(Request, self).__init__(*args, **kwargs)
		self.title = None
		self.request_by = None
		
		
		
		
