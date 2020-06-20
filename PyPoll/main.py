import os
import csv

# Lists
candidates = []
votes = []
candidate_dict = {}
unique_candidates = []


# Create function to apply to the voter data
def election_results(candidates, votes):

    for row in candidates:
        if row not in unique_candidates:
            unique_candidates.append(row)
    # Total number of votesS
    t_votes = len(votes)
    # Put unique candidate info into a dictonary
    for x in range(len(unique_candidates)):
        candidate_dict[unique_candidates[x]] = 0
    # Idenfity votes each candidate received
    for x in range(len(votes)):
        candidate_dict[candidates[x]] += 1
    # Create dictionary to keep track of candidates, 
    # setting all votes to zero
    candidate_data = ""
    maxvotes = 0
    winner = ""
    for key,value in candidate_dict.items():
        candidate_data += (f"\n{key}: {round((value/t_votes)*100, 2)} ({value})")
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
    

    

#     t_votes = len(votes)
#     results = " "
#     # Capture the names of the candidates in a list
    
#     # Each candidate obtains their own variable for every step below
    
# #Test
# candidates = []
#     if 'Billy' not in candidates:
#        candidates.append('Billy')
#     print(candidates)

        

#     # Count total number of votes cast by finding the list length
#     # Compile list of candidates who received votes by identifying unique values in the list (research)
#     # Identify the total number of votes each candidate won 
#     # Calculate percentage of votes each candidate won     
#     # The winner of the election based on popular vote
    



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
        if row[0] == 19865775:
          break
        # Test function on the first few rows
        votes.append(row[0])
        candidates.append(row[2])
#Debuging
#print(*candidates)
print(election_results(candidates, votes))
        #print(row)
# for x in range(len(candidates)):
#     candidate_dict[candidates[x]] = 0
# print (candidate_dict)
# #print (candidate_dict['Candidate 1'] = {candidates})
# print("Test2")
# for key in candidate_dict:
#     print(key)
        
        
# for x in range(len(candidates)):
#     if candidates(x) not in candidate_dict:
#         candidate_dict[candidates[x]] = 0
# # Idenfity votes each candidate received
# for x in range(len(votes)):
#     if candidates(x) == candidate_dict[candidates(x)]:
#         candidate_dict[candidates[row]] += 1    
# print(candidate_dict)
#print election_results(row)