with open("stud.txt") as f:
	slist=f.readlines()
print(slist)
slist=[s.strip() for s in slist]
print("The contents of the file r: ")
print(slist)
