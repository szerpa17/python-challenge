import os
import csv

# Insert location of csv file to be used for analysis in the file_path variable
file_path = os.path.join('Resources', 'budget_data.csv')

with open (file_path, 'r') as budget_file:
    # Create budget_reader in order to review file contents
    budget_reader = csv.reader(budget_file, delimiter=',')
    # Create budget header in order to view heading of file contents
    budget_header = next(budget_reader)

    # # Print TextIOWrapper
    # print (budget_file)
    # # Print budged_reader object
    # print(budget_reader, type(budget_reader))
    # Print budget_header
    print(budget_header, type(budget_header))


    
