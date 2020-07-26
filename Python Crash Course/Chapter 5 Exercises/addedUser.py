Usernames = ['admin'] # This is the user list of the program

if Usernames:
	for Call_Username in Usernames: # A loop that allows new users to be inputted
		print('Adding ' + Call_Username + '.') # as long as the program runs
else:
	print('We need users!') # If there are no users, this is the output