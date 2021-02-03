import csv
outputfile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputfile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham',])
outputWriter.writerow(['hello, World', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1,2,3.141592, 4])
outputfile.close()
print(outputfile)