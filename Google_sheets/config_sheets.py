from google.oauth2 import service_account
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = "lesson-44-2.json"


creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets']
)

service = build('sheets', 'v4', credentials=creds)

google_sheet_id_users = '17TRyIQ1c7yvZsJRbQSaGwPnP6VyqwZgWXaotXKgWRB4'