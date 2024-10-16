# Moodtracker - Keep a continuous pulse on your people.

## Table of Contents

- [Introduction](#introduction)
- [User Story](#user-story)
- [Data Source](#data-source)
- [Features](#features)
  - [Existing Features](#existing-features)
    - [Main Menu](#main-menu)
    - [Moodtracker Survey](#moodtracker-survey)
    - [Analysis Program](#analysis-program)
  - [Features left to implement](#features-left-to-implement)
- [Manual Testing](#manual-testing)
- [Refactoring Process](#refactoring-process-improving-efficiency-and-readability)
- [PEP8 validation](#pep8-validation)
- [Deployment Steps](#deployment-steps)
- [Forking and Cloning the Project]()
- [External Libraries, Tools and Technology](#external-libraries-tools-and-technology)
- [Resources](#resources)

## Introduction

The [Moodtracker](https://satisfaction-survey-sd-a479e4d4f1cf.herokuapp.com/) project was inspired by a tool already in use at [Workhuman](https://www.workhuman.com/about-us/), a global software company that builds technology that enhances the employee experience and drives company cultures forward. *Moodtracker* is a survey tool designed to gauge employee satisfaction and provide valuable insights through survey data analysis.

## User Story

This Python project is a simplified version of the *Workhuman - Moodtracker*. It provides a command-line program that serves two distinct purposes:
- To allow employees to easily participate in a satisfaction survey.
- To enable Human Ressources or management to analyse the survey data, generate key insights and identify areas for improvement.

**For Employees (Survey Respondents)**:
- As an employee, I want to easily access and complete the survey questions so that I can share my feedback on the company’s performance, culture and how I feel in my current role.

- As an employee, I want the survey process to be simple and straightforward so that I can complete it quickly without technical difficulties.

**For Human Ressources & Managers (Survey Analysis)**:
- As an HR manager, I want to collect and analyse employee responses so that I can identify trends, review the overall sentiment and identify areas of concern within the company.

- As a manager, I want to generate summary statistics and analyse top satisfaction and top concerns so I can make data-driven decisions to improve employee satisfaction.

- Additionally, the storage of data in a Google worksheet makes it easier to generate reports and presentations, allowing both HR and managers to easily share insights with leadership team.

## Data Source:
This project uses and stores data in real-time in the following Google Sheet:
- [Google Sheet: Satisfaction Survey Data](https://docs.google.com/spreadsheets/d/1x5RsHwn2zUPl56D76aO-50ZlqlY9ddiT1pAFBvrcX14/edit?usp=sharing)

![Google Worksheet ScreenShot](media/google_worksheet.png)

## Features:

To define the structure of the program, I started by working with a flowchart on [Lucid](https://lucid.app/lucidchart/6696772b-e3ff-4ca0-9902-c664edc9038e/edit?invitationId=inv_e35a23e0-a2a0-4a1a-8bd6-4be77803b441&page=0_0#). The flowchart helped me visualise the overall flow of the application, including how users interact with the main menu, survey questions, and analysis options. It helped defining the logical steps from displaying the menu, collecting user input, and storing survey responses, to analysing the data retrieved from a Google Sheets.

By using a flowchart, I wanted to ensure a smooth, logical flow.

![Project Flowchart](media/flowcharts.png)

### Existing Features:

#### Main Menu

- *Overview*: The Main Menu serves as a starting point for navigating the program.

- *Features*:
  - **Clear Options Presentation**: The menu presents the available options in a simple, easy-to-read format.
    - Menu Handlin: The options are managed using a `MenuOptions` class. This allows for flexibility, as the same code is used for different menus. A `for` loop is used to iterate over the list of options and display them, making the code easier to maintain.
  - **Input Validation**: User inputs are validated to ensure that only valid options are accepted. If an invalid option is entered, the user is prompted to try again.
    - Validation Logic: Input validation is managed using a `while` loop and `try-except` block. The `try` block checks if the input is a valid integer within the expected range. If not, an exception is raised, and the user is prompted to enter a correct value.
  - **User Flow**: The program allows users to easily navigate between sections.

![Main Menu with options](media/main_menu.png)

#### Moodtracker Survey

- *Goal*: To collect employee satisfaction levels. This tool offers a simple and engaging way for employees to provide feedback regurlarly, on different aspects of the work environment.

- *Features*:
  - **Question Display**: The survey presents one question at a time, allowing employees to provide thoughtful responses.
    - Survey Logic: The survey uses dictionaries to store questions and possible answers. Each question is a 'key,' and the possible answers are the 'values.' This structure made it easy to add more questions later (which I did after working with a shorter sample to test the function).
  - **Input Validation**: The program ensures that all inputs are valid using the same function as for the Main Menu.
  - **Summary**: Displays user responses at the end of the survey, providing a clear overview of what will be recorded.
  - **Next Action**: After the survey, user has the option to move to another section or Exit the program.

- *User Experience*: The survey design is quite simple and user-friendly, guiding employees through the process seamlessly. Prompts and clear instructions make it easy for users to navigate and complete the survey.

![Survey displaying with sample of questions and answers](media/survey.png)

![User responses summary](media/survey_user_summary.png)

![Prompt to next action with options](media/next_action.png)

#### Analysis Program

- *Goal*: To provide insightful data analysis to Human Ressources and managers, from a large panel of employee responses.

- *Feature*: 
  - **Interactive Menu**: The analysis section offers a easy-to-navigate menu with multiple options to explore survey results in detail.
  - **Input Validation**: Similar to the Main Menu and Survey section, user inputs are validated.
  - **Summary Analysis**: Provides an overview of survey responses.
    - Responses are counted and stored in a dictionary. These counts are converted into percentages by dividing by the total number of responses, giving a clear picture of how employees feel.
  - **Top Satisfaction and Top Concerns**: Shows the most and least favorable areas.
    - Sorting Logic: The analysis program calculates satisfaction scores by assigning points to each answer (e.g., "Very Satisfied" = 5 points). Then it uses a lambda function to sort the survey questions based on their score.
    - Percentage Calculation: For each question, the score is divided by the maximum possible score and multiplied by 100 to give a percentage. This percentage represents the satisfaction level for each question.
  - **Next Action**: After analysis, user has the option to move to another section or Exit the program.

- *User Experience*: This section has been designed to give HR professionals and managers quick access to meaningful statistics, making decision-making more informed and efficient.

![Analysis Menu with options](media/analysis_menu.png)

![Summary Statistic with survey results](media/summary_statistic.png)

![Top Satisfaction and Top concerns with ranking](media/tops.png)

### Features left to implement:

**Credentials requirement to access to Analysis Program**
- Since the analysis section contains confidential survey results, a credential check will be implemented to ensure only authorised personnel can access this data.

**Additional Analysis Options**
- The analysis program will be expanded to include more detailed metrics and deeper insights, providing a comprehensive view of employee satisfaction and potential areas for improvement.

## Manual Testing:

During development, I used [Python Tutor](https://pythontutor.com/visualize.html#mode=edit) to break down and visualise small blocks of code. This tool allowed me to test the execution of functions independently, spoting issues and confirming when the logic worked as expected.

***Key Tests, Bugs and fixs:***

- **API and Google Sheets Integration**
  - *Expected*: The program retrieves data from the [Google Sheet: Satisfaction Survey Data](https://docs.google.com/spreadsheets/d/1x5RsHwn2zUPl56D76aO-50ZlqlY9ddiT1pAFBvrcX14/edit?usp=sharing).
  - *Testing*: Created a variable `data` to store the retrieved data and a `print()` statement to display the contents of `data` in the terminal after running `run.py`.
  - *Result*: The data was retrieved and displayed in the terminal without errors. The form was a list of lists: each inner list corresponded to a row in the worksheet, each row contained the responses to the question.

- **Main Menu Input Validation**
  - *Expected*: The program only accepts valid inputs (1, 2, or 3) and provide access to the choosen section. Invalid inputs trigger an error message prompting the user to try again.
  - *Testing*: Ran run.py in the terminal, testing valid and invalid inputs: numbers out of range, punctuation, alphabet letters, blank.
  - *Result*: The program correctly processed valid inputs, allowing access to the selected section. All type of invalid inputs displayed the error message.

- **Main Menu Display with Class and Dictionary**
  - *Expected*: The menu options display in correct order (1, 2, 3) along with their respective section names.
  - *Testing*: Added a print() statement to display the set used for storing menu options then ran run.py in the terminal.
  - *Result*: The options were displayed in reverse order (3 to 1).
  - *Fix*: To maintain the correct order, I replaced the set initially used for storing menu options with a dictionary, which preserves the insertion order.

- **Survey Display**
  - *Expected*: The program displays questions one at a time, allowing user to select their answers before moving to the next question.
  - *Testing*: Ran run.py in the terminal to simulate the survey.
  - *Result*: All questions were displayed simultaneously.
  - *Fix*: The input for user answers was placed outside the loop because of an incorrect idendation, causing all questions to appear at once. I moved the input inside the loop so the program waited for user input before moving to the next question.

- **Survey responses**
  - *Expected*: User responses to be collected and displayed in a summary.
  - *Testing*: Ran run.py and submitted answers to test the response collection.
  - *Result*: Incorrect responses were displayed (e.g., "Satisfied" instead of "Very Satisfied").
  - *Fix*: The issue came from the indexing in the list of answers (zero-based). By subtracting 1 from user choice, I ensured the correct answer was selected. Additionally, I noticed a variable name conflict in the final print loop (`answers` was reused), so I renamed it to `selected_answer` for more clarity.

- **Analysis Menu**
  - *Expected*: Displays analysis options in the correct order (1, 2, 3).
  - *Testing*: Ran run.py and checked the order of the menu display.
  - *Result*: The menu options were displayed in reverse (3 to 1).
  - *Fix*: Similar to the main menu, I switched to using a dictionary to preserve the correct order. I also corrected an issue by passing the correct variable `analysis_menu` to the `get_user_choice` function instead of `main_menu`.


## Refactoring Process: Improving Efficiency and Readability

- **Menu Handling Logic**
  - *Before Refactoring*: Initially, I had separate functions for handling different parts of the program. Each had its own logic to display options and get user input, which was repetitive.

  - *After Refactoring*: I created a more generic `MenuOptions` class that could be reused for all menus. With this in place, I only need to define the options and could reuse the same functions for handling the display across multiple menus, reducing duplication.

- **Avoiding repetitions**
  - *Before Refactoring*: Despite the `MenuOptions` class, I noticed that I was still repeating similar blocks of code to display Menu titles and options. For example, the Main menu and Analysis menu had nearly identical code for introducing the section.

![Example of a block of code before Refactoring](media/analysis_menu_before_refactoring.webp)

  - *After Refactoring*: I created two generic functions to separately handle the display of the title and the display of the options for each Menu. Next, I applied the same approach to how each function handled user input and called the next action. These functions are now reusable across different sections independently.

![Example of a block of code after Refactoring](media/analysis_menu_after_refactoring.webp)

- **Improved Usage of the MenuOptions Class**
  - *Before Refactoring*: The `MenuOptions` class was initially used only to display menu options with an index and a description. Each function with a menu had its own block of code to display the options and handle user choice.
  - *After Refactoring*: I moved the menu options directly into their respective dictionaries and added a new method to the MenuOptions class to display a message and execute the appropriate function. I tested the logic using [Python Tutor](https://pythontutor.com/visualize.html#mode=edit) to ensure everything worked as expected, and then applied the refactored logic to all menus across the program. With this in place, there was no longer a need to use the `handle_choice` function.

![Screenshot of Python Tutor with block of code tested](media/python_tutor.png)

- **Centered Title Formatting**
  - *Before Refactoring*: Titles had to be manually centered by typing spaces and counting them to ensure alignment, which was time-consuming and not precise enough.
  - *After Refactoring*: A `format_title` function was added to center the title within a fixed menu width of 80 characters. The function calculates the padding based on the title's length, ensuring alignment across menus.

### PEP8 validation

I used *flake8* to test the conformity of the file `run.py` according to PEP8 standards. Below are the steps I followed:
- To install the linter in *Gitpod*, I ran the following command in the terminal:
  - `pip install flake8`
- To run the linter on run.py, I used:
  - `flake8 run.py`.

Here the list of main issues raised and fixed after running flake8:
  - E302: Expected 2 blank lines, found 1
  - W293: Blank line contains whitespace
  - E231: Missing whitespace around operator
  - E501: Line too long (### > 79 characters)

Using flake8 first was beneficial because it allowed me to understand the specific formatting issues and learn the rules of PEP 8. After a few rounds of manual corrections, I found that switching to an automated tool like *Black* improved efficiency. Below are the steps I followed: 
- To install black for automatic code formatting:
  - `pip install black`
- To format the code using black on the specific file:
  - `black run.py`
- As I noticed that Black kept lines together up to 88 characters, I added a line-length configuration:
  - `black --line-length 79 run.py`

### Deployment Steps

The site was deployed successfully to [Heroku](https://www.heroku.com/github-students/signup) following the steps below:

1. Ensure that the `run.py` file is conform before deployment:
    - Add `\n` at the end of any inputs.
2. In *Gitpod*, create a list of dependencies in `requirements.txt` file:
    - Run `pip3 freeze > requirements.txt` in the terminal.
3. In *Heroku* account, create the new App:
    - Select `New` and `Create a new app`.
    - Name the App: `satisfaction-survey-sd` and choose a region: `Europe`Click `Create App`.
4. In the new App page, access to the `Settings` section.
5. Create a `Config Var` to access the credentials in `creds.json` file:
    - In the field `KEY` enter `CREDS`.
    - In the field `VALUE` paste the entire `creds.json` file content.
    - Click `Add`.
6. Add `Buildpacks` to install other dependancies:
    - Click `Add buildpack`.
    - Select `python` and add, then select `nodejs` and add.
7. Access to the `Deploy` section.
8. Select the deployment method:
    - Select `GitHub`
    - Search for the repository by taping the name in the search barre `PP3_Satisfaction_Survey`
    - Click on `Connect`
    - Select the option `Automatic deploys`
9. Once App deployed, the message *Your app was successfully deployed.*

The live link can be found here: [Moodtracker](https://satisfaction-survey-sd-a479e4d4f1cf.herokuapp.com/)

### Forking and Cloning the Project

Forking the repository creates a copy of this project, allowing modifications without affecting the original code. Once the repository is forked, it can be cloned to a local machine for development. Follow these steps to fork, clone, and work on the project:

- **Fork the repository**
  - Go to the repository you want to fork on [GitHub](https://github.com/).
  - In the top-right corner of the page, click `Fork`.
  - Name the new forked repository, then click `Create Fork`.
  - This creates a copy of the repository under your own GitHub account.

Once the repository is forked, we need to clone it to our local machine before working on it. This is done by following the steps below:

- **Clone the forked repository**
  - In the forked repository on GitHub, above the list of files, click `Code`.
  - Copy the URL for the repository (either HTTPS or SSH).
  - Open a terminal (or Git Bash).
  - Type `git clone`, then paste the copied URL.
  - Press `Enter`
  - Navigate to the newly cloned repository directory: `cd` and the repository name.

### External Libraries, Tools and Technology

- `gspread`: A Python library used to interact with *Google Sheets*. This library was essential for retrieving and storing survey responses in real-time, allowing the application to dynamically update and analyse survey data directly from the Google Sheets document.
- `google.oauth2`: Another librairy used for authenticating access to *Google Sheets* via service account credentials. This library was crucial for secure and authorised access to the Google Sheets API. Credentials were managed securely through the creds.json file. 
- `Google Sheets`: Used to store and manage survey responses.
- `Python`: The main programming language used for building the survey and analysis tool.
- `Google Cloud Console`: Used to generate credentials and API accesses for Google Sheets integration.
- `Gitpod`: A cloud-based IDE used for developing the project.

### Resources

- [Love Sandwiches Project](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master/05-deployment/01-deployment-part-1): 
  - This *Code Institute* project provided guidance on how to implement the integration with *Google Sheets*. Specifically, the setup for `gspread` and Credentials authentication was adapted from this project.
  - The code handling *Google Sheets* authentication and updating (in the `update_worksheet` and `get_survey_data` functions) was also based on this project but modified to suit the needs of the current project. These modifications included adjusting for different worksheet names and data formatting for survey responses. 
  - The validation logic using a `while True` loop with `try-except` for user input was also adapted and slightly modified to handle different menu options and return selections based on this project's requirements.
- [Python Tutor](https://pythontutor.com/visualize.html#mode=edit): 
  - This online tool was used to visualize and debug blocks of code, helping to ensure the logic was correct throughout development.
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/), [Flake8](https://flake8.pycqa.org/en/latest/) and [Black](https://pypi.org/project/black/): 
  - These resources were used for code formatting and validation according to Python standards. Flake8 was initially used for style error detection, while Black was employed for automated code formatting.
- [Functions vs Classes: When to Use Which and Why?](https://www.youtube.com/watch?v=txRTzljmV0Q):
  - This video helped me understand when to use functions and when to use classes, which made it easier to apply these concepts in my project.
- [List Comprehension](https://www.learndatasci.com/solutions/python-list-comprehension/):
  - This resource deepened my understanding of list comprehension and its usage for the project. Lists comprehension were used for example in the `summary_statistic` or `top_analysis` functions.
- [Lambda function](https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/):
  - This article showed me how to use lambda functions to sort lists of dictionaries, and was used for the display of the Top Satisfaction and Concerns.
- [Docstrings documentation](https://www.geeksforgeeks.org/python-docstrings/):
  - This article helped me write docstrings and understand how to format comments properly. I also improved the documentation by adding information about `Parameters` and `Returns`. 

