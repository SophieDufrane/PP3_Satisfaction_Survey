# Moodtracker - The most modern Voice of the Employee tool on the market today.

The [Moodtracker](ADD LINK HERE) project was inspired by a tool already in use at *Workhuman* (my company), which is designed to gauge employee satisfaction and provide valuable insights through survey data analysis.

This Python project is a simplified version of the *Workhuman - Moodtracker*. It provides a command-line tool that serves two distinct purposes:
- To allow employees to easily participate in a satisfaction survey.
- To enable HR or management to analyze the survey data, generate key insights such as summary statistics and satisfaction levels, and identify areas for improvement.

**For Employees (Survey Respondents)**:
- As an employee, I want to easily access and complete the survey questions so that I can share my feedback on the company’s performance.

- As an employee, I want the survey process to be simple and straightforward so that I can complete it quickly without technical difficulties.

**For HR/Managers (Survey Analysts)**:
- As an HR manager, I want to collect and analyze employee responses from the survey so that I can identify satisfaction trends, review the overall sentiment of the employees and identify the areas of concern within the company.

- As a manager, I want to generate summary statistics and analyze top satisfaction/concern areas so that I can make data-driven decisions to improve employee satisfaction.

![Responsive Mockup](ADD PICTURE LINK HERE)

## Features:

To define the structure of the program, I started by working with a flowchart on [Lucid](https://lucid.app/lucidchart/6696772b-e3ff-4ca0-9902-c664edc9038e/edit?invitationId=inv_e35a23e0-a2a0-4a1a-8bd6-4be77803b441&page=0_0#). The flowchart helped me visualize the overall flow of the application, including how users interact with the main menu, survey questions, and analysis options. It outlines the logical steps from displaying the menu, collecting user input, and storing survey responses, to analyzing the data retrieved from Google Sheets.

By using a flowchart, I wanted to ensure a smooth, logical flow of data throughout.
![Flowchart](ADD PICTURE LINK HERE)

### Existing Features:

![MainMenu](ADD PICTURE LINK HERE)
- **Moodtracker Survey**
  - Goal: Collecting employees statisfaction level. Employees can feel heard....lalalalala
  - Feature: Access to question one by one, control that input is valid and prompt user to enter another value if not.....
  - flow and UX...lalalala

![Survey](ADD PICTURE LINK HERE)
- **Moodtracker Survey**
  - Goal: Collecting employees statisfaction level. Employees can feel heard....lalalalala
  - Feature: Access to question one by one, control that input is valid and prompt user to enter another value if not.....
  - flow and UX...lalalala

![Analysis](ADD PICTURE LINK HERE)
- **Analysis Program**  
  - Goal: Get insights from a large panel of employees....lalalala
  - Features: Access to a Menu with different options, control that user's choice is a valid input.....
  - flow and UX.....


### Features left to implement:

- **Credentials requirement to access to Analysis Program**
  As the program serves to main goals (Survey and results) we'll need to add a Credential requirement option to access the Analysis Program, as results should be confidentials....

- **Other Analysis Options**

## Manual Testing:

Along the development, I tested bloc of code using  [Python Tutor](https://pythontutor.com/visualize.html#mode=edit) blablabla

- **Wire API and Google sheet TEST**
  - Expected: when running the program it is expected to retrieve the data from the worksheet.
  - Testing: tested the program by running run.py in the terminal.
  - Result: the feature responded as expected and displayed the data from the worksheet survey_result

- **Validate user's selection in the main Menu**
  - Expected: program is expected to verify if the data provided is 1, 2 or 3. If so, the program will move to the section selected. If not it will display a ValueError message and will prompt the user to try again.
  - Testing: tested the program by running run.py in the terminal.
  - Result: the feature responded as expected, with the input 1, 2 or 3, the program informs that it is accessing to the option selected, then accesses the section selected. For any other data, an error message requests that the user tries again as data provided invalid.

- **Using class and dictionary to list the Main menu Options**
  - Expected: the command line is expected to display the options as: index (1, 2, 3) and name of the section.
  - Testing: tested the program by running run.py in the terminal.
  - Result: the feature did not responded as expected and displayed the index / sections from 3 to 1. 
  - Fix: To fix this and maintain the order of the options, I use a dictionary to preserve the order instead of a set.
  
- **Survey responses**
  - Expected: the command line is expected to get the user's responses and display a summary (to check if the data is correct).
  - Testing: tested the program by running run.py in the terminal.
  - Result: the feature did not responded as expected and displayed others answers (Satisfied instead of Very Satisfied for example). 
  - Fix: As the answers are stored in a list, the index start at zero and not 1. By substrating 1 form the choice, we'll get the correct answer.


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

The site was deployed to Heroku following the steps below:

1. Ensure that the `run.py` file is conform before deployment:
  - Add `\n` at the end of any inputs
2. In *Gitpod*, create a list of dependencies in `requirements.txt` file:
  - Run `pip3 freeze > requirements.txt` in the terminal


The live link can be found here: [Moodtracker](ADD LINK HERE)

### Content

- Inspiration: [Workhuman](https://www.workhuman.com/)


### Credits
- The integration with *Google Sheets* was implemented using code examples from the **Code Institute** [Love Sandwiches Project](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master/05-deployment/01-deployment-part-1)

### External Libraries
- `gspread`: Used to interact with *Google Sheets*. This library was essential for retrieving and storing survey responses in real-time, allowing the application to dynamically update and analyze survey data directly from the Google Sheets document.
- `google.oauth2`: Used for authenticating access to *Google Sheets* via service account credentials. This library was crucial for secure and authorized access to the Google Sheets API, ensuring that only authorized users can read or write data to the survey spreadsheet.