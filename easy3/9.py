import re

def real_palindrome(string):
	string = re.sub('[^a-zA-Z]', '', string).lower()
	return string == string[::-1]

print(real_palindrome('madam') == True)
print(real_palindrome('Madam') == True)           # (case does not matter)
print(real_palindrome("Madam, I'm Adam") == True) # (only alphanumerics matter)
print(real_palindrome('356653') == True)
print(real_palindrome('356a653') == True)
print(real_palindrome('123ab321') == False)