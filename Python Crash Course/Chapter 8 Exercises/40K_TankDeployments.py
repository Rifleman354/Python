def Vehicle_Variant(tank_model, tank_variant, deployment_location):
	"""Prints the location where the tank model will be deployed
		and what variant it is"""
	make_tank = 'Archmagos, the ' + model + ' (Variant ' + variant + ')' + ' will be deployed in the ' + location + '!'
	return make_tank

while True:
	print("\nWhat tank model do you want us to mass produce, Archmagos? (Type 'q' to quit)")
	
	model = input('Model, type here: ')
	if model == 'q':
		break
		
	variant = input('Variant? Type here: ')
	if variant == 'q':
		break
		
	location = input('Location? Type here: ')
	if location == 'q':
		break

	deploy_tank = Vehicle_Variant(model,variant,location)
	print(deploy_tank)
