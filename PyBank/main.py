import os
import csv

# Create functions for calculations
# Total months - calculated by creating a list and then finding the length of the list
def total_months(months_list):
    months = len(month_list)
    return months_list, len(months)

# Net profit/loss - calculated by converting the first column of every row
def net_total(profit_list):
    total = sum(profit_list)
    return total

# Insert location of csv file to be used for analysis in the file_path variable
file_path = os.path.join('Resources', 'budget_data.csv')

# Open the file
with open (file_path, 'r') as csvfile:
    # Create csvreader in order to review file contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Create csv header in order to view heading of file contents
    csvheader = next(csvfile)

    # # Print TextIOWrapper
    # print (csvfile)
    # # Print csvreader object
    # print(csvreader, type(csvreader))
    print(csvheader, type(csvheader))

    months = []
    total = []

    # Go through every line of the csv
    for row in csvreader:
        #print(row)
        months.append(row[0][0:3])
        profit = int(row[1])
        total.append(profit)
        # print(months, total)
        # print(total_months(months))
        # print(net_total(total))
        
        # Created this conditional to test functions and analyis on the first 3 rows
        if row[0] == 'Mar-2010':
            break