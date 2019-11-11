def tip_calculator():
    base = int(input('What is the bill? '))
    tip_percent = int(input('What is the tip percentage? '))
    tip = base * (tip_percent / 100)
    total = base + tip

    print('The tip is ${0}'.format(tip))
    print('The total is ${0}'.format(total))

tip_calculator()