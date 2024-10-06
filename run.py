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

# Define the mapping of answers to scores.
answers_mapping = {
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


def display_main_menu():
    """
    Display the Main Menu with options.
    Call the get_user_choice function to check if input is valid.
    Move to the next action based on the user's choice.
    """
    print("=" * 50)
    print("              WELCOME TO MOODTRACKER")
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
            choice = int(
                input(f"\nPlease enter your selection (1-{len(options)}):\n")
                )
            if 1 <= choice <= len(options):
                return choice
            else:
                raise ValueError("Invalid selection.")

        except ValueError as e:
            print(f"{e}, please try again.")


def access_survey():
    """
    Display the survey.
    Call the get_user_choice function to check if input is valid.
    Store the responses in a dictionary.
    Display the responses.
    """
    print("-" * 50)
    print("          >>>>> YOUR VOICE MATTERS <<<<<")
    print("-" * 50)

    user_responses = {}

    # Iterate over each question in the survey
    for question, answers in question_options.items():
        print(f"\n {question}")

        # Display answers with index
        for index, answer in enumerate(answers, 1):
            print(f"{index} - {answer}")

        choice = get_user_choice(answers)
        user_responses[question] = answers[choice - 1]

    print("\nYour feedback, our improvement!\n")
    for question, selected_answer in user_responses.items():
        print(question)
        print(f"  --> {selected_answer.upper()}\n")

    update_worksheet(user_responses, survey)
    # next action? back to main menu, exit program....


def update_worksheet(user_responses, survey):
    """
    Convert the user's responses from a dictionary to a list format.
    Update the worksheet with the user's answers.
    """

    print("\nUpdating...")
    responses_list = list(user_responses.values())
    survey.append_row(responses_list)

    print("Thank you, your answers have been recorded!\n")


def analysis_program():
    print("=" * 50)
    print("           >>>>> ANALYSIS PROGRAM <<<<<")
    print("=" * 50)
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


def get_survey_data():
    """
    Retrieve survey data from survey_result worksheet.
    Return Headers and rows in separate variables.
    """
    data = survey.get_all_values()
    headers = data[0]
    rows = data[1:]
    total_answers = len(rows)
    return headers, rows, total_answers


def summary_statistic():
    """
    Display the Summary Statistic.
    Get the data from the survey_result worksheet.
    Generate for each question the number of answers received.
    """
    print("=" * 50)
    print("                SUMMARY STATISTIC")
    print("=" * 50)
    print()

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


def top_analysis():
    """
    Display the Top Satisfaction & Top Concerns.
    Get the data from the survey_result worksheet.
    Generate for each question a score based on the answers mapping sum.
    """
    print("=" * 50)
    print("          TOP SATISFACTION & TOP CONCERNS")
    print("=" * 50)
    print()

    headers, rows, total_answers = get_survey_data()
    survey_score = {}
    max_score = total_answers * 5

    for index, header in enumerate(headers):
        answers = [row[index] for row in rows]
        
        total_score = 0
        for answer in answers:
            score = answers_mapping.get(answer,0)
            total_score += score
        
        survey_score[header] = total_score
        sorted_score = sorted(survey_score.items(), key=lambda item: item[1], reverse = True)

    print("Survey results from highest to lowest score:\n")
    for question, score in sorted_score:
        print(f"- {question}: {score} / {max_score}")


display_main_menu()
