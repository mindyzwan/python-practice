def digit_list(num):
	return [int(digit) for digit in str(num)]

print(digit_list(12345) == [1, 2, 3, 4, 5])
print(digit_list(7) == [7])
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])
print(digit_list(444) == [4, 4, 4])