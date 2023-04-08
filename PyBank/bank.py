# Import Dependencies
import os
import csv

# Create empty lists to iterate through specific rows for the following variables
total_months = []
total_profit = []
monthly_profit_change = []
csvpath = os.path.join("Resources", "budget_data.csv")
# Open csv in default read mode with context manager
with open(csvpath, "r") as csvfile:
     # Store the contents of budget_data.csv in the variable csvreader
    csvreader = csv.reader(csvfile,delimiter=",")
    # Skip the header labels to iterate with the values
    header = next(csvreader)
    # Iterate through the rows in the stored file contents
    for row in csvreader:
        # Append the total months and total profit to their corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(total_profit)-1):
        # Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
# Obtain the max and min of the the montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)
# Correlate max and min to the proper month using month list and index from max and min
#We use the plus 1 at the end since month associated with change is the + 1 month or next month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1
#Print Statements
# Print Statements
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
#Output files
# Output files
output_file = "./Analysis/budget_analysis.txt"
with open(output_file,"w") as file:
#Write methods to print to Financial_Analysis_Summary
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {len(total_months)}\n")
    file.write(f"Total: ${sum(total_profit)}\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})\n")



















# ORIGINAL CODE ***************************************

# # Import modules
# import os
# import csv

# total_months = []
# net_total = []
# monthly_changes = []

# # Setting the csv path and creating a variable from it. The .join is telling the script to join the the csv elements into a string, in which I set the delimeter later
# # bank_csv = os.path.join('..', '/Users/deronpayton/Desktop/python-challenge/PyBank/Resources/budget_data.csv')
# bank_csv = os.path.join("Resources", "budget_data.csv")
# bank_results = os.path.join("Analysis", "bank_results.txt")
    
# # CSV reader specifies the delimiter and variable that hold the contents of the CSV. The .open function is opening the file and returning it as a file object(provides methods and attributes
# # to access and manipulate files). The .reader module can then iterate over that file object.
# with open(bank_csv, 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter = ',')     
#     # Read the header row, telling the script to skip this line and start counting entries after this one. 
#     csv_header = next(csv_reader)
#    # Iterate through the rows in the opened object file
#     for row in csv_reader:
#         total_months.append(row[0])
#         net_total.append(int(row[1]))
#     # Iterate through the profits in order to get the monthly changes
#     for i in range(len(net_total)-1):
#         # Take the difference between the two months and append to monthly change
#         monthly_changes.append(net_total[i+1]-net_total[i])




# # Done with importing csv
# print("=======================================")
    
# # Need to calculate the total number of months included in the dataset by counting the length of the total rows, skipping the header. 
# # total_months = len(rows)
# # print(f'Total Months: {total_months}')

# # Calculate the net total amount of "Profit/Losses" over the entire period. Set net_total variable to 0 as a default place to start counting. Calculate total by iterating 
# # for row in rows:
# #     total = int(row[1])
# #     net_total = net_total + total
# # print(f'Net total is: ${net_total:,}')
# # # Finished calculating net total
# # print("=======================================")

# # Calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes


#     # Add all the values in column index 1
#     # So I need to find the column, grab first value and name it to a variable?
#     # Then add that number to the next row down, get new value and then add that to the next row and so on
#     # Once all rows are added together, divide that number by the total rows/months






# # monthly_changes = (f"sum{net_total} / len{total_months}", 2)
# # print(monthly_changes)

# # Calculate the greatest increase in profits (date and amount) over the entire period
# # max_increase = max(f"{monthly_changes}")
# # max_decrease = min(f"{monthly_changes}")

# # Calculate the greatest decrease in profits (date and amount) over the entire period

