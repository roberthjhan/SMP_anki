from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

"""
modules
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
"""
API_KEY = "AIzaSyDbxsmCG4O5egNtvX57vs3avctmwzLPGAc"
key = API_KEY
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

SHEET_ID = "wXG90uXpzrtKjYEhAbXCtH7sMbrx582X8Z_gxwDrcYY"
SHEET_RANGE = "Approved!A:G"

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        print("no creds")
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
        for row in values:
            # Print columns A -> G, which correspond to indices 0 -> 6.
            print('%s, %s, %s, %s, %s, %s, %s' % (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

if __name__ == '__main__':
    main()



