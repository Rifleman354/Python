def WH40K_Vehicles(tank_model, tank_variant, location = ''):
	"""Returns the tank model and variant from WH40K"""	
	if location:
		print("\"" + tank_model + ", " + tank_variant + ", " + "Location: "
			+ location + "\"")
	else:
		print("\"" + tank_model + ", " + tank_variant + "\"")
	
WH40K_Vehicles("Baneblade", "Omega")
WH40K_Vehicles("Baneblade", "Shadowsword")
WH40K_Vehicles("Leman Russ", "Executioner", "Sol System")