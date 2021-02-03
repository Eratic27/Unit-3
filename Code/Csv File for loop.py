import csv
examplefile = open('example.csv')
examplereader = csv.reader(examplefile)
for row in examplereader:
    print ('Row #' + str(examplereader.line_num) + ' ' + str(row))