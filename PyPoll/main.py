import os
import csv

# File Path
pypoll_csv = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join('Analysis', 'results.txt')

# Assigning Variables
votes_total = 0
first_candidate = 0
second_candidate = 0
third_candidate = 0
other_votes = 0
winner = ''

# Reading CSV file
with open(pypoll_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvfile, None)

    # Looping through rows
    for row in csvreader:
        votes_total += 1

        if row[2] == 'Charles Casper Stockham':
            first_candidate += 1
        elif row[2] == 'Diana DeGette':
            second_candidate += 1
        elif row[2] == 'Raymon Anthony Doane':
            third_candidate += 1
        else:
            other_votes += 1

# Finding the winner
if first_candidate > second_candidate and first_candidate > third_candidate:
    winner = 'Charles Casper Stockham'
elif second_candidate > first_candidate and second_candidate > third_candidate:
    winner = 'Diana DeGette'
elif third_candidate > first_candidate and third_candidate > second_candidate:
    winner = 'Raymon Anthony Doane'

# Final votes percentages
first_percent = round((first_candidate / votes_total) * 100, 3)
second_percent = round((second_candidate / votes_total) * 100, 3)
third_percent = round((third_candidate / votes_total) * 100, 3)

# Printing results to .txt file
with open(output_path, 'w') as outputfile:
    outputfile.write('Election Results\n')
    outputfile.write('--------------------------\n') 
    outputfile.write(f'Total Votes: {votes_total}\n--------------------------\n')
    outputfile.write(f'Charles Casper Stockham: {first_percent}% ({first_candidate})\n')
    outputfile.write(f'Diana DeGette: {second_percent}% ({second_candidate})\n')
    outputfile.write(f'Raymon Anthony Doane: {third_percent}% ({third_candidate})\n')
    outputfile.write('--------------------------\n')
    outputfile.write(f'Winner: {winner}\n')
    outputfile.write('--------------------------\n')


# Printing final results to terminal
print('Election Results\n--------------------------')
print(f'Total Votes: {votes_total}\n--------------------------')
print(f'Charles Casper Stockham: {first_percent}% ({first_candidate})')
print(f'Diana DeGette: {second_percent}% ({second_candidate})')
print(f'Raymon Anthony Doane: {third_percent}% ({third_candidate})')
print('--------------------------')
print(f'Winner: {winner}')
print('--------------------------')
