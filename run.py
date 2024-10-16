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

# Sets up a length for displaying titles.
MENU_WIDTH = 80


def format_title(title):
    """
    Formats the given title by centering it within the menu width.

    The function calculates the padding based on the title's length
    and the menu width, and adds spaces before the title to center it.

    Parameters:
    title (str): The title to be centered.

    Returns:
    str: The title string centered with spaces for defined menu width.
    """
    title_length = len(title)
    padding = (MENU_WIDTH - title_length) // 2
    return (" " * padding) + title


def display_title(title):
    """
    Displays menu title with decorative formatting.

    Parameters:
    title (str): The Menu title to be displayed.
    """
    print("=" * MENU_WIDTH)
    print(format_title(title))
    print("=" * MENU_WIDTH)


def display_options(menu_options):
    """
    Displays the list of menu options.

    Class:
    This function uses instances from MenuOptions class to display options.

    Parameters:
    menu_options (list of MenuOptions): A list of MenuOptions instances.
    """
    for option in menu_options:
        print(option.display_menu_options())


def get_user_choice(options):
    """
    Gets and validates the user selection from the list of options.

    Parameters:
    options (list): The list of available Menu options.

    Returns:
    int: The validated user selection as an integer.
    """
    # Prompts user to select an option until valid input entered.
    while True:
        try:
            choice = int(
                input(f"\nPlease enter your selection (1-{len(options)}):\n")
            )
            if 1 <= choice <= len(options):
                return choice
            else:
                raise ValueError(
                    "Invalid selection. Please choose a number"
                    "within the range."
                )

        except ValueError:
            print("Invalid selection, please try again.")


def display_main_menu():
    """
    Displays the main menu, handles user choice, and directs to next action.
    """
    display_title("MAIN MENU")
    display_options(MAIN_MENU)
    choice = get_user_choice(MAIN_MENU)
    # Converts user 1-based choice to the list's 0-based index.
    selected_option = MAIN_MENU[choice - 1]
    selected_option.run_selected_option()


def access_survey():
    """
    Displays the survey questions, collects user responses
    and updates the worksheet.
    """
    display_title(">>>>> YOUR VOICE MATTERS <<<<<")
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

    Parameters:
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
    print("." * MENU_WIDTH)
    print("What would you like to do next? Please select an option:")
    display_options(NEXT_ACTION_MENU)
    choice = get_user_choice(NEXT_ACTION_MENU)
    selected_option = NEXT_ACTION_MENU[choice - 1]
    selected_option.run_selected_option()


def display_analysis_menu():
    """
    Displays the Analysis menu and handles user choice for analysis options.

    """
    display_title(">>> ANALYSIS PROGRAM <<<")
    display_options(ANALYSIS_MENU)
    choice = get_user_choice(ANALYSIS_MENU)
    selected_option = ANALYSIS_MENU[choice - 1]
    selected_option.run_selected_option()


def get_survey_data():
    """
    Retrieves survey data from worksheet.

    Returns:
    tuple: Tuple containing the headers, rows of data, a count of responses.
    """
    data = SURVEY.get_all_values()
    headers = data[0]
    rows = data[1:]
    total_answers = len(rows)
    return headers, rows, total_answers


def summary_statistic():
    """
    Displays a summary of the survey statistic,
    showing percentage of each response for every question.
    """
    display_title("SUMMARY STATISTIC")

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
        print("-" * MENU_WIDTH)
        print(question.upper())
        print("-" * MENU_WIDTH)
        for answer, percentage in answers.items():
            print(f"   --> {answer}: {percentage} %")

    next_action()


def top_analysis():
    """
    Displays a ranking of responses for each area.
    For each question, calculates a score by mapping answers to a
    value and ranks the results accordingly.
    """
    display_title("TOP SATISFACTION & TOP CONCERNS")

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
    Displays a Menu Options, with an index and a description for each option.
    Executes the corresponding action when selected by the user.
    """

    def __init__(self, index, option, action_message, execute_action):
        """
        Initialises a MenuOptions.

        Parameters:
            index (int): The number representing the option.
            option (str): A string description of the option.
            action_message (str): A message to confirm user selection.
            execute_action (function): A function to be executed.
        """
        self.index = index
        self.option = option
        self.action_message = action_message
        self.execute_action = execute_action

    def display_menu_options(self):
        """
        Returns a formatted string for displaying menu options.

        Returns:
            str: Formatted option as 'index - option description'.
        """
        return f"{self.index} - {self.option}"

    def run_selected_option(self):
        """
        Prints a message to acknowledge the user choice.
        Calls the function associated to action selected.

        Returns:
            The associated function.
        """
        print(self.action_message)
        return self.execute_action()


# Constants for menu options used throughout the program.
MAIN_MENU = [
    MenuOptions(
        index=1,
        option="Access to Survey",
        action_message="Accessing Moodtracker Survey...\n",
        execute_action=access_survey,
    ),
    MenuOptions(
        index=2,
        option="Access to Analysis Program",
        action_message="Accessing Analysis Program...\n",
        execute_action=display_analysis_menu,
    ),
    MenuOptions(
        index=3,
        option="Exit Program",
        action_message="Exiting Program...",
        execute_action=quit,
    ),
]

ANALYSIS_MENU = [
    MenuOptions(
        index=1,
        option="Summary Statistic",
        action_message="Accessing Summary Statistic...\n",
        execute_action=summary_statistic,
    ),
    MenuOptions(
        index=2,
        option="Top Satisfaction & Top Concerns",
        action_message="Accessing Top Satisfaction & Top Concerns...\n",
        execute_action=top_analysis,
    ),
    MenuOptions(
        index=3,
        option="Back to Main Menu",
        action_message="Back to Main Menu...\n",
        execute_action=display_main_menu,
    ),
    MenuOptions(
        index=4,
        option="Exit Program",
        action_message="Exiting Program...",
        execute_action=quit,
    ),
]

NEXT_ACTION_MENU = [
    MenuOptions(
        index=1,
        option="Back to Main Menu",
        action_message="Accessing to Main Menu...\n",
        execute_action=display_main_menu,
    ),
    MenuOptions(
        index=2,
        option="Back to Analysis Menu",
        action_message="Accessing to Analysis Menu...\n",
        execute_action=display_analysis_menu,
    ),
    MenuOptions(
        index=3,
        option="Exit Program",
        action_message="Exiting Program...",
        execute_action=quit,
    ),
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
