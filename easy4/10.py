def integer_to_string(num):
	nums = {
		1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
		6: '6', 7: '7', 8: '8', 9: '9', 0: '0'
	}

	digits = []
	num_part = num

	while num_part > 0:
		digit = round((round(num_part / 10, 1) - (num_part // 10)) * 10)
		digits.append(digit)
		num_part -= digit
		num_part //= 10

	return ''.join([nums[digit] for digit in digits[::-1]])

def signed_integer_to_string(num):
    neg = False
    if abs(num) != num: neg = True
    if num == 0: return '0'
    
    return '-' + integer_to_string(abs(num)) if neg else '+' + integer_to_string(num)

print(signed_integer_to_string(4321) == '+4321')
print(signed_integer_to_string(-123) == '-123')
print(signed_integer_to_string(0) == '0')