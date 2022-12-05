import pandas as pd

def part1():
    print("Part 1")
    pass

def part1_DS1() -> pd.DataFrame:
    pass

def part1_DS2() -> pd.DataFrame:
    pass

def part1_DS3() -> pd.DataFrame:
    pass

def part1_DS4() -> pd.DataFrame:
    pass

def part1_DS5() -> pd.DataFrame:
    pass

def part2():
    print("Part 2")
    pass

def part2_DS1() -> pd.DataFrame:
    pass

def part2_DS2() -> pd.DataFrame:
    pass

def part2_DS3() -> pd.DataFrame:
    pass


print("Welcome to the final project!")

state = True

while(state):

    choice = int(input("Please enter which part you wish to run (1)Covid (2)DSC Jobs (3)Quit: "))
    while(choice < 1 or choice > 3):
        choice = int(input("%d is not a valid choice. Please try again: "%choice))

    if(choice == 1):
        part1()
    elif(choice == 2):
        part2()
    else:
        state = False