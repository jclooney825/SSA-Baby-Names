from record import Record 
from database import Database
import matplotlib.pyplot as plt 

''' 
This program analyzes baby names from annual 
data from the SSA ranging from 1880 to 2020. 

# SSA Baby Name data 
https://www.ssa.gov/oact/babynames/limits.html


July 20, 2021 
'''

# Menu method for 
def menu():

    # Start and end years 
    start, end = 1920,  2020

    # Database object 
    db = Database('names', start, end)

    while True:
        print('                 Menu                   ')
        print('----------------------------------------')
        print('1. Top 10 female names for a given year')
        print('2. Top 10 male names for a given year')
        print('3. Plot female name by year')
        print('4. Plot male name by year')
        print('5. Exit')
        print('Choose an option:')
        print()
        
        try: 
            option = int(input())
            
        except ValueError:
            print('Please enter a valid option. ')
            print()
            continue 

        if option == 1:
            sex = 'F'
            print( 'Enter year:')
            year = int(input())
            recs = db.top_ten(sex, year, 10)
            top_names(recs , year)

        elif option == 2:
            sex = 'M'
            print( 'Enter year:')
            recs = db.top_ten(sex, year, 10)
            top_names(recs, year)

        elif option == 3:   
            print('Enter a female name:')
            name = input()
            sex = 'F'
            recs = db.selectAllNameRecords(name, sex)
            plot_results(recs, name)   

        elif option == 4:   
            print('Enter a male name:')
            name = input()
            sex = 'M'
            recs = db.selectAllNameRecords(name, sex)
            plot_results(recs, name)  

        elif option == 5:
            break
        else:
            print('Please enter a valid option.')
            print()

# Plots the number of babies named for a given name input
def plot_results(recs, name):
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['font.family'] = 'STIXGeneral'

    if len(recs) == 0:
        print("No babies named " + name)
        return 

    years = [rec.year for rec in recs]
    count = [rec.num for rec in recs]
    
    plt.plot(years, count)
    plt.title(f'{name} Babies By Year')
    plt.grid(True)
    plt.xlabel('Years')
    plt.ylabel('Number of babies')
    plt.show()

# Prints the top ten names for a given year 
def top_names(recs, year):
    print()
    print(f'   Most popular Baby Names for {year}  ')
    print('----------------------------------------')
    for i in range(len(recs)):
        print(f'{i + 1}.{recs[i].name}')
    print()


if __name__ == '__main__':
    menu()