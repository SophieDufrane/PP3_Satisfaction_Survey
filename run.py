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

class MainMenuOptions:
    """
    Display the Main Menu Options, with an index and description.
    """
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
    Display the Main Menu with options.
    Call the get_user_choice function to check if input is valid.
    Move to the next action based on the user's choice.
    """
    print("=" * 50)
    print("               WELCOME TO MOODTRACKER")
    print("=" * 50)
    print("\nPlease select an option:\n")

    for option in menu_options:
        print(option.display_menu())

    choice = get_user_choice(menu_options)

    # Find a more dynamic way to use the dict and move to next action without hard coding
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
    """
    Get the user's choice.
    Verify if the input is valid.
    """
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
    Display the survey.
    Call the get_user_choice function to check if input is valid.
    Store the responses in a dictionary.
    Display the responses.
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
    print("Here your answers: \n")
    for question, answers in user_responses.items():
        print(f"- {question}: {answers}")
    
    update_worksheet(user_responses, survey)
    

def update_worksheet(user_responses, survey):
    """
    Convert the user's responses from a dictionary to a list format.
    Update the worksheet with the user's answers.
    """

    print("\nUpdating worksheet...")
    responses_list = list(user_responses.values()) # Get the values from dictionary and convert them into a list 
    survey.append_row(responses_list) # Add a new row in worksheet with values from the list

    print("Worksheet updated successfully.\n")

def analysis_program():
    print(">" * 50)
    print("           Welcome to Analysis Program.")
    print("<" * 50)

display_main_menu()
