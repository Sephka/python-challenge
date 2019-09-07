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



# # Creating a function
# def bankingInfo(bankData):

def mean(numbers):
	return float(sum(numbers)) / max(len(numbers), 1)
	
# 	# Creating variables
# 	date = str(bankData[0])
# 	netTotal = int(bankData[1])

# 	# Total number of months in dataset
# 	totalMonths = len(date)
# 	print(totalMonths)


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


	print(f"Total months: {totalMonths}")
	print(f"Total: {netTotal}")
	avgChange = mean(profLoss)
	print(f"Average Change: {avgChange}")
	print(f"Greatest increase in Profits: {greatestIncreaseDate} {greatestIncreaseTotal}")
	print(f"Greatest decrease in Profits: {greatestDecreaseDate} {greatestDecreaseTotal}")

	textFile = open("bankFile.txt","w")
	with open("bankFile.txt", "w") as att_file:
		att_file.write(str(lMonths) + "\n")




