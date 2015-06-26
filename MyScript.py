import sys
#
#Make SQL query from list of IDs
#

dataFile = open(sys.argv[1],'r')
outputFile = open('query.sql', 'w')
outputFile.write('SELECT * FROM table WHERE id IN (')
count = 0
for id in dataFile:
	count += 1
	if count%1000==0:
		output = '\'' + id.strip('\n') + '\')\nOR id IN(' 
	else: output = '\'' + id.strip('\n') + '\',\n'
	outputFile.write(output)
outputFile.write(')')
