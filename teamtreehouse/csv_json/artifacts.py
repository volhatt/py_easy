import csv
## to read from file
with open('E:\\code\\test\\museum.csv', newline='') as csvfile:
	# artreader = csv.reader(csvfile, delimeter ='|')
	# row = list(artreader)
	# for row in rows[:2]:
	# 	print(', '.join(row))


	## update to dictionary
	artreader = csv.DictReader(csvfile, delimiter ='|')
	rows = list(artreader)
	for row in rows[1:2]:
		print(', '.join(row['group1']))



## to create CSV file with digtinary
with open('E:\\code\\test\\teachers.csv', 'a') as csvfile:
	fieldnames = ['first_name', 'last_name', 'topic']
	teachwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

	teachwriter.writeheader()
	teachwriter.writerow({
		'first_name': 'Olga',
		'last_name': 'Love',
		'topic': 'Python'
		})
	teachwriter.writerow({
		'first_name': 'Alena',
		'last_name': 'Hulligan',
		'topic': 'PHP'
		})

