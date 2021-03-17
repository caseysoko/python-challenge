# Assignment for PyBank
# Calculate
# total number of months in data set
# net total amt of Profit/Losses over entire period
# changes in profit/losses and find average of changes
# greatest increase in profits for entire period - include date and amount
# greatest decrease in losses for entire period - include date and amount

import os
import csv

months = []
total_month = 0
total_amount = 0
previous_amount = 0
current_change = 0
total_change = 0
average_change = 0
greatest_increase = 0
overall_increase = ""
greatest_decrease = 0
overall_decrease = ""
value_col = 1
month_col = 0

csv_path = os.path.join('Resources', 'budget_data.csv')

with open(csv_path, newline="") as csvfile:
    budget_reader=csv.reader(csvfile,delimiter=",")
    budget_header=next(budget_reader)

    for row in budget_reader:
        total_month = total_month + 1 

        total_amount = total_amount + int(row[value_col])

        current_change = int(row[value_col]) - previous_amount
        if previous_amount != 0:
            total_change = total_change + current_change
        previous_amount = int(row[value_col])

        if current_change>greatest_increase:
            greatest_increase=current_change
            overall_increase = row[month_col]
        if current_change<greatest_decrease:
            greatest_decrease=current_change
            overall_decrease=row[month_col]
        
        if total_month != 1:
            average_change=round((total_change/(total_month-1)),2)
        
        print("Financial Analysis")
        print("------------------")
        print(f'Total Months: {total_month}')
        print(f'Total Profit/Loss: ${total_amount}')
        print(f'Average Profit/Losses Change: ${average_change}')
        print(f'Greatest Increase: {overall_increase} ${greatest_increase}')
        print(f'Greatest Decrease: {overall_decrease} ${greatest_decrease}')

        output_path=os.path.join("Output","PyBankAnalysis.txt")
        output_file=open(output_path,"w")

       

            
    



