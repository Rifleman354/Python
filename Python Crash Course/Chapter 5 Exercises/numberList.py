number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in number_list: # Returns the ordinal numbers from 'number_list' with a loop
	if i == 1: 
		print(str(i) + 'st')
	elif i == 2:
		print(str(i) + 'nd')
	elif i == 3:
		print(str(i) + 'rd')
	else:
		print(str(i) + 'th')
		