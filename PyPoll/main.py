# Import OS and CSV
import os
import csv

# Declaring variables
votes_cast = 0
winner = ''
line_break = "-"*30
dct = {}
candidate_list = []

# Path to collect data from csv in resources folder
poll_csv = os.path.join('Resources','election_data.csv')

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

		# Tracking total number of votes cast
		votes_cast = votes_cast + 1


# Formatting vote percentages into percentages properly
for person in dct:
	percentage = "{:.3f}%".format(dct[person][0] / votes_cast * 100)
	dct[person].append(percentage)

# Grabbing the highest vote count, associating it with the correct key, to be used when printing out the text file.
highest_votes = max([dct[i] for i in dct], key = lambda x: x[1])[0]
winner = [i for i in dct if dct[i][0] == highest_votes]

# Grabbing the keys from the dictionary to use in writing the text file.
for cand in dct:
	candidate_list.append(cand)

# One lining the text file yaaay
txt_file_info = f"Election Results"'\n'f"{line_break}"'\n'f"Total Votes: {votes_cast}"'\n'f"{line_break}"'\n'f"{candidate_list[0]}: {dct[candidate_list[0]][1]} ({dct[candidate_list[0]][0]})"'\n'f"{candidate_list[1]}: {dct[candidate_list[1]][1]} ({dct[candidate_list[1]][0]})"'\n'f"{candidate_list[2]}: {dct[candidate_list[2]][1]} ({dct[candidate_list[2]][0]})"'\n'f"{candidate_list[3]}: {dct[candidate_list[3]][1]} ({dct[candidate_list[3]][0]})"'\n'f"{line_break}"'\n'f"Winner: {winner[0]}"
print(txt_file_info)


# Creating text file and adding information
text_file = open("poll_file.txt","w")
with open("poll_file.txt", "w") as att_file:
	att_file.write(txt_file_info)
