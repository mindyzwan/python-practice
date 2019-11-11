def calculate_bonus(salary, bonus):
    return 0.5 * salary if bonus else 0

print(calculate_bonus(2800, True) == 1400)
print(calculate_bonus(1000, False) == 0)
print(calculate_bonus(50000, True) == 25000)