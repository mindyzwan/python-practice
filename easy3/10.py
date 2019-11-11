def palindromic_number(num):
	return str(num) == str(num)[::-1]

print(palindromic_number(34543) == True)
print(palindromic_number(123210) == False)
print(palindromic_number(22) == True)
print(palindromic_number(5) == True)