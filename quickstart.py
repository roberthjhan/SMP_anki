from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

"""
credit google sheets API quickstart document
modules
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
"""

# API_KEY = "AIzaSyB-vBUhBie0GlWVQvyvJAi69kYth6Duo-E"
key = open("key.txt", "r").read() # Read in API key from key.txt
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SHEET_ID = "1wXG90uXpzrtKjYEhAbXCtH7sMbrx582X8Z_gxwDrcYY"
SHEET_RANGE = "Approved!A:G"

def get_sheet():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.

    Calls the google sheets API to retrieve data from the SMP anki collab sheet
    https://docs.google.com/spreadsheets/d/1wXG90uXpzrtKjYEhAbXCtH7sMbrx582X8Z_gxwDrcYY/edit#gid=252059345

    Returns an array (list of lists) with 7 columns.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        print("CHECK CREDS")
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SHEET_ID,
                                range=SHEET_RANGE,
                                key=API_KEY).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        return values

if __name__ == '__main__':
    sheet = get_sheet()
    print(sheet)


