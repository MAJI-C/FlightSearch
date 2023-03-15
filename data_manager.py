from configure import configure
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

configure()

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")
#   The ID and range of a sample spreadsheet.
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
RANGE_NAME = "iata!A1:C"


class DataManager:
    def __init__(self):
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('sheets', 'v4', credentials=creds)
        self.sheet = service.spreadsheets()


    def call_spreadsheet_api(self):
        result = self.sheet.values().get(spreadsheetId=SPREADSHEET_ID,range=RANGE_NAME).execute()
        values = result.get('values', [])
        return values

    def get_cell_value(self, cell):
        result = self.sheet.values().get(spreadsheetId=SPREADSHEET_ID,range=cell).execute()
        values = result.get('values')
        return values
    
    def update_cells(self, upd_range, upd_values):
        request = self.sheet.values().update(spreadsheetId = SPREADSHEET_ID, range = upd_range, valueInputOption = "USER_ENTERED", body = {"values": upd_values}).execute()
        print(request)
    
    def get_column_values(self, range_names):
        result = self.sheet.values().batchGet(spreadsheetId = SPREADSHEET_ID, ranges = range_names).execute()
        ranges = result.get('valueRanges')[0].get('values')
        return ranges
    


