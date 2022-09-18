import os, csv
import pandas as pd

files = []

for file in os.listdir("data"):
    if file.endswith(".csv"):
        files.append(file)
print(files)     
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

# Aggregate Windows version data
winFiles = os.listdir("data/Windows")
winFiles.sort()
winHeaders = ['Date']
# Get headers for output
for file in winFiles:
    with open("data/Windows/" + file, 'r') as currentFile:

        # Read CSV into object
        reader = csv.reader(currentFile)
        
        # Remove duplicates and append to header list
        for item in next(reader):
            if item not in winHeaders:
                winHeaders.append(item)


# Write headers to output file
with open("win_data.csv", 'w') as output:
    writer = csv.writer(output)
    writer.writerow(winHeaders)

# Read data and parse to output 
for file in winFiles:
    with open("data/Windows/" + file, 'r') as currentFile:
        dictReader = csv.DictReader(currentFile, delimiter=",")
        
        
        with open("win_data.csv", 'a') as output:
            writer = csv.DictWriter(output, fieldnames=winHeaders)

            writer.writerows(dictReader)

# Aggregate Mac version data
macFiles = os.listdir("data/Mac")
macFiles.sort()
macHeaders = ['Date']
# Get headers for output
for file in macFiles:
    with open("data/Mac/" + file, 'r') as currentFile:

        # Read CSV into object
        reader = csv.reader(currentFile)
        
        # Remove duplicates and append to header list
        for item in next(reader):
            if item not in macHeaders:
                macHeaders.append(item)


# Write headers to output file
with open("mac_data.csv", 'w') as output:
    writer = csv.writer(output)
    writer.writerow(macHeaders)

# Read data and parse to output 
for file in macFiles:
    with open("data/Mac/" + file, 'r') as currentFile:
        dictReader = csv.DictReader(currentFile, delimiter=",")
        
        
        with open("mac_data.csv", 'a') as output:
            writer = csv.DictWriter(output, fieldnames=macHeaders)

            writer.writerows(dictReader)

# Merge aggregated Windows version data into main output
data1 = pd.read_csv("win_data.csv")
data2 = pd.read_csv("formatted_data.csv")

output = pd.merge(data1,data2,on="Date",how="inner")

output.to_csv("formatted_data.csv")

# Merge aggregated Mac version data into main output
data1 = pd.read_csv("mac_data.csv")
data2 = pd.read_csv("formatted_data.csv")

output = pd.merge(data1,data2,on="Date",how="right")

output.to_csv("formatted_data.csv")


# Update Windows and Mac version share to be relative to whole market.
with open("formatted_data.csv", 'r') as file:
    dictReader = csv.DictReader(file, delimiter=",")
    with open("output_data.csv", 'w') as output:
        writer = csv.DictWriter(output, fieldnames=dictReader.fieldnames)
        writer.writeheader()
        for row in dictReader:
            print(row["Date"])
            for item in winHeaders:
                print(item)
                if item != "Date" and row[item] != "":
                    row[item] = str(float(row["Windows"]) * (float(row[item]) / 100))
                
            for item in macHeaders:
                if item != "Date" and row[item] != "":
                    row[item] = str(float(row["OS X"]) * (float(row[item]) / 100))
            
            writer.writerow(row)
        
        


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

fout.writelines(text)
fout.close()