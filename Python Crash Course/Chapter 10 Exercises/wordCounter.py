def count_words(BookFile):
	'''Method that counts the number of times the specified file has the text "the"'''
	with open(BookFile) as file_object:
		contents = file_object.read()
	tally = contents.lower().count('the')
	print("The file " + BookFile + " has " + str(tally) + " words with the word 'the.'")
	
BookFile = 'mechanicusCommandments.txt'
count_words(BookFile)
