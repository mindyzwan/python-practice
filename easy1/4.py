def count_occurrences(array):
	for item in set(array):
		print(item, ' => ', array.count(item))


vehicles = [
  'car', 'car', 'truck', 'car', 'SUV', 'truck',
  'motorcycle', 'motorcycle', 'car', 'truck'
]

count_occurrences(vehicles)