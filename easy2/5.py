def greeting():
    name = input('What is your name? ')
    if name.endswith('!'):
        print(f'HELLO {name.upper()} WHY ARE WE SCREAMING?')
    else:
        print(f'Hello {name}.')

greeting()