import csv
import pandas
field=['name','age','rollno']
sdict=[{'name':'akshay','age':20,'rollno':27},{'name':'aimen','age':21,'rollno':26}]
with open("dpt.csv",'w') as dfile:
	writer=csv.DictWriter(dfile ,fieldnames=field)
	writer.writeheader()
	writer.writerows(sdict)	
data=pandas.read_csv('dpt.csv')
print(data)
