# Pybank challenge. For this challenge you need analyze the
# financial records of a company.

# Step 1: Import the necessary modules to work with the .csv file
#         open, create a file object and read file.

import os
import csv
import math as m

pybank = os.path.join("budget_data.csv")

months_list=[]
total_list=[]
# pybank = open("budget_data.csv")

with open(pybank, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    # Read and store header
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")

    #Read through each row of data after the header to get the months
    for row in csvreader:

        rows=[row[0]]
        
        months_list.append(rows)

        total=[row[1]]

        total_list.append(total)
        
    # print total number of months in the dataset   
print(f"The total number of months in the dataset is {len(months_list)}")


flattened=[]

for sublist in total_list:
    for val in sublist:
        flattened.append(val)


flattened=list(map(int,flattened))


# print net total amount of "Profit/Losses"
print(f"The net total amount of Profit/Losses in the dataset is equal to {m.fsum(flattened)}")

