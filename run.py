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

class MainMenuOptions:
    def __init__ (self, index, option):
        self.index = index
        self.option = option
    
    def description(self):
        return f"{self.index} - {self.option}"

menu_options = [
    MainMenuOptions(1, "Access to Survey"),
    MainMenuOptions(2, "Access to Analysis Program"),
    MainMenuOptions(3, "Exit Program")
]

def display_main_menu():
    """
    Display the Main Menu and program options.
    Prompt the user to select an option.
    """
    print("=" * 50)
    print("               WELCOME TO MOODTRACKER")
    print("=" * 50)
    print("\nPlease select an option:\n")

    for option in menu_options:
        print(option.description())

    validate_user_choice()

def validate_user_choice():
    """
    Validate the input from user.
    Return to the user's input until data provided is valid
    """
    while True:
    
        try:
            choice = input("\nEnter your choice (1-3): ")
            if choice == "1":
                print("Accessing Moodtracker Survey...\n")
                access_survey()
                break
            elif choice == "2":
                print("Accessing Analysis Program...\n")
                analysis_program()
                break
            elif choice == "3":
                print("Exiting Program...")
                quit()
                break
            else:
                raise ValueError("Invalid selection.")
        
        except ValueError as e:
            print(f"{e}, please try again: ")

def access_survey():
    print("." * 50)
    print("     Welcome to Employees Satisfaction Survey")
    print("." * 50)

def analysis_program():
    print(">" * 50)
    print("           Welcome to Analysis Program.")
    print("<" * 50)

display_main_menu()