import csv
import os

file_path = os.path.join('Resources' , 'election_data.csv')

with open(file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    line_count = 0

    candidate_votes = {}

    for row in csv_reader:
        line_count += 1

        # continue if header row
        if line_count == 1:
            continue

        candidate = row[2]
        
        # task 2 - list candidates that received votes
        if candidate not in candidate_votes.keys():
            candidate_votes[candidate] = 1 
        else: 
            candidate_votes[candidate] +=1 

total_votes = line_count - 1

print(f'Total Votes: {total_votes}')
winning_candidate = None
winning_candidate_votes = 0

for candidate in candidate_votes.keys():
    vote_count = candidate_votes[candidate]
    vote_percent = round(vote_count/total_votes*100,2)

    if vote_count > winning_candidate_votes:
        winning_candidate = candidate
        winning_candidate_votes = vote_count

    print(f'{candidate}: {vote_percent}% ({vote_count})')
print(f'Winner: {winning_candidate}')

 #output analysis

output_path = os.path.join('Analysis' , 'results.txt')

with open (output_path, 'w') as txtfile:
    txtfile.write(f'Total Votes: {total_votes})\n')
    txtfile.write(f'{candidate}: {vote_percent}% ({vote_count}))\n')
    txtfile.write(f'Winner: {winning_candidate})\n')
