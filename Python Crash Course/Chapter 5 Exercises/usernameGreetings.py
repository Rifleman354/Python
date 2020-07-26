Usernames = ['admin','Joel','Alexis','Kensley']

for Call_Username in Usernames:
	if Call_Username == 'admin': # A conditional statement that gives a different prompt if admin logs in
		print('Hello admin, would you like to see a status report?')
	else: # A condition that gives the user this prompt
		print('Hello ' + Call_Username + "!")