import csv
examplefile = open('example.csv')
examplereader = csv.reader(examplefile)
exampledata = list(examplereader)
print (exampledata[0][0])