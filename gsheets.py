import gspread, csv, argparse, time
from oauth2client.service_account import ServiceAccountCredentials

start = time.time()

# Process cmd line args
descStr = "Script for parsing finished datasets into a WatchStats workbook."
parser = argparse.ArgumentParser(description=descStr)
parser.add_argument("book_title", help='The exact title of the Google Sheets workbook. e.g. "Comparison: Most Popular Mobile OS"')
parser.add_argument("csv_file", help='Location of csv data file. e.g. "Most_Popular_Mobile_OS/formatted_data.csv"')

args = parser.parse_args()





# Setup API connection
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)



book = client.open(args.book_title)
sheet = book.worksheet("Researcher Book")


# Ensure element name headers are all empty.
cellRange = sheet.range("D7:BA7")
print("Cleaning element headers...")
for cell in cellRange:
    cell.value = ""
    sheet.update_cells(cellRange)
print("DONE")
rowData = []
with open(args.csv_file, "r") as f:

    # Read data out of csv
    reader = csv.reader(f)

    for line in reader:
        rowData.append(line)
    
    # Get csv file dimensions
    csvWidth = len(rowData[0])
    csvHeight = len(rowData)

    # Store csv data in cell range object
    cell_list = sheet.range(7,3, 7+csvHeight, 3+csvWidth)
    for cell in cell_list:
        try:
            cell.value = rowData[cell.row-7][cell.col-3]
        except IndexError:
            continue
    
    # Batch update cells
    print("Writing csv data to cells")
    sheet.update_cells(cell_list, value_input_option="USER_ENTERED")
print("DONE")
end = time.time()
print("Wrote", len(cell_list), "cells in", round((end-start),2),"seconds!")