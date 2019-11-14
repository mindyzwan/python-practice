import math

def century(year):
	century = int((year - 1) / 100 + 1)
	return str(century) + return_ordinal(century)

def return_ordinal(num):
	ordinals = {'1': 'st', '2': 'nd', '3':'rd'}

	last_two = str(num)[-2:]
	if last_two in ['11', '12', '13']: return 'th'

	last_one = str(num)[-1]
	if last_one in ['1', '2', '3']:
		return ordinals[last_one]
	else:
		return 'th'

print(century(2000) == '20th')
print(century(2001) == '21st')
print(century(1965) == '20th')
print(century(256) == '3rd')
print(century(5) == '1st')
print(century(10103) == '102nd')
print(century(1052) == '11th')
print(century(1127) == '12th')
print(century(11201) == '113th')