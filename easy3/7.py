def oddities(array):
	return [element for index, element in enumerate(array) if index % 2 == 0]

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])
print(oddities([1, 2, 3, 4, 5, 6]) == [1, 3, 5])
print(oddities(['abc', 'def']) == ['abc'])
print(oddities([123]) == [123])
print(oddities([]) == [])