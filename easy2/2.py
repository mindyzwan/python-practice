def area():
    length = input('Enter the length of the room in meters: \n')
    width = input('Enter the width of the room in meters: \n')
    area_meters = int(length) * int(width)
    area_feet = area_meters * 10.7639
    print('The area of the room is', area_meters, 'square meters (', area_feet, 'square feet ).')

area()