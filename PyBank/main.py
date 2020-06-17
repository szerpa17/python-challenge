import os
import csv

# Create functions for calculations
# Total months - calculated by creating a list and then finding the length of the list
def total_months(row):
    month = str(row[0])
    month = month[:3]
    months = []
    months.append(month)
    return months, len(months)

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

    # Go through every line of the csv
    for row in csvreader:
        #print(row)
        print(total_months(row))
        # Break inserted to test code on one row
        break