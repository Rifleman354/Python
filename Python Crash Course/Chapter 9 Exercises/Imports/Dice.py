from random import randint

class Dice():
	'''Random number generator; dice theme'''
	
	def __init__(self, die_faces):
		'''Initializes the name and rank attributes'''
		self.die_faces = die_faces
		self.startRoll = 1
	
	def roll_die(self):
		'''Random interger function with 6 faces, from random library'''
		print("\nRolls of " + str(self.die_faces) + " faced die: ")
		while self.startRoll <= 10:
			print(randint(1, self.die_faces))
			self.startRoll += 1
		
roll = Dice(6)
roll.roll_die()

roll2 = Dice(10)
roll2.roll_die()

roll3 = Dice(20)
roll3.roll_die()