# Pybank challenge. For this challenge you need analyze the
# financial records of a company.

# Step 1: Import the necessary modules to work with the .csv file
#         open, create a file object and read file.

import os
import csv
import math as m
import numpy as np

pybank = os.path.join("budget_data.csv")

months_list=[]
total_list=[]
# pybank = open("budget_data.csv")
print(f"")
print(f"-------------------------------")
print(f"Financial Analysis")
print(f"-------------------------------")
with open(pybank, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    # Read and store header
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")

    #Read through each row of data after the header to get the months
    for row in csvreader:

        rows=row[0]
        
        months_list.append(rows)

        total=row[1]

        total_list.append(total)
        
               
# print total number of months in the dataset 
totalmonth = len(months_list)
print(f"Total Months: {totalmonth}")


total_list_int=list(map(int,total_list))


# print net total amount of "Profit/Losses"
totalsum = m.fsum(total_list_int)
print(f"Total: ${totalsum}")

# calculate ( (n+1) - n ) average change using numpy module (diff function)
diff_list = np.diff(total_list_int)

# calculate average
avg_diff = np.average(diff_list)

# print average using numpy module (avg function)
print(f"Average Change: ${avg_diff}")

# calculate greatest increase in profits
max_prof = max(diff_list)

# calculate greatest decrease in losses
max_loss = min(diff_list)

# to get the index associated with the max_prof and max_loss convert array
# into a list and get the index. Make sure you add 1 to account for the differences
# in length

list_conv = list(diff_list)

# index calculation for profits
i = list_conv.index(max_prof) + 1

# index calculation for losses
j = list_conv.index(max_loss) +1
#index_profit = np.where(diff_list == max_prof)

print(f"Greatest Increase in Profits: {months_list[i]} (${max_prof})")
print(f"Greatest Decrease in Profits: {months_list[j]} (${max_loss})")




