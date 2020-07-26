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
		
class Database_Admin_Login(TP_Database):
	'''Class that gives admin priviledges to the developer'''
	
	def __init__(self, name, rank):
		'''Initializes the priviledges attribute'''
		super().__init__(name, rank)
		self.priviledges = []
		
	def show_priviledges(self):
		'''Prints the available commands the admin has'''
		priviledges_ready = ["Can Add Post", "Can Delete Post", "Can Ban User"]
		while priviledges_ready:
			current_priviledges = priviledges_ready.pop()
			self.priviledges.append(current_priviledges)
		print('\nThe following priviledges are yours to use in the database: ')
		for commands in self.priviledges:
			print('- ' + commands.title())
	
Admin = Database_Admin_Login("helios", "archmagos")
Admin.show_priviledges()