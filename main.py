import random

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

