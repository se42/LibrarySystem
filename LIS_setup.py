import datetime

from Patron import Patron
from Item import new_title

db = {
	'Patrons': [],
	'Titles': [],
	'Items': [],
}

patrons = [
	('Scott Edwards', datetime.date(1987, 11, 18)),
	('Mary Johnson', datetime.date(1987, 3, 12)),
	('William Jones', datetime.date(1985, 3, 12)),
	('Jessica Little', datetime.date(1985, 3, 12)),
	('Justin Little', datetime.date(2010, 3, 12)),
]

for patron in patrons:
	p = Patron(patron[0])
	p.birthday = patron[1]
	db['Patrons'].append(p)

titles = [
	('Mag 1', 1, 'magazine'),
	('AV 1', 25, 'av'),
	('Book 1', 35, 'book'),
	('Book 2', 45, 'book'),
]

for each in titles:
	title, value, item_type = each
	t = new_title(title, value, item_type)
	t.new_items(2)
	db['Titles'].append(t)
	for item in t.items:
		db['Items'].append(item)
