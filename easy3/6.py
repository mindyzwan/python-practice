def xor(operand1, operand2):
	if operand1 and not operand2:
		return True
	if not operand1 and operand2:
		return True
	else: 
		return False

print(xor(True, False))
print(xor(False, True))
print(xor(True, True))
print(xor(False, False))

