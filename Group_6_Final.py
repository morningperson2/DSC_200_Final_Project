import pandas as pd

def part1():
    print("Part 1")
    pass

def part1_DS1() -> pd.DataFrame:
    # varient data
    ds1 = pd.read_csv("https://data.chhs.ca.gov/dataset/52e4aa7a-2ea3-4bfd-8cd6-7d653db1ee74/resource/d7f9acfa-b113-4cbc-9abc-91e707efc08a/download/covid19_variants.csv")
    ds1.to_csv('ds1.csv')


def part1_DS2() -> pd.DataFrame:
    # vaccine progress dashboard
    ds2 = pd.read_csv("https://data.chhs.ca.gov/dataset/e283ee5a-cf18-4f20-a92c-ee94a2866ccd/resource/22b05bf3-16e5-4b2b-a66a-6b035e0cd9f4/download/covid19vaccinesadministeredbyhpiquartile.csv")
    ds2.to_csv('ds2.csv')

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
