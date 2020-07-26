def Names_40K(usernames, titled_names):
	"""Loops names of untitled tech priests"""
	while usernames:
		current_names = usernames.pop()
		#Tech priests being promoted
		print('Tech priests being promoted: ' + current_names.title())
		titled_names.append(current_names)

def Archmagos_Title(titled_names):
	"""Loops new titles to tech priests"""
	print("\nThe following tech priests have been promoted to Archmagos:")
	for titled_name in titled_names:
		print("Archmagos " + titled_name.title())
		
usernames = ["cawl", "helios", "satarael"]
titled_names = []
Names_40K(usernames, titled_names)
Archmagos_Title(titled_names)