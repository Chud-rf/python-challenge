import os
import csv

# File Path
pybank_csv = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('Analysis', 'results.txt')

# Assigning Variables
months_total = 0
profit_loss_total = 0
total_change = 0
prev_value = None
greatest_change = {
    'Date1': '',
    'Increase': 0,
    'Date2': '',
    'Decrease': 0
}

# Reading CSV file
with open(pybank_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvfile, None)

    # Looping through rows
    for row in csvreader:
        months_total+= 1
        profit_loss_total += float(row[1])
        value = float(row[1])

        # Comparing previous profit/loss and adding total
        if prev_value is not None:
            change = value - prev_value
            total_change = total_change + change
            if change > greatest_change['Increase']:
                greatest_change['Increase'] = change
                greatest_change['Date1'] = row[0]
            elif change < greatest_change['Decrease']:
                greatest_change['Decrease'] = change
                greatest_change['Date2'] = row[0]


        prev_value = value

# Printing results to .txt file
with open(output_path, 'w') as outputfile:
    outputfile.write('Financial Analysis\n')
    outputfile.write('------------------------------\n')
    outputfile.write(f'Total Months: {months_total}\n')
    outputfile.write(f"Total: ${round(profit_loss_total)}\n")
    outputfile.write(f"Average Change: ${round(total_change / (months_total - 1), 2)}\n")
    outputfile.write(f"Greatest Increase in Profits: {greatest_change['Date1']} (${round(greatest_change['Increase'])})\n")
    outputfile.write(f"Greatest Decrease in Profits: {greatest_change['Date2']} (${round(greatest_change['Decrease'])})\n")

# Printing results to terminal
print("Financial Analysis")
print("------------------------------")
# Returns 86, like the example output
print(f"Total Months: {months_total}") 
print(f"Total: ${round(profit_loss_total)}")

# Does not match example output without the -1, not sure why.
print(f"Average Change: ${round(total_change / (months_total - 1), 2)}") 
print(f"Greatest Increase in Profits: {greatest_change['Date1']} (${round(greatest_change['Increase'])})")
print(f"Greatest Decrease in Profits: {greatest_change['Date2']} (${round(greatest_change['Decrease'])})")
