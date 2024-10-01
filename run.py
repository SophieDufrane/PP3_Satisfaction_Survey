import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('satisfaction-survey')

survey = SHEET.worksheet('survey_result')
data = survey.get_all_values()

def display_main_menu():
    print("=" * 50)
    print("               WELCOME TO MOODTRACKER")
    print("=" * 50)
    print("\nPlease select an option:\n")
    print("1 - Access to Satisfaction Survey")
    print("2 - Access to Analysis Program")
    print("3 - Exit Program")

    choice = input("\nEnter your choice (1-3): ")
    return choice

display_main_menu()