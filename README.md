# Moodtracker - The most modern Voice of the Employee tool on the market today.

The [Moodtracker](https://sophiedufrane.github.io/PP2_Rock_Paper_Scissors_Lizard_Spock_Game/) project was inspired by a tool already in use at *Workhuman* (my company), which is designed to gauge employee satisfaction and provide valuable insights through survey data analysis.

This Python project is a simplified version of the *Workhuman - Moodtracker*. It provides a command-line tool that serves two distinct purposes:
- To allow employees to easily participate in a satisfaction survey.
- To enable HR or management to analyze the survey data, generate key insights such as summary statistics and satisfaction levels, and identify areas for improvement.

**For Employees (Survey Respondents)**:
- As an employee, I want to easily access and complete the survey questions so that I can share my feedback on the company’s performance.

- As an employee, I want the survey process to be simple and straightforward so that I can complete it quickly without technical difficulties.

**For HR/Managers (Survey Analysts)**:
- As an HR manager, I want to collect and analyze employee responses from the survey so that I can identify satisfaction trends, review the overall sentiment of the employees and identify the areas of concern within the company.

- As a manager, I want to generate summary statistics and analyze top satisfaction/concern areas so that I can make data-driven decisions to improve employee satisfaction.

![Responsive Mockup](assets/media/rock_paper_scissors_mockup.png)

## Features:

Intro

Here the key features:

### Existing Features:

- **Feature 1**
  - lalalala.

  ![Feature1](assets/media/rock_paper_scissors_header.png)



### Features left to implement:

- **To be implemented**
  - lalala.


### Bugs, Fixes

- **Bug 1**: lalala.

- **Bug 2**: lalala.


## Testing:

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


### Feature Functionality Testing

- **Accessibility and Browser Compatibility**: 

- **Testing**: lalala.


### Validator Testing


### Deployment Steps

The site was deployed to Heroku following the steps below:

1. Step 1.
2. Step 2.


The live link can be found here: [Moodtracker](https://sophiedufrane.github.io/PP2_Rock_Paper_Scissors_Lizard_Spock_Game/)

### Content

- Inspiration: [Workhuman](https://www.workhuman.com/)
  
### Media