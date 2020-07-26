modulo = input('Enter a number, and I will tell you if it is divisible by 10. \nEnter digits:')
modulo = int(modulo)
# Asks the user to input a number, then determines if it is divisible by 10
# Thanks to the modulo
if modulo % 10 == 0:
	print('The number ' + str(modulo) + ' is divisible by 10.')
else:
	print('The number ' + str(modulo) + ' is not divisible by 10!')
