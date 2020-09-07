'''
Author: Ben Lehmann
Function: Years to Months
Date Modified: 9/7/2020
'''
def convert_to_months(age_in_months):
    months = age_in_months
    return months

if __name__ == '__main__':
    age_in_months = (input("Enter an Age:"))
    age_in_years = convert_to_months(int(age_in_months))*12
    print("3 years is "+ str(age_in_years) + " Months") #3 years is 36 months




