# Import OS and CSV
import os
import csv

# Declaring CSV Columns
voter_id = []
county = []

# Declaring variables
votes_cast = 0
candidate_list = set()
cand_per_vote = 0
cand_total_vote = 0
winner = ''
line_break = "-"*30
dct = {}
votes = 0

# Path to collect data from csv in resources folder
poll_csv = os.path.join('Resources','election_data.csv')

# Saving space for functions if necessary

# Read that CSV file! Go go go!
with open(poll_csv, newline='') as csvfile:
	reader = csv.DictReader(csvfile)

	# Interating through the rows
	for row in reader:

		# Appends votes to the unique canidate name
		if row['Candidate'] not in dct:
			dct[row['Candidate']] = []
			dct[row['Candidate']].append(1)
		else:
			dct[row['Candidate']][0] += 1

		# Creating list of unique candidates using previously declared set variable
		candidate_list.add(row['Candidate'])

		# Tracking total number of votes cast
		votes_cast = votes_cast + 1


# Creates and writes variables to a text file


print(candidate_list)
print(votes_cast)
print(dct)
print(dct['Khan'][0])

for person in dct:
	percentage = dct[person][0] / votes_cast
	dct[person].append(percentage)

print(dct)

highest_votes = max([dct[i] for i in dct], key = lambda x: x[1])[0]
winner = [i for i in dct if dct[i][0] == highest_votes]
print(winner[0])


'''
# Creating text file and adding information
textFile = open("poll_file.txt","w")
with open("poll_file.txt", "w") as att_file:
	att_file.write(txt_file_info)
'''