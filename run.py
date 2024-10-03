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
    
    def display_menu(self):
        return f"{self.index} - {self.option}"

menu_options = [
    MainMenuOptions(1, "Access to Survey"),
    MainMenuOptions(2, "Access to Analysis Program"),
    MainMenuOptions(3, "Exit Program")
]

# Dictionary with Question as key and list of answers as values
question_options = {
    "How satisfied are you with your current job role?":[
        "Very Satisfied",
        "Satisfied",
        "Neutral",
        "Dissatisfied",
        "Very Dissatisfied"
    ],
    "How would you rate the work environment at our company?":[
        "Excellent",
        "Good",
        "Average",
        "Poor",
        "Very Poor",
    ]
}

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
        print(option.display_menu())

    choice = get_user_choice(menu_options)
    if choice == 1:
        print("Accessing Moodtracker Survey...\n")
        access_survey()
    elif choice == 2:
        print("Accessing Analysis Program...\n")
        analysis_program()
    elif choice == 3:
        print("Exiting Program...")
        quit()

def get_user_choice(options):
    # Prompt user for an options
    while True:
        try:
            choice = int(input(f"\nPlease enter your selection (1-{len(options)}): "))
            if 1 <= choice <= len(options):
                return choice
                break
            else:
                raise ValueError("Invalid selection.")
        
        except ValueError as e:
            print(f"{e}, please try again: ")    

def access_survey():
    """
    Display the survey and get the user's answers.
    Store the responses in a dictionary.
    """
    print("." * 50)
    print("     Welcome to Employees Satisfaction Survey")
    print("." * 50)

    user_responses = {}

    # Iterate over each question in the survey
    for question, answers in question_options.items():
        print(f"\n {question}")
        
        # Display answers with index
        for index, answer in enumerate(answers, 1):
            print(f"{index} - {answer}")

        choice = get_user_choice(answers)
        user_responses[question] = answers[choice -1]

    print("\nThank you for your time!")
    print("Here your answers: ")
    for question, answers in user_responses.items():
        print(f"- {question}: {answers}")
    
    return user_responses

def analysis_program():
    print(">" * 50)
    print("           Welcome to Analysis Program.")
    print("<" * 50)

display_main_menu()