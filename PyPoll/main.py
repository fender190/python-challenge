# PyPoll Homework

# Import OS and CSV
import os
import csv

# Open the data file
csvpath = os.path.join("election_data.csv")

# Read with CSV Reader
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Skipp Header Row
    file_header = next(csvreader)

    # votes counter, set to start at 0
    votes_total = 0

    # Store candidates fron candidate column
    candidate = []
        
    # iterates through all rows
    for row in csvreader:

        #store all
        #count total number of votes
        candidate.append(row[2])
        votes_total +=1

    # Get each candidate    
    # Calculate each candidates vote
    candidate_count = [[x ,candidate.count(x)] for x in set(candidate)]
    
    # list for storing votes count for each candidate
    votes_count = []
    candidates_name = []
    
    # Iterates through each row for each candidate name and vote count
    for row in candidate_count:
        candidates_name.append(row[0])
        votes_count.append(row[1])

    candidate_zip = zip(candidates_name, votes_count)
    candidate_list = list(candidate_zip)

    # Gets the winner, candidate with the most votes
    winner = max(votes_count)

    # Iterates for each row in the candidate list
    for row in candidate_list:
        if row[1] == winner:
            winner_name = row[0] 
            
#votes total for candidates        
total_votes = len(candidate)

# Get results for each candidate, Correy
correy_total = candidate.count('Correy')
correy_percent = int(correy_total) / int(total_votes)

# Get results for O' Tooley
o_tooley_total = candidate.count("O'Tooley")
o_tooley_percent = o_tooley_total / total_votes

# Get results for Li
li_total = candidate.count('Li')
li_percent = li_total / total_votes

# Get results for Khan
khan_total = candidate.count('Khan')
khan_percent = khan_total / total_votes

# print all results
print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(votes_total))
print('-------------------------')
print(f'Khan: {khan_percent:.3%} ({khan_total})')
print(f'Correy: {correy_percent:.3%} ({correy_total})')
print(f'Li: {li_percent:.3%} ({li_total})')
print(f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley_total})")
print('-------------------------')
print(f'Winner: {winner_name}')
print('-------------------------')

# Specifed the file to write to
output_path = os.path.join("PypollC.csv")

# Open file using Write mode
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['------------------------'])
    csvwriter.writerow(['Total Votes: ' + str(votes_total)])
    csvwriter.writerow(['------------------------'])
    csvwriter.writerow([f'Khan: {khan_percent:.3%} ({khan_total})'])
    csvwriter.writerow([f'Correy: {correy_percent:.3%} ({correy_total})'])
    csvwriter.writerow([f'Li: {li_percent:.3%} ({li_total})'])
    csvwriter.writerow([f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley_total})"])
    csvwriter.writerow(['--------------------------'])
    csvwriter.writerow([f'Winner: {winner_name}'])
    csvwriter.writerow(['---------------------'])
 


