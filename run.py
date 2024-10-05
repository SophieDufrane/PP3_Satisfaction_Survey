# External libraries used for accessing Google Sheets
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

# Based on a code from Code Institute "Love Sandwiches" project
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("satisfaction-survey")
survey = SHEET.worksheet("survey_result")


class MenuOptions:
    """
    Display the Menu Options, with an index and description.
    """

    def __init__(self, index, option):
        self.index = index
        self.option = option

    def display_menu(self):
        return f"{self.index} - {self.option}"


main_menu_options = [
    MenuOptions(1, "Access to Survey"),
    MenuOptions(2, "Access to Analysis Program"),
    MenuOptions(3, "Exit Program"),
]

analysis_menu_options = [
    MenuOptions(1, "Summary Statistic"),
    MenuOptions(2, "Top Satisfaction & Top Concerns"),
    MenuOptions(3, "Back to Main Menu"),
]

# Dictionary with Question as key and list of answers as values
question_options = {
    "How satisfied are you with your current job role?": [
        "Very Satisfied",
        "Satisfied",
        "Neutral",
        "Dissatisfied",
        "Very Dissatisfied",
    ],
    "How would you rate the work environment at our company?": [
        "Excellent",
        "Good",
        "Average",
        "Poor",
        "Very Poor",
    ],
    "Do you feel you have opportunities for professional growth and "
    "development?": [
        "Strongly Agree",
        "Agree",
        "Neutral",
        "Disagree",
        "Strongly Disagree",
    ],
    "How would you rate your work-life balance?": [
        "Excellent",
        "Good",
        "Average",
        "Poor",
        "Very Poor",
    ],
    "How effective is communication within the company?": [
        "Very Effective",
        "Effective",
        "Neutral",
        "Ineffective",
        "Very Ineffective",
    ],
    "Overall, how satisfied are you with working at our company?": [
        "Very Satisfied",
        "Satisfied",
        "Neutral",
        "Dissatisfied",
        "Very Dissatisfied",
    ],
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
    print("\n")

    for option in main_menu_options:
        print(option.display_menu())

    choice = get_user_choice(main_menu_options)

    # Find a dynamic way to move to next action without hard coding
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
        user_responses[question] = answers[choice - 1]

    print("\nThank you for your time!")
    print("Here your answers: \n")
    for question, answers in user_responses.items():
        print(f"- {question}: {answers}")

    update_worksheet(user_responses, survey)
    # next action? back to main menu, exit program....


def update_worksheet(user_responses, survey):
    """
    Convert the user's responses from a dictionary to a list format.
    Update the worksheet with the user's answers.
    """

    print("\nUpdating worksheet...")
    responses_list = list(user_responses.values())
    survey.append_row(responses_list)

    print("Worksheet updated successfully.\n")


def analysis_program():
    print(">" * 50)
    print("           Welcome to Analysis Program.")
    print("<" * 50)
    print("\n")

    for option in analysis_menu_options:
        print(option.display_menu())

    choice = get_user_choice(analysis_menu_options)

    # Find a dynamic way to move to next action without hard coding
    if choice == 1:
        print("Accessing Summary Statistic...\n")
        summary_statistic()
    elif choice == 2:
        print("Accessing Top Satisfaction & Top Concerns...\n")
        top_analysis()
    elif choice == 3:
        print("Back to Main Menu...")
        display_main_menu()


def summary_statistic():
    """
    Display the Summary Statistic.
    Get the data from the survey_result worksheet.
    Generate for each question the number of answers received.
    """
    print("Summary Statistic:\n")

    data = survey.get_all_values()
    headers = data[0]
    rows = data[1:]
    survey_data = {}

    for index, header in enumerate(headers):
        answers = [row[index] for row in rows]

        answer_count = {}
        for answer in answers:
            if answer in answer_count:
                answer_count[answer] += 1
            else:
                answer_count[answer] = 1

        survey_data[header] = answer_count

    for question, answers in survey_data.items():
        print(f"\n{question}:")
        for answer, count in answers.items():
            response_label = "answer" if count == 1 else "answers"
            print(f"   ---> {answer}: {count} {response_label}")


def top_analysis():
    print("Top Satisfaction & Top Concerns:")


display_main_menu()
