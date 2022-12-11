import requests
from bs4 import BeautifulSoup
import pandas as pd

def part1():
    print("Part 1")
    
    #df = pd.merge(pd.merge(pd.merge(pd.merge(part1_DS1(), part1_DS2(), on="Date"), part1_DS3(), on="Date"), part1_DS4(), on="Date"), part1_DS5(), on="Date")
    #df.to_csv("group_6_covid.csv")

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
    #df1 = part2_DS1()
    #df2 = part2_DS2()

    #df1 = df1[df1["job title"].str.contains(["Data", "DATA"]) == True]
    df = pd.merge(part2_DS1(), part2_DS2(), how="outer", on=["job title", "company name", "city", "state"])
    df = df[df["job title"].str.contains("Data|DATA|data") == True]
    df.to_csv("group_6_dsc_jobs.csv", index=False)
    pass

def part2_DS1() -> pd.DataFrame:
    url= 'https://www.simplyhired.com/search?q=data+science&l=&job=f6OiCClL7m7gOAQ9o5ElmNquyKreuYz_0b-j3kwtgZ4_mb69UV9KQQ'
    html = requests.get(url)

    soup = BeautifulSoup(html.content, "html.parser")

    salary=[]
    job_title=[]
    company_name=[]
    city=[]
    state=[]
    job_type=[]

    for a in soup.find_all('a', class_='SerpJob-link card-link'):
        job_title.append(a.text.strip())

    for div in soup.find_all('div', class_=['SerpJob-metaInfoLeft']):
        if div.text == '':
            salary.append('Unknown')
        else:
            salary.append(div.text.strip('Estimated: ').strip('Quick Apply').strip('a year'))

    for span in soup.find_all('span', class_='JobPosting-labelWithIcon jobposting-company'):
        company_name.append(span.text.strip())

    for span in soup.find_all('span', class_='JobPosting-labelWithIcon jobposting-location'):
        location= span.text.strip()
        # separates city and state
        if ',' in location:
            split = (location.split(", "))
            # adds city data
            city.append(split[0])
            # adds state data
            state.append(split[1])
        else:
            city.append(location)
            state.append(location)

    df = pd.DataFrame({'job title': job_title, 'company name': company_name, 'salary': salary, 'city': city, 'state': state})
    return df

def part2_DS2() -> pd.DataFrame:
    url= 'https://www.glassdoor.com/Job/data-science-jobs-SRCH_KO0,12.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=data%2520science'
    html = requests.get(url)

    soup = BeautifulSoup(html.content, "html.parser")

    job_title= []
    company_name= []
    city= []
    state= []

    for li in soup.find_all('li', class_='react-job-listing'):
        for div in li.find_all('div', class_='d-flex justify-content-between align-items-start'):
            company_name.append(div.text.strip())
        for a in li.find_all('a', class_='jobLink css-1rd3saf eigr9kq3'):
            for span in a.find_all('span'):
                job_title.append(span.text.strip())
        for div in li.find_all('div', class_='d-flex flex-wrap css-11d3uq0 e1rrn5ka2'):
            for span in div.find_all('span'):
                location= span.text.strip()
                # separates city and state
                if ',' in location:
                    split = (location.split(", "))
                    # adds city data
                    city.append(split[0])
                    # adds state data
                    state.append(split[1])
                else:
                    city.append(location)
                    state.append(location)

    df = pd.DataFrame({'job title': job_title, 'company name': company_name, 'city': city, 'state': state})
    return df

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
