class TP_Database():
	'''Tech priest database class'''
	
	def __init__(self, name, rank):
		'''Initializes the name and rank attributes'''
		self.name = name
		self.rank = rank
		
	def describe_TP(self, *extraDesc):
		'''Summarizes the information about the tech priest'''
		print(self.rank.title() + ' ' + self.name.title() + ' has the following information in the database:')
		for desc in extraDesc:
			print('- ' + desc)
			
	def greet_TP(self):
		'''Greets the tech priest'''
		print('\nHello ' + self.rank.title() + ' ' + self.name.title() + '!')
		
Helios = TP_Database('helios', 'archmagos')
Helios.describe_TP('Location: Uldan','Age: 1800', 'Role: Artisan')
Helios.greet_TP()