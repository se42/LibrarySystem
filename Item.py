import datetime


class Title:
	"""docstring for Title"""
	def __init__(self, title, author, value, edition=None, pub_date=None,
		publisher=None, item_type='book', num_items=0, loanable=True,
		bestseller=False, period=datetime.timedelta(weeks=3)):

		self.title = title
		self.author = author
		self.value = value
		self.edition = edition
		self.pub_date = pub_date
		self.publisher = publisher
		self.loanable = loanable
		self.bestseller = bestseller
		self.period = period
		self.items = []

		for each in range(num_items):
			if item_type == 'book':
				x = Book(self)
			elif item_type == 'audiovideo':
				x = AudioVideo(self)
			elif item_type == 'magazine':
				x = Magazine(self)
			self.items.append(x)


class Item:
	"""docstring for Item"""

	_item_numbers = [1000]

	def __init__(self, title):
		self.title = title
		self.item_number = self._next_item_number()

	@classmethod
	def _next_item_number(cls):
		num = max(cls._item_numbers) + 1
		cls._item_numbers.append(num)
		return num


class Book(Item):
	"""docstring for Book"""
	def __init__(self, *args, **kwargs):
		super(Book, self).__init__(*args, **kwargs)


class AudioVideo(Item):
	"""docstring for AudioVideo"""
	def __init__(self, *args, **kwargs):
		super(AudioVideo, self).__init__(*args, **kwargs)


class Magazine(Item):
	"""docstring for Magazine"""
	def __init__(self, *args, **kwargs):
		super(Magazine, self).__init__(*args, **kwargs)
		
		
		
		
