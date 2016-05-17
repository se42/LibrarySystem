import datetime


def new_title(title, author, value, item_type, *args, **kwargs):
	d = {
		'book': Book,
		'av': AudioVideo,
		'magazine': Magazine,
	}
	return d[item_type](title, author, value, *args, **kwargs)


class Title:
	"""docstring for Title"""
	def __init__(self, title, author, value, edition=None, pub_date=None,
		publisher=None, num_items=0):

		self.title = title
		self.author = author
		self.value = value
		self.edition = edition
		self.pub_date = pub_date
		self.publisher = publisher
		self.loanable = True
		self.bestseller = False
		self.period = datetime.timedelta(weeks=3)
		self.items = []

		for each in range(num_items):
			self.items.append(Item(self))


class Book(Title):
	"""docstring for Book"""
	def __init__(self, *args, **kwargs):
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

	def __init__(self, title):
		self.title = title
		self.item_number = self._next_item_number()

	@classmethod
	def _next_item_number(cls):
		num = max(cls._item_numbers) + 1
		cls._item_numbers.append(num)
		return num
		
		
		
		
