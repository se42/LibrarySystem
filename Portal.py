import datetime
import sys

import Item
from Patron import Patron

from LIS_setup import db as DATA

class Portal:
	"""docstring for Portal"""
	def __init__(self, data):
		self.data = data
		self.commands = [
			'patrons',
			'patron',
			'new_patron',
			'titles',
			'title',
			'new_title',
			'items',
			'new_item',
			'quit',
		]


	## Main/Control loops
	def main(self):
		self.control_loop(self, self._parse_cmd)
		self.main()

	def control_loop(self, obj, parser):
		print('------\nCommand options:')
		for each in obj.commands:
			print('\t', each)
		if obj != self:
			print('\t', 'back')
		cmd, option = parser()
		if cmd == 'back':
			pass
		else:
			if cmd in obj.commands:
				x = getattr(obj, cmd, lambda x: print('Command not found'))
				try:
					x(option)
				except TypeError:
					print(x)
			else:
				print('Command not allowed')
			self.control_loop(obj, parser)


	## Portal commands
	def new_patron(self, *args, input_f=input):
		name = input_f('Enter name: ')
		address = input_f('Enter address: ')
		phone = input_f('Enter phone number: ')
		bday = self._get_birthday()
		p = Patron(name)
		p.address = address
		p.phone_number = phone
		p.birthday = bday
		self.data['Patrons'].append(p)
		p.display()

	def patrons(self, *args):
		self._display_objects('Patrons')

	def patron(self, number):
		p = self._get_patron(number)
		if p:
			p.display()
			self.control_loop(p, self._parse_cmd)
		else:
			msg = 'Format for patron command is:  patron [patron_number]\ne.g.:  patron 101'
			self._patron_not_found(number, msg=msg)

	def new_title(self, *args, input_f=input):
		title = input_f('Enter title: ')
		value = int(input_f('Enter value (integer): '))
		item_type = input_f('Enter item type [book | av | magazine]: ')
		num_items = int(input_f('Number of Items to create (integer): '))
		t = Item.new_title(title, value, item_type, num_items=num_items)
		self.data['Titles'].append(t)
		for item in t.items:
			self.data['Items'].append(item)
		t.display()

	def titles(self, *args):
		self._display_objects('Titles')

	def title(self, number):
		t = self._get_title(number)
		if t:
			t.display()
			self.control_loop(t, self._parse_cmd)
		else:
			msg = 'Format for title command is:  title [title_number]\ne.g.:  title 5001'
			self._title_not_found(number, msg=msg)

	def items(self, *args):
		self._display_objects('Items')

	def new_item(self, *args, input_f=input):
		title_num = input_f('Enter title number: ')
		number = input_f('Number of items to create: ')
		t = self._get_title(title_num)
		news = t.new_items(number)
		for each in news:
			self.data['Items'].append(each)

	def quit(self, *args, **kwargs):
		sys.exit()


	## Utility functions
	def _parse_cmd(self, input_f=input):
		inp = input_f('cmd >> ')
		inp = inp.split()
		cmd = inp[0]
		try:
			option = inp[1]
		except IndexError:
			option = None
		return cmd, option

	def _display_objects(self, group):
		for each in self.data[group]:
			each.display()
			print()

	def _get_patron(self, number):
		for p in self.data['Patrons']:
			if str(p.card_number) == number:
				return p
		return None

	def _patron_not_found(self, number, msg=None):
		print('No patron found with card number {0}'.format(number))
		if msg:
			print(msg)

	def _get_title(self, number):
		for t in self.data['Titles']:
			if str(t.title_number) == number:
				return t
		return None

	def _title_not_found(self, number, msg=None):
		print('No Title found with title number {0}'.format(number))
		if msg:
			print(msg)

	def _get_birthday(self):
		y = self._get_number('Enter birthday year: ', mini=1900, maxi=datetime.date.today().year)
		m = self._get_number('Enter birthday month: ', mini=1, maxi=12)
		d = self._get_number('Enter birthday day: ', mini=1, maxi=31)
		try:
			bday = datetime.date(y, m, d)
		except ValueError:
			print('Bad date.  Please check values and try again.')
			return self._get_birthday()
		return bday

	def _get_number(self, msg, input_f=input, mini=None, maxi=None):
		x = input_f(msg)
		try:
			x = int(x)
		except ValueError:
			print('Value must be an integer between {0} and {1}'.format(mini, maxi))
			return self._get_number(msg, mini=mini, maxi=maxi)
		if mini <= x <= maxi:
			return x
		else:
			print('Value must be an integer between {0} and {1}'.format(mini, maxi))
			return self._get_number(msg, mini=mini, maxi=maxi)

if __name__ == '__main__':
	print('\nWelcome to the Library Information System\n')
	Portal(DATA).main()
