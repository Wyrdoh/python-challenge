#calculating th average change
#defineing monthly changes as an empty list because we will be adding the profit changes in it
monthly_changes = []
previous_month_profit = int(rows[0][1])
for i in range(1, len(rows)):
#     #current month profit will be the month after the first which will have index of [i] and we itrating starting from the second element of the list
#     #the row[1] means we are looking at the value profit inside the sublist[[month0,value0]<==i=0,[month1,value1]<==i=1,[month2,value2]i<== 2 ....]===>[]
     current_month_profit = int(rows[i][1])
#     #monthly change will be the value of the current month - previous month will be taking the previous value and it will take the value of the current
#     #because the current one will be the previous one in the next itration
     monthly_change = current_month_profit - previous_month_profit
#     #we need to save those changes in a list which i called monthly_changes and we add values by calling the .append function which adds the new values to the list.
     monthly_changes.append(monthly_change)
#     #now we define the previous month profit by assigning it to the current month
     previous_month_profit = current_month_profit
# #calculating the average *note we -1 from the total number of moths because the first month value has no previos value !!
average_monthly_change = sum(monthly_changes) / (total_number_of_months - 1)
rounded_average_change = round(average_monthly_change, 2)
print(f'Average Change: ${rounded_average_change}')
#===================================================================

# the comprehension version of the for loop
# monthly_changes = [int(rows[i][1]) - int(rows[i-1][1]) for i in range(1, len(rows))]
# average_monthly_change = sum(monthly_changes) / (len(rows) - 1)
# rounded_average_change = round(average_monthly_change, 2)
# print(f'Average Change: ${rounded_average_change}')