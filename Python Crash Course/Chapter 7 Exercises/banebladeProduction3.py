prompt = '\nHow many Baneblades do you want us to mass produce Archmagos?'
prompt += '\n(Enter "quit" when you are finished) Type digits here: '
# Prompts the user to input numerical digits of how many Baneblades to deploy

active = True # Creates a flag that allows the user to quit the program
while active:
	vehicle_input = input(prompt)
	if vehicle_input == 'quit':
		active = False
		continue
	vehicle_quantity = int(vehicle_input)
	if vehicle_quantity == 0:
		print('You have to mass produce vehicles to the war effort, Archmagos!')
		# Notifies the user to make a Baneblade
	elif vehicle_quantity <= 2:
		print('You need to produce more vehicles to the war effort, Archmagos!')
		# Tells the user to make more Baneblades
	elif 50 > vehicle_quantity > 2:
		print('Producing ' + str(vehicle_quantity) + ' Baneblades, Archmagos!')
		# Tells the user on how many Baneblades that will be produced
	elif vehicle_quantity >= 50:
		print('We do not have enough materials to produce that many, Archmagos!')
		# Warns the user that he or she is asking for too many tanks