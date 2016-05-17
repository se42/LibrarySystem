import datetime


class Ledger:
	"""docstring for Ledger"""
	def __init__(self, patron):
		self.patron = patron
		self.ledger_number = 'LDG-' + str(self.patron.card_number)

		self._next_line_num = 1

	def get_balance(self):
		return '$50'

	def make_line_item(self, chk_line_item):
		# called by the CheckoutLineItem class upon instantiation
		# to ensure CheckoutLineItem is linked to a LedgerLineItem
		self._next_line_num += 1
		return LedgerLineItem(self, _next_line_num, chk_line_item)


class LedgerLineItem:
	"""docstring for LedgerLineItem"""
	def __init__(self, ledger, line_number, chk_line_item):
		self.ledger = ledger
		self.line_number = line_number
		self.checkout_line_item = chk_line_item
		self.amount_paid = 0

		self._fine_amount = 0
		self._outstanding_balance = 0

	@property
	def outstanding_balance(self):
		self.outstanding_balance = self.fine_amount - self.amount_paid
		return self._outstanding_balance

	@outstanding_balance.setter
	def outstanding_balance(self, value):
		self._outstanding_balance = value

	@property
	def fine_amount(self):
		self.fine_amount = self._calculate_fine()
		return self._fine_amount

	@fine_amount.setter
	def fine_amount(self, value):
		self._fine_amount = value

	def _calculate_fine(self):
		days = (datetime.date.today() - self.checkout_line_item.due_date).days
		if days < 1:
			return 0
		else:
			max_fine = self.checkout_line_item.item.title.value
			calc_fine = days * 0.10
			return min([max_fine, calc_fine])
	
		
