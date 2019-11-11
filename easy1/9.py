def sum_digits(num):
	return sum([int(digit) for digit in str(num)])

print(sum_digits(23) == 5)
print(sum_digits(496) == 19)
print(sum_digits(123_456_789) == 45)