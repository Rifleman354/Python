LemanRusses_In_Production = ['Annihilator,' 'Original,' 'Conqueror,' 'Demolisher,'
 'Punisher'] # The list of Leman Russ tanks that are being produced
LemanRusses_Deployed = [] # The output list of Leman Russ tanks

while LemanRusses_In_Production: # The loop of Leman Russ tanks
	currently_in_production = LemanRusses_In_Production.pop()  
		# Pops all the Leman Russ tanks in LemanRusses_In_Production list												
	print('Archmagos, we have Leman Russ variants (' +
		currently_in_production.title() + ') in production!') 
		# Prints the Leman Russ tanks that would be in production
	LemanRusses_Deployed.append(currently_in_production)
		# Adds new content to the LemanRusses_Deployed list
print('\nThe following variants have been deployed, Archmagos! -')
	# Prints a prompt telling the user the following has been deployed
for LemanRusses_Deployed in LemanRusses_Deployed:
	print(LemanRusses_Deployed.title()) # The output loop of the tank variants