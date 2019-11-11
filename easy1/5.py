def reverse_sentence(string):
	return ' '.join(string.split(' ')[::-1])

print(reverse_sentence('') == '')
print(reverse_sentence('Hello World') == 'World Hello')
print(reverse_sentence('Reverse these words') == 'words these Reverse')