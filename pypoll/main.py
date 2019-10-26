# Pypoll challenge. For this challenge you need to modernize the vote-counting
# process in a small, rural town

# Step 1: Import the necessary modules to work with the .csv file
#         open, create a file object and read file.

import os
import csv

pypoll = os.path.join("election_data.csv")

total_votes=[]
total_candidates=[]

print(f"")
print(f"Election Results")
print(f"-------------------------------")
with open(pypoll, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    # Read and store header
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")

    #Read through a row of data after the header to get the months
    for row in csvreader:

        votes=row[0]
        
        total_votes.append(votes)

        candidates=row[2]

        total_candidates.append(candidates)


# Total number of votes will be the length of any column. In this
# case I am taking the the first column (Voter ID)

total=len(total_votes)
print(f"Total Votes : {total}")
print(f"-------------------------------")

count_khan = total_candidates.count('Khan')
count_corr = total_candidates.count('Correy')
count_li = total_candidates.count('Li')
count_o = total_candidates.count("O'Tooley")

percent_khan= ((int(count_khan) * 100)/int(total))
percent_corr= ((int(count_corr) * 100)/int(total))
percent_li=((int(count_li) * 100)/int(total))
percent_o=((int(count_o) * 100)/int(total))

print(f'Khan: {percent_khan}% ({count_khan})')
print(f'Correy: {percent_corr}% ({count_corr})')
print(f'Li: {percent_li}% ({count_li})')
print(f"O'Tooley: {percent_o}% ({count_o})")
