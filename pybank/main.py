# Pybank challenge. For this challenge you need analyze the
# financial records of a company.

# Step 1: Import the necessary modules to work with the .csv file
#         open, create a file object and read file.

import os
import csv

pybank = os.path.join("budget_data.csv")

months_list=[]
# pybank = open("budget_data.csv")

with open(pybank, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    # Read and store header
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")

    #Read through each row of data after the header
    for row in csvreader:

        rows=[row[0]]
        
        months_list.append(rows)
        
        
print(len(months_list))