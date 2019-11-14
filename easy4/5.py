def multisum(num):
	return sum([n for n in range(num + 1) if n % 5 == 0 or n % 3 == 0])

print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)