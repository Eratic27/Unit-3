import csv, os

os.makedirs('headerRemoved', exist_ok=True)
# Loop through every file in the current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue #Skip non-csv files

    print ('Removing header from ' + csvFilename + '...')

# TODO: Read the csv file in (skipping first row)
csvRows = []
csvFileObj = open(csvFilename)
readerObj = csv.reader(csvFileObj)
for row in readerObj:
    if readerObj.line_num == 1:
        continue #Skip First Row
    csvRows.append(row)
csvFileObj.close()
        
# TODO: Write out the CSV file
csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
csvWriter = csv.writer(csvFileObj)
for row in csvRows:
    csvWriter.writerow(row)
csvFileObj.close()
