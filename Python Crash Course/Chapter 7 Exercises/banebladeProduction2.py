prompt = '\nHow many Baneblades do you want us to mass produce Archmagos?'
prompt += '\n(Enter "quit" when you are finished) Type digits here: '
#Prompts the user to type in the numerical input of Baneblades do produce
while True: # Creates a continuous input loop until the user types quit
	vehicle_input = input(prompt)
	if vehicle_input == 'quit':
		break
	vehicle_quantity = int(vehicle_input)
	if vehicle_quantity == 0:
		print('You have to mass produce vehicles to the war effort, Archmagos!')
		# Condition that prompts the user that he or she needs to produce more Banblades
	elif vehicle_quantity <= 2:
		print('You need to produce more vehicles to the war effort, Archmagos!')
		# Condition that prompts the user to make more than 2 tanks
	elif 50 > vehicle_quantity > 2:
		print('Producing ' + str(vehicle_quantity) + ' Baneblades, Archmagos!')
		# Condition that prompts the user how many Baneblades that are going to be produced
	elif vehicle_quantity >= 50:
		print('We do not have enough materials to produce that many, Archmagos!')
		# Condition that warns the user that he or she is asking for too many tanks
	
