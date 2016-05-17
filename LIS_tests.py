import datetime
import unittest

from Ledger import Ledger
from Patron import Patron


class TestPatron(unittest.TestCase):

	def setUp(self):
		self.last_number = max(Patron._card_numbers)
		self.expected_patron_number = self.last_number + 1
		self.p = Patron('Scott', date_f=lambda: datetime.date(2016, 1, 1))

	def test_init(self):
		self.assertEqual(self.p.name, 'Scott')
		self.assertEqual(self.p.address, None)
		self.assertEqual(self.p.phone_number, None)
		self.assertEqual(self.p.birthday, None)
		self.assertEqual(self.p.card_number, self.expected_patron_number)
		self.assertEqual(self.p.card_issued, datetime.date(2016, 1, 1))
		self.assertEqual(self.p.orders, [])
		self.assertTrue(isinstance(self.p.ledger, Ledger))
		self.assertEqual(self.p.ledger.patron, self.p)
		self.assertEqual(self.p.ledger.ledger_number, 'LDG-' + str(self.p.card_number))

	def test_next_card_number(self):
		first = max(Patron._card_numbers)
		next_num = Patron._next_card_number()
		next_next_num = Patron._next_card_number()
		self.assertEqual(next_num, first + 1)
		self.assertEqual(next_next_num, first + 2)
		self.assertEqual(max(Patron._card_numbers), next_next_num)
		self.assertTrue(first in Patron._card_numbers)
		self.assertTrue(next_num in Patron._card_numbers)
		self.assertTrue(next_next_num in Patron._card_numbers)




class TestLedger(unittest.TestCase):

	def setUp(self):
		self.p = Patron('Scott', date_f=lambda: datetime.date(2016, 1, 1))
		self.ldg = self.p.ledger # Ledger object created during Patron __init__

	def test_init(self):
		self.assertEqual(self.ldg.patron, self.p)
		self.assertEqual(self.ldg.ledger_number, 'LDG-' + str(self.p.card_number))




if __name__ == '__main__':
	unittest.main()
