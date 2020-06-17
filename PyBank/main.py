import os
import csv

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

    
