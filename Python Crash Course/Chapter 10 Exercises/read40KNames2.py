def name_file_read(nameFiles):
	"""Reads out names from specified files"""
	try: 
		with open(nameFiles) as o_files:
			names = o_files.read() #Reads out the files
	except FileNotFoundError:
		pass
	else:
		# Prints the contents of the file
		print(names)
			
nameFiles = ['admechNames.txt', 'astartesNames.txt']
for read_out in nameFiles:
	name_file_read(read_out)