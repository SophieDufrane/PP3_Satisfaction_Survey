# External libraries used for accessing Google Sheets.
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

# This code is based on the Code Institute "Love Sandwiches" project.
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("satisfaction-survey")
SURVEY = SHEET.worksheet("survey_result")


def display_title(title):
    """
    Displays menu title with decorative formatting.

    Args:
    title (str): The Menu title to be displayed.
    """
    print("=" * 50)
    print(title)
    print("=" * 50)


def display_options(menu_options):
    """
    Displays the list of menu options.

    Args:
    menu_options (list): A list of MenuOptions objects to be displayed.
    """
    for option in menu_options:
        print(option.display_menu_options())


def get_user_choice(options):
    """
    Gets and validates the user selection from the list of options.
    
    Args:
    options (list): The list of available Menu options.

    Returns:
    int: The validated user selection as an integer.
    """
    # Prompts user to select an option until valid input entered.
    while True:
        try:
            choice = int(input(f"\nPlease enter your selection (1-{len(options)}):\n"))
            if 1 <= choice <= len(options):
                return choice
            else:
                raise ValueError("Invalid selection. Please choose a number within the range.")

        except ValueError:
            print("Invalid selection, please try again.")


#def handle_choice(choice, choices):
    """
    Handles the user choice by displaying a message and executing the associated function.

    Args:
    choice (int): The user selected choice.
    choices (dict): Dictionary mapping the choice number to a tuple (description, function)
    """
    #if choice in choices:
        #print(choices[choice][0])
        #choices[choice][1]()


def display_main_menu():
    """
    Displays the main menu, handles user choice, and directs to next action.
    """
    # Add extra spaces to center the title.
    display_title("                    MAIN MENU")
    display_options(MAIN_MENU)
    choice = get_user_choice(MAIN_MENU)
    selected_option = MAIN_MENU[choice -1]
    selected_option.run_selected_option()


def access_survey():
    """
    Displays the survey questions, collects user responses, and updates the worksheet.
    """
    display_title("           >>>>> YOUR VOICE MATTERS <<<<<")
    user_responses = {}

    # Iterates over each question in the survey.
    for question, answers in QUESTION_OPTIONS.items():
        print(f"\n {question}")

        # Displays answers possible with their index.
        for index, answer in enumerate(answers, 1):
            print(f"{index} - {answer}")

        choice = get_user_choice(answers)
        user_responses[question] = answers[choice - 1]

    print("\nYour feedback, our improvement!\n")
    for question, selected_answer in user_responses.items():
        print(question)
        print(f"  --> {selected_answer.upper()}\n")

    update_worksheet(user_responses, SURVEY)
    next_action()


def update_worksheet(user_responses, SURVEY):
    """
    Updates the Google worksheet with user responses.

    Args:
    user_responses (dict): Dictionary of survey questions and user responses.
    SURVEY (gspread.Worksheet): Worksheet to append the responses to.
    """
    print("\nUpdating...")
    responses_list = list(user_responses.values())
    SURVEY.append_row(responses_list)

    print("Thank you, your answers have been recorded!\n")


def next_action():
    """
    Displays options for next action.
    """
    print()
    print("." * 50)
    print("What would you like to do next? Please select an option:")
    display_options(NEXT_ACTION_MENU)
    choice = get_user_choice(NEXT_ACTION_MENU)
    selected_option = NEXT_ACTION_MENU[choice -1]
    selected_option.run_selected_option()


def display_analysis_menu():
    """
    Displays the Analysis menu and handles user choice for analysis options.

    """
    display_title("             >>> ANALYSIS PROGRAM <<<")
    display_options(ANALYSIS_MENU)
    choice = get_user_choice(ANALYSIS_MENU)
    selected_option = ANALYSIS_MENU[choice -1]
    selected_option.run_selected_option()


def get_survey_data():
    """
    Retrieves survey data from worksheet.
    
    Returns:
    tuple: Tuple containing the headers, rows of data, and total count of answers.
    """
    data = SURVEY.get_all_values()
    headers = data[0]
    rows = data[1:]
    total_answers = len(rows)
    return headers, rows, total_answers


