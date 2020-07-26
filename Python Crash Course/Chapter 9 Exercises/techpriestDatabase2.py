class TP_Database():
	'''Tech priest database class'''
	
	def __init__(self, name, rank):
		'''Initializes the name and rank attributes'''
		self.name = name
		self.rank = rank
		self.login_attempts = 0
		
	def describe_TP(self, *extraDesc):
		'''Summarizes the information about the tech priest'''
		print(self.rank.title() + ' ' + self.name.title() + ' has the following information in the database:')
		for desc in extraDesc:
			print('- ' + desc)
			
	def greet_TP(self):
		'''Greets the tech priest'''
		print('\nHello ' + self.rank.title() + ' ' + self.name.title() + '!')
		
	def increment_login_attempts(self, attempts):
		'''Increments the amount of logins'''
		self.login_attempts += attempts
		
	def reset_login_attempts(self):
		'''Resets the login attempts to zero'''
		self.login_attempts = 0
		
	def read_login_attempts(self):
		'''Reads the attempts the user has logged in'''
		print('The current user has logged in with ' + str(self.login_attempts) + ' times.')
		
Helios = TP_Database('helios', 'archmagos')
Helios.read_login_attempts()
Helios.increment_login_attempts(6)
Helios.read_login_attempts()
Helios.reset_login_attempts()
Helios.read_login_attempts()
Helios.increment_login_attempts(4)
Helios.read_login_attempts()