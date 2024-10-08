# Moodtracker - The most modern Voice of the Employee tool on the market today.

The [Moodtracker](https://satisfaction-survey-sd-a479e4d4f1cf.herokuapp.com/) project was inspired by a tool already in use at *Workhuman*, the company I work for. This tool is designed to gauge employee satisfaction and provide valuable insights through survey data analysis.

This Python project is a simplified version of the *Workhuman - Moodtracker*. It provides a command-line program that serves two distinct purposes:
- To allow employees to easily participate in a satisfaction survey.
- To enable Human Ressources or management to analyze the survey data, generate key insights and identify areas for improvement.

**For Employees (Survey Respondents)**:
- As an employee, I want to easily access and complete the survey questions so that I can share my feedback on the company’s performance, culture and how I feel in my current role.

- As an employee, I want the survey process to be simple and straightforward so that I can complete it quickly without technical difficulties.

**For Human Ressources & Managers (Survey Analysis)**:
- As an HR manager, I want to collect and analyze employee responses from the survey so that I can identify satisfaction trends, review the overall sentiment and identify areas of concern within the company.

- As a manager, I want to generate summary statistics and analyze top satisfaction / concern so I can make data-driven decisions to improve employee satisfaction.

![Responsive Mockup](ADD PICTURE LINK HERE)

## Features:

To define the structure of the program, I started by working with a flowchart on [Lucid](https://lucid.app/lucidchart/6696772b-e3ff-4ca0-9902-c664edc9038e/edit?invitationId=inv_e35a23e0-a2a0-4a1a-8bd6-4be77803b441&page=0_0#). The flowchart helped me visualize the overall flow of the application, including how users interact with the main menu, survey questions, and analysis options. It helped defining the logical steps from displaying the menu, collecting user input, and storing survey responses, to analyzing the data retrieved from a Google Sheets.

By using a flowchart, I wanted to ensure a smooth, logical flow of data throughout.

![Flowchart](ADD PICTURE LINK HERE)

### Existing Features:

![MainMenu](ADD PICTURE LINK HERE)
**Main Menu**
- Overview: The Main Menu serves as a starting point for navigating between different sections of the program, allowing users to easily choose between starting the survey or accessing the analysis tools (for authorized personnel).
- Features:
  - Clear Option Presentation: The menu presents the available options in a simple, easy-to-read format, ensuring that users can make informed decisions.
  - Input Validation: User inputs are validated to ensure that the selected menu options are valid. If an incorrect option is entered, the program will prompt the user to try again.
  - User Flow: The flow from the main menu to other parts of the program is intuitive, providing a seamless experience.

![Survey](ADD PICTURE LINK HERE)
**Moodtracker Survey**
- Goal: To collect employee satisfaction levels, ensuring that employees feel heard and valued within the organization. This tool offers a simple and engaging way for employees to provide feedback regurlarly, on different aspects of their job and work environment.
- Features:
  - Question Display: Employees are presented with one question at a time, allowing them to focus and provide thoughtful responses.
  - Input Validation: The program ensures that all responses are valid by checking inputs. If an invalid input is detected, users are prompted to enter a correct value.
  - User Experience: The survey design is quite simple and user-friendly, guiding employees through the process seamlessly. Prompts and clear instructions make it easy for users to navigate and complete the survey.

![Analysis](ADD PICTURE LINK HERE)
**Analysis Program**
- Goal: To provide insightful data analysis from a large panel of employee responses, empowering HR and managers with actionable insights.
- Feature: 
  - Interactive Menu: The analysis section offers a clean, easy-to-navigate menu with multiple options, enabling users to explore survey results in detail.
  - Input Validation: Similar to the survey section, user choices are validated. If an invalid selection is made, the program prompts the user to choose a valid option, maintaining smooth navigation.
  - User Experience: This section has been designed to give HR professionals and managers quick access to meaningful statistics, making decision-making more informed and efficient.

### Features left to implement:

**Credentials requirement to access to Analysis Program**
- Since the analysis section contains confidential survey results, a credential check will be implemented to ensure only authorized personnel can access this data.

**Additional Analysis Options**
- The analysis program will be expanded to include more detailed metrics and deeper insights, providing a more comprehensive view of employee satisfaction and potential areas for improvement.

## Manual Testing:

Along the development, I tested bloc of code using  [Python Tutor](https://pythontutor.com/visualize.html#mode=edit) blablabla

- **Wire API and Google sheet TEST**
  - *Expected*: when running the program it is expected to retrieve the data from the worksheet.
  - *Testing*: tested the program by running run.py in the terminal.
  - *Result*: the feature responded as expected and displayed the data from the worksheet survey_result

- **Validate user's selection in the main Menu**
  - *Expected*: program is expected to verify if the data provided is 1, 2 or 3. If so, the program will move to the section selected. If not it will display a ValueError message and will prompt the user to try again.
  - *Testing*: tested the program by running run.py in the terminal.
  - *Result*: the feature responded as expected, with the input 1, 2 or 3, the program informs that it is accessing to the option selected, then accesses the section selected. For any other data, an error message requests that the user tries again as data provided invalid.

- **Using class and dictionary to list the Main menu Options**
  - *Expected*: the command line is expected to display the options as: index (1, 2, 3) and name of the section.
  - *Testing*: tested the program by running run.py in the terminal.
  - *Result*: the feature did not responded as expected and displayed the index / sections from 3 to 1. 
  - *Fix*: To fix this and maintain the order of the options, I use a dictionary to preserve the order instead of a set.
  
- **Survey responses**
  - *Expected*: the command line is expected to get the user's responses and display a summary (to check if the data is correct).
  - *Testing*: tested the program by running run.py in the terminal.
  - *Result*: the feature did not responded as expected and displayed others answers (Satisfied instead of Very Satisfied for example). 
  - *Fix*: As the answers are stored in a list, the index start at zero and not 1. By substrating 1 form the choice, we'll get the correct answer. Also in the second loop, I was re-using the variable name `answers` already used in the first loop, which confused the program. Re-naming the variable `selected_answer` inside the final print loop resolved clearly distinguishing the correct data to print.


## Refactoring Process: Improving Efficiency and Readability

- **Menu Handling Logic**
  - *Before Refactoring*: Initially, I had separate functions for handling different parts of the program (like the main menu and the analysis menu). Each had its own logic to display options and get user input, which was repetitive.

  - *After Refactoring*: I created a more generic MenuOptions class that could be reused for all menus. With this in place, I only need to define the options in one place and could reuse the same functions for handling the display across multiple menus, reducing duplication.

- **Avoiding repetitions**
  -  *Before Refactoring*: Despite the MenuOptions class, I noticed that I was still repeating similar blocks of code in multiple parts of the project to display Menu titles and options. For example, both the Main menu and Analysis menu had nearly identical code for introducing the section: ![BeforeRefactoring](ADD PICTURE LINK HERE)
  - *After Refactoring*: To reduce repetition, I refactored the code by creating 2 generic functions to handle the display of the title, and separatly the display of the options. These functions can be reused across different sections independently.

### PEP8 validation

I used *flake8* to test the conformity of the file `run.py` according to PEP8 standards. Below are the setps I followed:
- To install the linter in *Gitpod*, I ran the following command in the terminal:
  - `pip install flake8`
- To run the linter on run.py, I used:
  - `flake8 run.py`.

Here the list of main issues raised and fixed after running flake8:
  - E302: Expected 2 blank lines, found 1
  - W293: Blank line contains whitespace
  - E231: Missing whitespace around operator
  - E501: Line too long (### > 79 characters)


### Bugs, Fixes

- **Bug 1**: lalala...


### Deployment Steps

The site was deployed successfully to *Heroku* following the steps below:

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

### Content

- Inspiration: [Workhuman](https://www.workhuman.com/)


### Credits
- The integration with *Google Sheets* was implemented using code examples from the  [Love Sandwiches Project](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master/05-deployment/01-deployment-part-1) *Code Institute*


### External Libraries
- `gspread`: Used to interact with *Google Sheets*. This library was essential for retrieving and storing survey responses in real-time, allowing the application to dynamically update and analyze survey data directly from the Google Sheets document.
- `google.oauth2`: Used for authenticating access to *Google Sheets* via service account credentials. This library was crucial for secure and authorized access to the Google Sheets API, ensuring that only authorized users can read or write data to the survey spreadsheet.