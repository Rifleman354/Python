print("Input 2 numbers, and I'll add them.")
print("Enter 'q' to quit.\n") # Simple addition calculator inputted by prompted user

first_number = input("Type first number: \n")
second_number = input("Type second number: \n")
try:
	answer = int(first_number) + int(second_number)
except:
	print("You need to input digits!")
	# The try-exception block prompts the user to put in digits only
else:
	print("Your result: " + str(answer))
	#The result of the user inputting 2 digits into system
