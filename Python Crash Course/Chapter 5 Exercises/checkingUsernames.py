current_users = ['Matthew', 'Amanda', 'Terry', 'Ashley', 
	'Bruce']
new_users = ['Ashley', 'York', 'Jacob', 'Terry',
	'Caitlyn']

for call_new_users in new_users: # A loop that determines redundant names
	if call_new_users in current_users:
		print('Username ' + call_new_users + ' is not availible!')
	else:
		print('Username ' + call_new_users + ' is availible')
		# There are 2 redundant and unavailable names