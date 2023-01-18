# WatchStats

Script for parsing a prepared csv dataset into a WatchStats workbook.


## Usage
### Setup
* Make sure that your credential file is in the same directory as the script and name it `creds.json`.
* Take your client email out of the credential file and share the workbook with that email.
### Example command
```python3 gsheets.py "Comparison: Most Popular Mobile OS" "Most_Popular_Mobile_OS/formatted_data.csv"```

```
usage: gsheets.py [-h] book_title csv_file

Script for parsing finished datasets into a WatchStats workbook.

positional arguments:
  book_title  The exact title of the Google Sheets workbook. e.g. "Comparison: Most Popular Mobile OS"
  csv_file    Location of csv data file. e.g. "Most_Popular_Mobile_OS/formatted_data.csv"

options:
  -h, --help  show this help message and exit
```
