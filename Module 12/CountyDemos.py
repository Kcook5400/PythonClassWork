"""
PEP: 8
Title: County_Demos
Author: Kevin Cook
Status: Active
Type: Process
Created: 11-11-2020
Post: 11-11-2020
History:
"""
import csv
class CountyDemos:

    def __init__(self, Rank, County, Per_Capita_income, Median_household_income, Median_Family_Income, Population, Number_of_Households):
        self.Rank = Rank
        self.County = County
        self.Per_Capita_Income= int(Per_Capita_income.replace(',', '').replace('$',''))
        self.Median_household_income = int(Median_household_income.replace(',', '').replace('$',''))
        self.Median_Family_Income = int(Median_Family_Income.replace(',', '').replace('$',''))
        self.Population = Population.replace(',', '')
        self.Number_of_Households = Number_of_Households.replace(',', '')


with open('Iowa 2010 Census Data Population income.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # initialize empty dictionary
    county={}

    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        county[str(row[1])] = CountyDemos(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
    Dallas_county_pop = county['Dallas'].Population
    print("The population of Dallas county is {:,.0f}".format(float(Dallas_county_pop)))



    def DallasCountyInfo(county):
        population = county['Dallas'].Population
        household_num = county['Dallas'].Number_of_Households
        pop_div_house= int(population)/int(household_num)
        print("The population of Dallas county divided by the number of households is {:,.2f}".format(pop_div_house))
        pop_sum=0
        for key in county:
            pop_sum += int(county[key].Population)
        print("The total population of Iowa is {:,.0f}".format(pop_sum))

DallasCountyInfo(county)