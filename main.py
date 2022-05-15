import random


class Row:
	def __init__(self, table, index, data=None):
		self.fields = table.fields
		self.data = {}
		self.index = index
		for i in range(len(self.fields)):
			if data:
				self.data[self.fields[i]] = data[i]
			else:
				self.data[self.fields[i]] = None
	
	def add_val(self, name, data): #to add a field value to the row
		self.data[name] = data

	def get_val(self, name):
		return self.data[name]

	def remove_val(self, name): #to remove a field from row
		self.data[name] = None

	def del_field(self, name)


class Table:
	def __init__(self, name="Table"):
		self.name = name
		self.fields = []
		self.rows = []

	def add_field(self, name, pos=None): # to add a new field to the table
		if pos:
			self.fields.insert(pos, name)
		else:
			self.fields.append(name)

	def remove_field(self, index):
		name = self.fields[index]
		for i in self.rows:
			i.remove_field(name)

		self.fields.pop(index)

	def add_row(self, data: list):
		new_row = Row(self, len(self.rows), data)
		self.rows.append(new_row)
		return new_row

	def get_row(self, index):
		return self.rows[index]

	def remove_row(self, index):
		self.rows.pop(index)

	def text_table(self, style='normal'):
		if style == 'normal':
			pass
		if style == 'styled'
			pass

	def render(self, style):
		if style == 'text':
			return self.text_table('normal')
		if style == 'text styled'
			return self.text_table('styled')

	def __str__(self):
		return self.render('text')