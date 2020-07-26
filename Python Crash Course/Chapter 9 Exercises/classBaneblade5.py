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
		self.Weapon_Battery = Stormblade_Variant_Battery()
		
	def baneblade_variants(self):
		'''Stores a list of variants'''
		models = ['Shadowsword', 'Stormblade', 'Original', 'Stormhammer']
		while models:
			current_models = models.pop()
			self.variants_ready.append(current_models)
		
	def print_variants(self):
		'''Prints the ready list of variants'''
		print('\nThe following Baneblade variants can be deployed into the field: ')
		for variants in self.variants_ready:
			print('- ' + variants.title())
			
class Stormblade_Variant_Battery():
	'''Determines the Stormblade variant's main weapon battery'''
	
	def __init__(self, battery = 0):
		'''Initializes attributes of the Stomrblade battery'''
		self.battery = battery
		
	def Stormblade_Battery_Charge(self, charge):
		'''Sets the Stormblade charge'''
		if charge >= self.battery:
			self.battery = charge
		else:
			print("You can't roll back Stormblade charge!")
	
	def Stormblade_Battery_Recharge(self, recharge):
		'''Recharges the Stormblade's main weapon battery'''
		self.battery += recharge
	
	def Stormblade_Battery_Check(self):
		'''Reads the battery charge of the main weapon'''
		if self.battery > 100:
			print("You can't go over the 100% charge of the Stormsword's weapon! Charge Currently: 100%")
			self.battery = 100
		else:
			print('The Stormblade has a ' + str(self.battery) + '% charge on the main gun!')
			
	def Stormblade_Fire(self):
		'''Stormblade fires its main gun, and discharges the battery reserve'''
		if self.battery < 20:
			print("You must recharge the Stormsword before you fire!")
		else:
			print("The Stormblade had fired its main gun!")
			self.battery -= 20
		
Stormblade = BaneBlade_Variants("Sol System")
Stormblade.Weapon_Battery.Stormblade_Battery_Check()
Stormblade.Weapon_Battery.Stormblade_Battery_Recharge(20)
Stormblade.Weapon_Battery.Stormblade_Battery_Check()
Stormblade.Weapon_Battery.Stormblade_Fire()
Stormblade.Weapon_Battery.Stormblade_Battery_Check()