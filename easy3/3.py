def count_characters():
	words = input('Please write a word or multiple words: ')
	words = words.replace(' ', '')
	print(f'There are {len(words)} characters in \"{words}\".')

count_characters()