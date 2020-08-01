import json

database = 'techPriestDatabase.json'
try:
	with open(database) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	username = input("What is your name tech priest? Type here: ")
	with open(database, 'w') as f_obj:
		json.dump(username, f_obj)
		print("Welcome to the database system, Archmagos " + str(username) + "!")
else:
	print("Welcome back, Archmagos " + str(username) + ".")
