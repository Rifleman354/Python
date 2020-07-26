class BaneBlade():
	"""Command the Baneblade to do something"""
	
	def __init__(self, location):
		'''Initialize the Baneblade attributes'''
	def fireAllGuns(self):
		'''Simulates the Baneblade firing all their guns'''
		print('The Baneblade is now firing at the target!')
		
	def relocate(self):
		'''The Baneblade redeploys to a new location'''
		print('The Baneblade is now being deployed to the ' + self.location.title() + '!')
		
class BaneBlade_Variants(BaneBlade):
	'''Class that stores a list of Baneblade variants'''
	
	def __init__(self, location):
		'''Initializes attributes of the parent class'''
		super().__init__(location)
		self.variants_ready = []
		
	def baneblade_variants(self):
		'''Stores a list of variants'''
		models = ['Shadowsword', 'Omega', 'Original', 'Stormhammer']
		while models:
			current_models = models.pop()
			self.variants_ready.append(current_models)
		
	def print_variants(self):
		'''Prints the ready list of variants'''
		print('\nThe following Baneblade variants can be deployed into the field: ')
		for variants in self.variants_ready:
			print('- ' + variants.title())
			
Other_Variants = BaneBlade_Variants('Sol System')
Other_Variants.baneblade_variants()
Other_Variants.print_variants()