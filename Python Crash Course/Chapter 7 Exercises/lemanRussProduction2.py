LemanRusses_In_Production = ['Annihilator', 'Punisher', 'Original','Conqueror',
 'Demolisher', 'Punisher', 'Punisher'] # The list of tank variants to be processed
LemanRusses_Deployed = [] # The output list of tank variants

while 'Punisher' in LemanRusses_In_Production: # Loop that removes the Punisher tank variant
	LemanRusses_In_Production.remove('Punisher')
	
while LemanRusses_In_Production:
	# The loop that adds the LemanRusses_In_Production, to LemanRusses_Deployed
	currently_in_production = LemanRusses_In_Production.pop()
	# Pops the list LemanRusses_In_Production into the variable currently_in_production
	print('Archmagos, we have Leman Russ variant (' +
		currently_in_production.title() + ') in production!')
	# Prompts the user what variants are being produced
	LemanRusses_Deployed.append(currently_in_production)
	# Adds new contnent to the LemanRusses_Deployed empty list
	
print('\nThe following variants have been deployed, Archmagos! -')
# Prompts the user what variants have been deployed

for LemanRusses_Deployed in LemanRusses_Deployed:
# The loop that outputs the variants deployed
	print(LemanRusses_Deployed.title())
print('\nWe do not have material for the Punisher variant, Archmagos!')