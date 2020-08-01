def name_file_read(nameFiles):
	"""Reads out names from specified files"""
	try: 
		with open(nameFiles) as o_files:
			names = o_files.read() #Reads out the files
	except FileNotFoundError:
		msg = "Sorry, the file " + nameFiles + " does not exist."
		print(msg) # Prompts the user that the file does not exist in the system
	else:
		# Prints the contents of the file
		print(names)
			
nameFiles = ['admechNames.txt', 'astartesNames.txt']
for read_out in nameFiles:
	name_file_read(read_out)