def summary_statistic():
    """
    Displays a summary of the survey statistic, showing percentage of each response for every question.
    """
    display_title("                 SUMMARY STATISTIC")

    headers, rows, total_answers = get_survey_data()
    survey_data = {}

    print(f"*** WE RECEIVED A TOTAL OF {total_answers} RESPONSES ***")

    for index, header in enumerate(headers):
        answers = [row[index] for row in rows]

        answer_count = {}
        for answer in answers:
            if answer in answer_count:
                answer_count[answer] += 1
            else:
                answer_count[answer] = 1

        survey_data[header] = {
            answer: round((count / total_answers) * 100, 1)
            for answer, count in answer_count.items()
        }

    for question, answers in survey_data.items():
        print()
        print("-" * 50)
        print(question.upper())
        print("-" * 50)
        for answer, percentage in answers.items():
            print(f"   --> {answer}: {percentage} %")

    next_action()


def top_analysis():
    """
    Displays the Top Satisfaction & Top Concerns based on survey scores.
    For each question, the function calculates a score based on the sum of mapped answers.
    """
    display_title("          TOP SATISFACTION & TOP CONCERNS")

    headers, rows, total_answers = get_survey_data()
    survey_score = {}
    max_score = total_answers * 5

    for index, header in enumerate(headers):
        answers = [row[index] for row in rows]

        total_score = 0
        for answer in answers:
            score = ANSWERS_MAPPING.get(answer, 0)
            total_score += score

        survey_score[header] = total_score
        sorted_score = sorted(
            survey_score.items(), key=lambda item: item[1], reverse=True
        )

    print("Survey results ranked from highest to lowest satisfaction score:\n")
    for question, score in sorted_score:
        percentage = round((score / max_score) * 100, 1)
        print(f"- {question.upper()}: {percentage}% satisfaction")

    next_action()

class MenuOptions:
    """
    Displays the Menus Options, with an index for each option.
    """

    def __init__(self, index, option, action_message, execute_action):
        """
        Initialises a MenuOptions instance with an index and option description.
        
        Args:
        index (int): The number representing the option.
        option (str): A string description of the option.
        action_message (str):
        execute_action ():
        """
        self.index = index
        self.option = option
        self.action_message = action_message
        self.execute_action = execute_action

    def display_menu_options(self):
        """
        Returns a formatted string for displaying menu options
        """
        return f"{self.index} - {self.option}"

    def run_selected_option(self):
        """
        Prints a message to acknowledge the user choice.
        Calls the function associated to action selected.
        """
        print(self.action_message)
        return self.execute_action()

MAIN_MENU = [
    MenuOptions(1, "Access to Survey", "Accessing Moodtracker Survey...\n", access_survey),
    MenuOptions(2, "Access to Analysis Program", "Accessing Analysis Program...\n", display_analysis_menu),
    MenuOptions(3, "Exit Program", "Exiting Program...", quit),
]

ANALYSIS_MENU = [
    MenuOptions(1, "Summary Statistic", "Accessing Summary Statistic...\n", summary_statistic),
    MenuOptions(2, "Top Satisfaction & Top Concerns", "Accessing Top Satisfaction & Top Concerns...\n", top_analysis),
    MenuOptions(3, "Back to Main Menu", "Back to Main Menu...\n", display_main_menu),
    MenuOptions(4, "Exit Program", "Exiting Program...", quit),
]

NEXT_ACTION_MENU = [
    MenuOptions(1, "Back to Main Menu", "Accessing to Main Menu...\n", display_main_menu),
    MenuOptions(2, "Back to Analysis Menu", "Accessing to Analysis Menu...\n", display_analysis_menu),
    MenuOptions(3, "Exit Program", "Exiting Program...", quit),
]

# Dictionary with Question as key and list of answers as values.
QUESTION_OPTIONS = {
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

# Maps answers to scores.
ANSWERS_MAPPING = {
    "Very Satisfied": 5,
    "Excellent": 5,
    "Strongly Agree": 5,
    "Very Effective": 5,
    "Satisfied": 4,
    "Good": 4,
    "Agree": 4,
    "Effective": 4,
    "Neutral": 3,
    "Average": 3,
    "Dissatisfied": 2,
    "Poor": 2,
    "Disagree": 2,
    "Ineffective": 2,
    "Very Dissatisfied": 1,
    "Very Poor": 1,
    "Stronly Disagree": 1,
    "Very Poor": 1,
    "Very Ineffective": 1,
}

if __name__ == "__main__":
    display_main_menu()
