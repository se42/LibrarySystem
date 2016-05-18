import datetime


def new_title(title, value, item_type, *args, **kwargs):
	d = {
		'book': Book,
		'av': AudioVideo,
		'magazine': Magazine,
	}
	return d[item_type](title, value, *args, **kwargs)


class Title:
	"""docstring for Title"""
	_title_numbers = [5000]

	@classmethod
	def _next_title_number(cls):
		num = max(cls._title_numbers) + 1
		cls._title_numbers.append(num)
		return num

	def __init__(self, title, value, loanable=True, bestseller=False, num_items=0):
		self.title_number = self._next_title_number()
		self.title = title
		self.value = value
		self.loanable = loanable
		self.bestseller = bestseller
		self.period = datetime.timedelta(weeks=3)
		self.items = []

		self.commands = ['new_items']

		for each in range(num_items):
			self.items.append(Item(self))

	def new_items(self, number):
		news = []
		for each in range(int(number)):
			new = Item(self)
			self.items.append(new)
			news.append(new)
		return news

	def display(self):
		print(self.title)
		print('\tTitle number:', self.title_number)
		print('\tValue:', self.value)
		print('\tLoanable:', self.loanable)
		print('\tBestseller:', self.bestseller)
		print('\tRental period:', self.period)
		print('\tItems listing:', self.items)


class Book(Title):
	"""docstring for Book"""
	def __init__(self, *args, author=None, edition=None, pub_date=None, publisher=None, **kwargs):
		self.author = author
		self.edition = edition
		self.pub_date = pub_date
		self.publisher = publisher
		super(Book, self).__init__(*args, **kwargs)


class AudioVideo(Title):
	"""docstring for AudioVideo"""
	def __init__(self, *args, **kwargs):
		super(AudioVideo, self).__init__(*args, **kwargs)


class Magazine(Title):
	"""docstring for Magazine"""
	def __init__(self, *args, **kwargs):
		super(Magazine, self).__init__(*args, **kwargs)
		self.loanable = False


class Item:
	"""docstring for Item"""

	_item_numbers = [1000]

	@classmethod
	def _next_item_number(cls):
		num = max(cls._item_numbers) + 1
		cls._item_numbers.append(num)
		return num

	def __init__(self, title):
		self.title = title
		self.item_number = self._next_item_number()

	def display(self):
		print('Item number:', self.item_number)
		print('Title:', self.title.title)
		
		
		
		
