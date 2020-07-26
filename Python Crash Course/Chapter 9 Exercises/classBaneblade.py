class BaneBlade():
	"""Command the Baneblade to do something"""
	
	def __init__(self, model, location):
		'''Initialize the Baneblade attributes'''
		self.model = model
		self.location = location
		
	def fireAllGuns(self):
		'''Simulates the Baneblade firing all their guns'''
		print('The ' + self.model.title() + ' is firing at the target!')
		
	def relocate(self):
		'''The Baneblade redeploys to a new location'''
		print('The ' + self.model.title() + ' is now being deployed to the ' + self.location.title() + '!')
		
Baneblade = BaneBlade('baneblade', 'karava system')
Baneblade.fireAllGuns()

