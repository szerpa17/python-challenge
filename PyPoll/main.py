import os
import csv

# Lists
candidates = []
votes = []
candidate_dict = {}
unique_candidates = []


# Create function to apply to the voter data
def election_results(candidates, votes):
    
    # Identify unique candidates
    for row in candidates:
        if row not in unique_candidates:
            unique_candidates.append(row)
    
    # Identify total number of votes
    # Each item in the votes list is a vote
    t_votes = len(votes)
    
    # Put unique candidate info into a dictonary
    # Set the value for each candidate to 0
    # The value will be later updated with the candidate's vote
    for x in range(len(unique_candidates)):
        candidate_dict[unique_candidates[x]] = 0

    # Idenfity votes each candidate received
    for x in range(len(votes)):
        candidate_dict[candidates[x]] += 1
    
    # Variables for the candidate specific data output
    candidate_data = ""
    winner = ""
    maxvotes = 0
    
    # Pull each candidate's name, percentage of total votes, and total votes
    # from dictionary
    # Use the same for loop to update the winner and maxvotes variables
    for key,value in candidate_dict.items():
        candidate_data += (f"\n{key}: {round((value/t_votes)*100, 2)}% ({value})")
        if value > maxvotes:
            winner = key
            maxvotes = value
    
    results = ("Election Results" +
            "\n-------------------------" +
            f"\nTotal Votes: {t_votes}" +
            "\n-------------------------" +
            candidate_data +
            "\n-------------------------" +
            f"\nWinner: {winner}" +
            "\n-------------------------")
    
    return results    

# File location
file_path = os.path.join('Resources', 'election_data.csv')

# Open the file
with open (file_path, 'r') as csvfile:
    # Create csvreader in order to review file contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Create csv header in order to view heading of file contents
    csvheader = next(csvfile)

    # Go through every line of the csv
    for row in csvreader:
        # Add values to votes and candidates list
        votes.append(row[0])
        candidates.append(row[2])
print(election_results(candidates, votes))
