import csv
with open('data.csv','r') as efile:
	data= csv.reader(efile)
	for i in data:
		print(i)
