# Pypoll challenge. For this challenge you need to modernize the vote-counting
# process in a small, rural town

# Step 1: Import the necessary modules to work with the .csv file
#         open, create a file object and read file.

import os
import csv

pypoll = os.path.join("election_data.csv")

total_votes=[]

print(f"")
print(f"Election Results")
print(f"-------------------------------")
with open(pypoll, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    # Read and store header
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")

    #Read through each row of data after the header to get the months
    for row in csvreader:

        votes=row[0]
        
        total_votes.append(votes)

        # total=row[1]

        # total_list.append(total)


# Total number of votes will be the length of any column. In this
# case I am taking the the first column (Voter ID)

print(f"Total Votes : {len(total_votes)}")
print(f"-------------------------------")