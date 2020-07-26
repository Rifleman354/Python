def Vehicle_Variant(tank_model, tank_variant, deployment_location='Sol System'):
	"""Prints the location where the Leman Russ tank will be deployed
		and what variant it is"""
	make_tank = {'model':tank_model,'variant':tank_variant, 'location':deployment_location}
	return make_tank

LemanRussV1 = Vehicle_Variant('Baneblade','Omega')	
LemanRussV2 = Vehicle_Variant('Leman Russ','Vanquisher', 'Kaurava System')
LemanRussV3 = Vehicle_Variant('Leman Russ','Annihilator','Armageddon System')
LemanRussV4 = Vehicle_Variant('Leman Russ','Eradicator')
print(LemanRussV1)
print(LemanRussV2)
print(LemanRussV3)
print(LemanRussV4)