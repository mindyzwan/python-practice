def string_to_signed_integer(string):
	neg = False

	if string.startswith('-'): neg = True
	if string.startswith('-') or string.startswith('+'):
		integer = string_to_integer(string[1:])
	else:
		integer = string_to_integer(string)

	return integer * -1 if neg else integer


def string_to_integer(string):
	nums = {
		'1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
		'6': 6, '7': 7, '8': 8, '9': 9, '0': 0
	}
	multiplier = 1
	integer = 0

	for char in string[::-1]:
		integer += nums[char] * multiplier
		multiplier *= 10

	return integer

print(string_to_signed_integer('4321') == 4321)
print(string_to_signed_integer('-570') == -570)
print(string_to_signed_integer('+100') == 100)