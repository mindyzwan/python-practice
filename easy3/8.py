def palindrome(string):
	return string == string[::-1]

print(palindrome('madam') == True)
print(palindrome('Madam') == False)          # (case matters)
print(palindrome("madam i'm adam") == False) # (all characters matter)
print(palindrome('356653') == True)