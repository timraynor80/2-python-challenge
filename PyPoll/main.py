import os
import csv
divider = ('-' * 50)
election_csv = os.path.join('..', '..', 'Instructions', 'PyPoll', 'Resources', 'election_data.csv')
with open(election_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # for row in csvreader:
    #     print(row)
    print(csv_header)

# print(f'Election Results')
# print(divider)