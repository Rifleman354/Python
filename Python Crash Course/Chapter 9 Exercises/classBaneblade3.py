class BaneBlade():
	"""Command the Baneblade to do something"""
	
	def __init__(self, model, location):
		'''Initialize the Baneblade attributes'''
		self.model = model
		self.location = location
		self.odometer_reading = 0
		
	def fireAllGuns(self):
		'''Simulates the Baneblade firing all their guns'''
		print('The ' + self.model.title() + ' is firing at the target!')
		
	def relocate(self):
		'''The Baneblade redeploys to a new location'''
		print('The ' + self.model.title() + ' is now being deployed to the ' + self.location.title() + '!')
			
	def distanceTraveled(self, kilometers):
		"""Sets the odometer of the Baneblade to zero kilometers"""
		if kilometers >= self.odometer_reading:
			self.odometer_reading = kilometers
		else:
			print("You can't roll back an odometer")
		
	def odometerIncrement(self, traveled):
		'''Reads the odometer of the Baneblade'''
		self.odometer_reading += traveled

	def readOdometer(self):
		'''Prints the Baneblade's travel distance'''
		print("The Baneblade has " + str(self.odometer_reading) + ' kilometers on it.')
		
Baneblade = BaneBlade('baneblade', 'karava system')
Baneblade.distanceTraveled(500)
Baneblade.readOdometer()
Baneblade.odometerIncrement(200)
Baneblade.readOdometer()