def TechPriest_Profile(Rank, Name, **Desc):
	'''Builds a dictionary containing tech preist information'''
	profile = {}
	profile['Rank'] = Rank
	profile['Name'] = Name
	for key, value in Desc.items():
		profile[key] = value
	return profile
	
Profile = TechPriest_Profile('Archmagos', 'Helios', location = 'Uldan', age = '1800', role = 'Artisan')
print(Profile)
