import os
import csv
divider = ('-' * 50)
voter_id = []
votes = []
candidates = []
output = open('output.txt', 'w')
election_csv = os.path.join('..', '..', 'Instructions', 'PyPoll', 'Resources', 'election_data.csv')
with open(election_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # '${:,}'.format(total_votes)
    for row in csvreader:
        voter_id.append(row[0])
        votes.append(row[2])
        if row[2] not in candidates:
            candidates.append(row[2])
total_votes = '{:,}'.format(len(votes))
print(f'Election Results')
print(divider)
print(f'Total Votes: {total_votes}')
print(divider)
for candidate in candidates:
    tally = '{:,}'.format(votes.count(candidate))
    share = '{0:.2f}%'.format((votes.count(candidate) / len(votes)) * 100)
    print(f'{candidate}: {share} ({tally})')
print(divider)
print(f'Winner: {max(set(votes), key= votes.count)}')