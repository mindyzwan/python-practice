def arithmetic():
	num1 = int(input('Enter the first number:\n'))
	num2 = int(input('Enter the second number:\n'))

	operators = {
		'*': num1 * num2,
	 	'-': num1 - num2,
		'+': num1 + num2,
		'/': num1 / num2,
		'%': num1 % num2,
		'**': num1 ** num2
		}

	for operator, result in operators.items():
		print(f'{num1} {operator} {num2} = {result}')

arithmetic()