from collections import OrderedDict

python_glossary = OrderedDict()

python_glossary['variables'] = 'storing individual pieces of information'
python_glossary['if_statements'] = 'conditional statement that returns a boolean value'
python_glossary['boolean'] = 'true or false value'
python_glossary['string'] = 'an array of characters, characters, or numbers'

for name, language in python_glossary.items():
	print(name.title() + ": " +
		language.title() + ".")
