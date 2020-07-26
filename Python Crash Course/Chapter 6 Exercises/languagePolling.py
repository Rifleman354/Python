favorite_languages = {'jen': 'python', 'sarah': 'c','edward': 'ruby', 'phil': 'python',
'artemis':'not polled', 'joey':'not polled'} # Input dictionary

for name in favorite_languages.keys(): # Loops the dictionary
	if 'not polled' != favorite_languages[name]:
		print(name.title() + ', thank you for taking the poll!')
		# Conditional statement that prints this string if the key isn't 'not polled'
	else:
		print(name.title() + ', please take the poll!')
		# Conditional statement that prompts the user to take the poll