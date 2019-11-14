def running_total(array):
	total = 0
	new_array = []

	for num in array:
		total += num
		new_array.append(total)
	
	return new_array

print(running_total([2, 5, 13]) == [2, 7, 20])
print(running_total([14, 11, 7, 15, 20]) == [14, 25, 32, 47, 67])
print(running_total([3]) == [3])
print(running_total([]) == [])