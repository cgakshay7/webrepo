with open('file1.txt','r') as f, open('e_file.txt','w') as evenfile:
	for i, j in enumerate(f, 1):
		if i%2==0:
			evenfile.write(j)
