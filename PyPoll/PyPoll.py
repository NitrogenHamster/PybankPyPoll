import csv

# Files to load and output (Remember to change these)
file = "Resources/election_data.csv"

all_votes = 0
all_candidates = 0
candidate_list = []
candidate_votes = {}
maxvotes = -1

# Read the csv and use it 
with open(file) as poll_data:
    reader = csv.DictReader(poll_data)
    
    for row in reader:
        current_person = row['Candidate']
        if current_person not in candidate_list :
            all_candidates = all_candidates + 1
            candidate_list.append(current_person)
            candidate_votes[current_person] = 0
            
        candidate_votes[current_person]=candidate_votes[current_person]+1
        all_votes = all_votes + 1
        
        if candidate_votes[current_person] > maxvotes :
            maxvotes = candidate_votes[current_person]
            maxcandidate = current_person

print('Election Results')
print("-------------------------------")
print("Total Votes " + str(all_votes))
print("-------------------------------")

for name in candidate_list :
    print(name + " : " + str(round(100*candidate_votes[name]/(0.0+all_votes),2)) + '% ' +  str(candidate_votes[name]))

print("-------------------------------")
print("Winner: " + str(maxcandidate))
print("-------------------------------")
 