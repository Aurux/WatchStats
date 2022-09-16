import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

# Setup API connection
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Copy of Comparison: Most Popular Mobile OS")
worksheet = sheet.worksheet("Researcher Book")