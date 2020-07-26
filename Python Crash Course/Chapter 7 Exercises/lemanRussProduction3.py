vehicle_Input = {} # The dictionary that would contain all the vehicle inputs

vehicle_Orders = True # The flag that turns the program on, 
					#but can be turned off by user

while vehicle_Orders: # The loop that notifies the user what tank variants to deploy
	name = input('\nWhat is your name Archmagos? ') # Asks for the user's name
	order = input('What Leman Russ tank variant would you like to deploy Archmagos '
		+ name.title() + '? ') # Asks for input on what Leman Russ tank variant to deploy
	
	vehicle_Input[name] = order # The inputs are then stored into the vehicle_Input dictionary
	
	new_Order = input('Would you like another variant? (yes/no) ')
	if new_Order == 'no': # If the user types 'no,' it ends the loop, then...
		vehicle_Orders = False

print('\n --- Leman Russ tanks in the field! ---')
for name, order in vehicle_Input.items(): #  the vehicle_Input goes to a new loop outputting the user inputs
	print('Archmagos ' + name + ', the tank variant ' + order +
	' Leman Russ has been deployed!')
