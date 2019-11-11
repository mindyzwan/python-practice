array1 = ['Moe', 'Larry', 'Curly', 'Shemp', 'Harpo', 'Chico', 'Groucho', 'Zeppo']
array2 = []

for element in array1:
	array2.append(element)

for index, element in enumerate(array1): 
	if element.startswith('C'): array1[index] = element.upper()

print(array1, array2)
# array1 will have C's uppered