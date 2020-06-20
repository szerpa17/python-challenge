import os
import csv

# Function to return total months, net profit/loss, average change, greatest 
# increase/decrease in profits/losses over the whole period.
def financial_analysis (month_list, profit_list):
    # Total months
    months = len(month_list)
    # Net profit/loss as "total"
    total = sum(profit_list)
    # Average change
    # Created a new list (change) and inserted the difference between 
    # index + 1 and index. This function excludes the last item on 
    # the list (as there is no index + 1 to calculate with).
    change = []
    g_increase = 0
    g_decrease = 0
    inc_month = ""
    dec_month = ""
    for index, profit in enumerate(profit_list):
        if (index == len(profit_list)-1):
            break
        else:
            change_val = (profit_list[index+1]-profit_list[index])
            change.append(change_val)    
        average_change = sum(change)/len(change)        
    # Greatest increase/decrease
    for index, value in enumerate(change):
        if value > g_increase:
            g_increase = value
            inc_month = month_list[index]
        if value < g_decrease:
            g_decrease = value
            dec_month = month_list[index]
    # Reference for currency format: https://stackoverflow.com/questions/320929/currency-formatting-in-python  
    results = ("Financial Analysis" +
                "\n----------------------------" +
                "\nTotal Months: " + str(months) +
                "\nTotal: " + str('${:,.2f}'.format(total)) + 
                "\nAverage Change: " + str('${:,.2f}'.format(average_change)) +
                "\nGreatest Increase in Profits: " + inc_month + " " +
                str('${:,.2f}'.format(g_increase)) +
                "\nGreatest Decrease in Profits: " + dec_month + " " +
                str('${:,.2f}'.format(g_decrease)))
    return results
    

# Identify csv file location
file_path = os.path.join('Resources', 'budget_data.csv')

# Open csv file
with open (file_path, 'r') as csvfile:
    
    # Create csvreader in order to review file contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Create csv header in order to view heading of file contents
    csvheader = next(csvfile)

    # CSV tests
    # print (csvfile)
    # print(csvreader, type(csvreader))
    # print(csvheader, type(csvheader))

    months = []
    total = []

    # Go through every line of the csv
    for row in csvreader:
        months.append(row[0]) 
        profit = int(row[1])
        total.append(profit)
    
analysis = financial_analysis(months, total)
print (analysis)

# Export as text file
output_file = os.path.join("analysis", "output.txt")
with open(output_file, 'w') as textfile:
    writer = text.writer(textfile)
    writer.writelines(analysis)


