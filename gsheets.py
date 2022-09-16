import gspread, csv
from oauth2client.service_account import ServiceAccountCredentials

# Setup API connection
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)


book = client.open("Copy of Comparison: Most Popular Mobile OS")
sheet = book.worksheet("Researcher Book")



# Ensure element name headers are all empty.
cellRange = sheet.range("D7:BA7")
for cell in cellRange:
    cell.value = ""
    sheet.update_cells(cellRange)

rowData = []
with open("Most_Popular_Mobile_OS/formatted_data.csv", "r") as f:

    # Read data out of csv
    reader = csv.reader(f)

    for line in reader:
        print(line)
        rowData.append(line)
    
    # Get csv file dimensions
    csvWidth = len(rowData[0])
    csvHeight = len(rowData)

    # Store csv data in cell range object
    cell_list = sheet.range(7,3, 7+csvHeight, 3+csvWidth)
    for cell in cell_list:
        print(cell.row-7)
        print(cell.col-3)
        try:
            cell.value = rowData[cell.row-7][cell.col-3]
        except IndexError:
            continue
    
    # Batch update cells
    sheet.update_cells(cell_list, value_input_option="USER_ENTERED")