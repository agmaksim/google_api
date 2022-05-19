from pprint import pprint

import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'creds.json'
spreadsheet_id = '1el_Owh1GVfh2xbUrqdRrocUmvmHiH-BW82CTRHbqo_o'

credintials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
        ]
    )

httpAuth = credintials.authorize(httplib2.Http())
service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)

values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='A1:D51',
    majorDimension='ROWS'
).execute()
pprint(values)
exit()
