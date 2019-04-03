import os
import csv

csvpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
'..', 'Resources', 'budget_data.csv')

total_month = []
total_profit = []
monthly_change = []

with open(csvpath, newline="") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")

    print("```text")
    print("Financial Analysis")
    print("-------------------------------")

    # Skip the header
    next(csvreader, None)
    
    for row in csvreader: 
        total_month.append(row[0])
        total_profit.append(int(row[1]))

    for x in range(len(total_profit) - 1):
        monthly_change.append(int(total_profit[x+1] - total_profit[x]))
    
    num_month = len(total_month)
    average = round(sum(monthly_change) / len(monthly_change), 2)
    greatest_increase = max(monthly_change)
    greatest_decrease = min(monthly_change)

    index_max_month = monthly_change.index(max(monthly_change)) + 1
    index_min_month = monthly_change.index(min(monthly_change)) + 1

    print("Total Months: " + str(num_month))
    print("Total: $" + str(sum(total_profit)))
    print("Average Change: $" + str(average))
    print("Greatest Decrease in Profits: " + total_month[index_max_month] + 
            " ($" + str(greatest_increase) + ")")
    print("Greatest Increase in Profits: " + total_month[index_min_month] + 
            " ($" + str(greatest_decrease) + ")")
    print("```")
    

with open ("result_budget.txt", "w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("-------------------------------")
    file.write("\n")
    file.write("Total Months: " + str(num_month))
    file.write("\n")
    file.write("Total: $" + str(sum(total_profit)))
    file.write("\n")
    file.write("Average Change: $" + str(average))
    file.write("\n")
    file.write("Greatest Decrease in Profits: " + total_month[index_max_month] + 
            " ($" + str(greatest_increase) + ")")
    file.write("\n")
    file.write("Greatest Increase in Profits: " + total_month[index_min_month] + 
            " ($" + str(greatest_decrease) + ")")
    file.write("\n")
    file.write("```")
