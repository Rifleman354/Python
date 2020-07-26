def build_40K_vehicles(*vehicles):
	'''Print 40K vehicles'''
	print('\nMass producing the following vehicles, Archmagos: ')
	for vehicle in vehicles:
		print('- ' + vehicle)

build_40K_vehicles('Leman Russ', 'Baneblade')
build_40K_vehicles('Macharius')
build_40K_vehicles('Chimera')