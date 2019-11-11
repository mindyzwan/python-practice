def sum_product():
	integer = 0
	while integer <= 0:
		integer = int(input('Please enter an integer greater than 0: '))
		if integer < 0: print('Not a valid option.')

	operation = ''
	while operation not in ['s', 'p']:
		operation = input("Enter 's' to compute the sum, 'p' to compute the product. ")
		if operation not in ['s', 'p']: print('Not a valid option.')
	
	if operation == 's':
		print(f'The sum of the integers between 1 and {integer} is {sum(range(1, integer + 1))}') 
	else:
		print(f'The product of the integers between 1 and {integer} is {product(range(1, integer + 1))}') 

def product(nums):
	product = 1

	for num in nums:
		product *= num
	
	return product

sum_product()