import datetime

def retire():
    age = int(input('What is your age? '))
    retire_age = int(input('At what age would you like to retire? '))
    current_year = datetime.date.today().year
    years_left = retire_age - age
    retire_year = current_year + years_left

    print(f"It's {current_year}. You will retire in {retire_year}. \nYou have only {years_left} of work to go!")

retire()