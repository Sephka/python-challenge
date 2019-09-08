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
def candidate_votes(poll_data):

	# Assigning values to variables
	votes = 0
	candidate = set(poll_data['Candidate'])
	votes = votes + 1

	# Assign to dictionary the candidates and their votes

# Read that CSV file! Go go go!
with open(poll_csv, newline='') as csvfile:
	reader = csv.DictReader(csvfile)

	# Interating through the rows
	for row in reader:

		candidate_votes(row)

		# Creating list of unique candidates using previously declared set variable
		candidate_list.add(row['Candidate'])


		# Tracking total number of votes cast
		votes_cast = votes_cast + 1


# Creates and writes variables to a text file
print(candidate_list)
print(votes_cast)
print(dct)

'''
# Creating text file and adding information
textFile = open("poll_file.txt","w")
with open("poll_file.txt", "w") as att_file:
	att_file.write(txt_file_info)
'''