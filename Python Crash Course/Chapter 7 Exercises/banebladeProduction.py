prompt = '\nHow many Baneblades do you want us to mass produce Archmagos?'
prompt += '\n(Enter "quit" when you are finished) Type digits here: '
#Prompts the user how many Baneblades he or she wants on the field
while True: #Outputs a loop of the user's input
	vehicle_input = input(prompt)
	vehicle_quantity = int(vehicle_input)
	if vehicle_quantity == '0
		print('You have to mass produce vehicles to the war effort, Archmagos!')
		# Condition that tells the user they have to put a number greater than zero
	elif vehicle_quantity < 2:
		print('You need to produce more vehicles to the war effort, Archmagos!')
		# Condition that tells the user to make more than 2 vehicles
	elif 50 > vehicle_quantity > 2:
		print('Producing ' + str(vehicle_quantity) + ' Baneblades, Archmagos!')
		# Condition that outputs the quantity of Baneblades to be produced
	elif vehicle_quantity >= 50:
		print('We do not have enough materials to produce that many, Archmagos!')
		# Condition that tells the user that there isn't enough material
		# for more than 50 Baneblades
