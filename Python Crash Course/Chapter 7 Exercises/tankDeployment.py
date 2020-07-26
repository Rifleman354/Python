prompt = input('How many Leman Russ tanks do you want us to deploy Archmagos? \nInput digit in tanks:')
prompt = int(prompt) #Takes the input of numerical Leman Russ tanks to deploy
if 1 < prompt < 20:
	print('We will deploy ' + str(prompt) + ' Leman Russ tanks, Archmagos!')
	# Prompts the user, on their specified input, how many tanks are to be deployed
elif prompt >= 20:
	print('We need more materials for producing more Leman Russ tanks, Archmagos!')
	# Prompts the user that there isn't enough material for 20 or more tanks
elif prompt == 1:
	print('We are deploying one Leman Russ tank, Archmagos!')
	# Prompts the user that one tank is being deployed
