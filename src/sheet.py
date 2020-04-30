import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Sheet:

    def __init__(self):
        self.scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name("C:\Projects\Python\cs-go-empire\creds.json", self.scope)
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open("API TEST").sheet1  # Open the spreadhseet

    def write(self, values):
        self.sheet.append_row(values) 

    def write_header(self):
        self.write(['----------------------NEW DATA START----------------------'])
