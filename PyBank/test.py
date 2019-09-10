# Import things and stuff 
import os
import csv

# Declaring CSV Columns
date = []
profLoss = []

# Declaring Variables
totalMonths = 0
netTotal = 0
avgChange = 0
greatestIncreaseDate = ''
greatestIncreaseTotal = 0
greatestDecreaseDate = ''
greatestDecreaseTotal = 0

# Path to collect data from the resources folder
bankCsv = os.path.join('Resources','budget_data.csv')

# Read in the CSV file
with open(bankCsv, newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		# print(row['Date'], row['Profit/Losses'])

		# Iterate each month
		totalMonths = totalMonths + 1

		# Add all totals
		netTotal = netTotal + int(row['Profit/Losses'])


'''
Old Method
# Read in the CSV file
with open(bankCsv, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	header = next(csvreader)

	print("Financial Analysis")
	print("-"*30)

	for row in csvreader:

		date.append(row[0])

		profLoss.append(int(row[1]))
	
		# Greatest Increase conditional
		value = int(row[1])
		if greatestIncreaseTotal < value:
			greatestIncreaseTotal = value
			greatestIncreaseDate = row[0]

		# Greatest Decrease conditional
		if greatestDecreaseTotal > value:
			greatestDecreaseTotal = value
			greatestDecreaseDate = row[0]
		
		totalMonths = totalMonths + 1
		netTotal = netTotal + int(row[1])
'''




print(f"Total months: {totalMonths}")
print(f"Total: {netTotal}")
avgChange = 0
print(f"Average Change: {avgChange}")
print(f"Greatest increase in Profits: {greatestIncreaseDate} {greatestIncreaseTotal}")
print(f"Greatest decrease in Profits: {greatestDecreaseDate} {greatestDecreaseTotal}")

'''
with open(bankCsv, 'r') as csvfile:
	a = [{k: str(v) for k, v in row.items()}
		for row in csv.DictReader(csvfile, skipinitialspace=True)]

	print(a[0].get('Date'))
'''
	# csvreader = csv.reader(csvfile, delimiter=',')
	# header = next(csvreader)

	# print("Financial Analysis")
	# print("-"*30)
	# 



lst = ['a','a','b','b','b','b','c','d','c','z','e','a','f']
occurences_dct = {}

for i in lst:
	if i not in occurences_dct:
		occurences_dct[i] = 1
	else:
		occurences_dct[i] += 1

print(occurences_dct)

lst2 = [['z', 9], ['a', 101], ['b', 2]]

lst2.sort(key = lambda x: x[1])
print(sorted(lst2, key = lambda x: x[1]))
print(lst2)
print(max(lst2, key = lambda x: x[1]))
print(max(lst2, key = lambda x: x[1])[0])

highest_votes = max([dct[i] for i in dct], key = lambda x: x[1])[0]
winner = [i for i in dct if dct[i][0] == highest_votes]
print(winner[0])
