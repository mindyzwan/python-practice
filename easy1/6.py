def reverse_words(string):
	array = string.split(' ')
	index = 0

	for word in array:
		if len(word) >= 5:
			array[index] = word[::-1]
		index += 1

	return ' '.join(array)

print(reverse_words('Professional'))
print(reverse_words('Walk around the block'))
print(reverse_words('Launch School'))