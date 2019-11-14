def leap_year(year):
	leap = False

	if year % 4 == 0: leap = True
	if year % 100 == 0: leap = False
	if year % 400 == 0: leap = True

	return leap

print(leap_year(2016) == True)
print(leap_year(2015) == False)
print(leap_year(2100) == False)
print(leap_year(2400) == True)
print(leap_year(240000) == True)
print(leap_year(240001) == False)
print(leap_year(2000) == True)
print(leap_year(1900) == False)
print(leap_year(1752) == True)
print(leap_year(1700) == False)
print(leap_year(1) == False)
print(leap_year(100) == False)
print(leap_year(400) == True)