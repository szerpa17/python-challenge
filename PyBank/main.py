import os
import csv

# Created the financial_analysis function to encompass multiple functions
def financial_analysis (month_list, profit_list):
    # Total months - calculated by creating a list and then finding the length of the list
    months = len(month_list)
    # Net profit/loss - calculated by converting the first column of every row
    total = sum(profit_list)
    # Average change - calculated by creating a new list and appending 
    # the differences between index + 1 and index to identify the change.
    # This function excludes the last item on the list (as there is no 
    # index + 1 to calculate with).
    change = []
    for index, profit in enumerate(profit_list):
        if (index == len(profit_list)-1):
            break
        else:
            change_val = (profit_list[index+1]-profit_list[index])
            change.append(change_val)            
    average_change = sum(change)/len(change)    
    # Greatest increase/decrease - calculated via the use of a conditional
    # in order to assign new values to variables.
    g_increase = 0
    g_decrease = 0
    for index, profit in enumerate(profit_list):
        if profit > g_increase:
            g_increase = profit
        elif profit < g_decrease:
            g_decrease = profit
    results = ("Financial Analysis" +
                "\n----------------------------"
                "\nTotal Months: " + str(months) +
                " \nTotal: " + str(total) + 
                " \nAverage Change: " + str(average_change) +
                " \nGreatest Increase in Profits: " + str(g_increase) +
                " \nGreatest Decrease in Profits: " + str(g_decrease))
    return results
    

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
    # print(csvheader, type(csvheader))

    months = []
    total = []

    # Go through every line of the csv
    for row in csvreader:
        # print(row)
        months.append(row[0][0:3])
        profit = int(row[1])
        total.append(profit)
        
        # Created this conditional to test functions and analyis on the first 3 rows
        # if row[0] == 'Mar-2010':
        #     break
    
    print(financial_analysis(months, total))
