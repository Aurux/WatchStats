import os, csv

files = os.listdir("data")
files.sort()

headers = ['Date']

# Get headers for output
for file in files:
    with open("data/" + file, 'r') as currentFile:

        # Read CSV into object
        reader = csv.reader(currentFile)
        
        # Remove duplicates and append to header list
        for item in next(reader):
            if item not in headers:
                headers.append(item)


# Write headers to output file
with open("formatted_data.csv", 'w') as output:
    writer = csv.writer(output)
    writer.writerow(headers)

# Read data and parse to output 
for file in files:
    with open("data/" + file, 'r') as currentFile:
        dictReader = csv.DictReader(currentFile, delimiter=",")
        
        
        with open("formatted_data.csv", 'a') as output:
            writer = csv.DictWriter(output, fieldnames=headers)

            writer.writerows(dictReader)

# Format date column
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
dates = [] 
outputDates = []

# Find and map dates to alphanumeric
with open("formatted_data.csv", 'r') as file:
    dictReader = csv.DictReader(file)
    reader = csv.reader(file)
    writer = csv.writer(file)
    
     

    for col in dictReader:
        dates.append(col["Date"])
    
    for date in dates:
        year, month = date.split("-")
        outputDates.append(months[int(month)-1] + " " + str(year))


# Convert output to string
fin = open("formatted_data.csv", "r")
text = ''.join([i for i in fin])


# Replace dates in file string and rewrite file with new string
fout = open("formatted_data.csv", "w")
i = 0
for date in dates:
    text = text.replace(date, outputDates[i])
    i += 1
print(text)
fout.writelines(text)
fout.close()