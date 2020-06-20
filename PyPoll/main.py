import os
import csv

# Create function to apply to the voter data
def election_results():
    votes = []

    results = " "
    # Capture the names of the candidates in a list
    
    # Each candidate obtains their own variable for every step below
    
    # Count total number of votes cast by finding the list length
    # Compile list of candidates who received votes by identifying unique values in the list (research)
    # Identify the total number of votes each candidate won 
    # Calculate percentage of votes each candidate won     
    # The winner of the election based on popular vote
    
    results = ("Election Results" +
                "\n-------------------------" +
                f"\nTotal Votes: {t_votes}" +
                "\n-------------------------" +
                "\n" +
                "\n-------------------------" +
                f"\nWinner: {winner}" +
                "\n-------------------------")


# Insert location of csv file to be used for analysis in the file_path variable
file_path = os.path.join('Resources', 'election_data.csv')

# Open the file
with open (file_path, 'r') as csvfile:
    # Create csvreader in order to review file contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Create csv header in order to view heading of file contents
    csvheader = next(csvfile)

    # Go through every line of the csv
    for row in csvreader:
        # Insert function

        #print(row)
        
        # Test function on the first 3 rows
        # if row[0] == 
        #     break
    
# print function