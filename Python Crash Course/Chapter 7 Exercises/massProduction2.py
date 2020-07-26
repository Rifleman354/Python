prompt = '\nWhat vehicle do you want to mass produce Archmagos?  '
prompt += '\n(Enter "quit" when you are finished) Type here: '
# Prompts the user what vehicle should be deployed
while True: # Makes a continuous loop until the user types 'quit'
	vehicle_input = input(prompt)
	if vehicle_input == 'quit':
		break
	else:
		print('We will mass produce ' + vehicle_input.title() + ', Archmagos!')
		# Outputs the input of vehicle would be deployed
