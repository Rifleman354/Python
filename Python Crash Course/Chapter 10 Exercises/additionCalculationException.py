print("Input 2 numbers, and I'll add them.")
print("Enter 'q' to quit.\n")
# Simple addition calculator inputted by prompted user

while True:
	# The while loop allows the user to quit the program...
	# in the middle of the calculation by pressing 'q'
	first_number = input("Type first number: \n")
	if first_number.lower() == 'q':
		break
	second_number = input("Type second number: \n")
	if second_number.lower() == 'q':
		break
	try:
		answer = int(first_number) + int(second_number)
	except:
		print("You need to input digits!")
		# Prompts the user to input digits only via try-except block
	else:
		print("Your result: " + str(answer))
		# Prompts the user of the result