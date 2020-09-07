def convert_to_months(age_in_years):

 return age_in_years*12


if __name__ == '__main__':

    age_in_years = int(input("Enter your age in years"))
    age_in_months = convert_to_months(age_in_years)
    print(age_in_months)