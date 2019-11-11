def searching():
	ordinals = ['1st', '2nd', '3rd', '4th', '5th', 'last']
	to_check = []

	for ordinal in ordinals:
		to_check.append(int(input(f'Enter the {ordinal} number: \n')))

	last = to_check.pop()

	message = 'appears' if last in to_check else 'does not appear'

	print(f'The number {last} {message} in {to_check}.')
	
searching()