# Code Institute: Python Project by Rafaela Wetzel

The third milestone project is about creating a Python command-line application and showcasing the Python skills I have attained over the past 5 weeks at Code Institute. It is deployed on a Code Institute mock terminal on Heroku and the third out of five projects.  

# Sorting Hat

For my Sorting Hat project I am creating a quiz-like application that imitates the house sorting process in the story of Harry Potter. When he and his friends come to the wizarding school Hogwarts for the first time there is a welcome celebration in the Great Hall that involves a sorting ceremony. There are four houses in Hogwarts: Gryffindor, Slytherin, Ravenclaw and Hufflepuff. Depending on the students character and intentions they are being placed in one of the houses by a magical, speaking Sorting Hat. Every student is called onstage individually and puts the Sorting Hat onto their head. For some students the Sorting Hat shouts out the house to the crowd after just a moment; for others the Sorting Hat speaks to them so only the two of them can hear, and shares its thought process about the house placement. 

In my application the user is the student that is coming to Hogwarts for the first time. They are being welcomed to the school and approach the sorting process. The Sorting Hat then speaks to them and says that the decision is not easy and that it needs more information about them to be able to make a decision. The quiz then starts and asks 15-20 questions that evaluate the user and places them into one of the houses depending on their answers. The questions are not about asking for specific knowledge but are aimed at analyzing the users character, values and fictional decisions. 

I chose to create this application because the story of Harry Potter had been a big part of my childhood so this project can be seen as a hommage to these novels and the phase of life it is associated with. I also wanted to create a different project than the most common ideas suggested for Python beginners. 

# Table of Contents

- [Code Institute: Python Project by Rafaela Wetzel](#)
- [Sorting Hat](#sorting-hat)
- [Table of Contents](#table-of-contents)
- [Live Demo](#live-demo)
- [How to Play](#how-to-play)
- [Flowchart](#flowchart)
- [Technologies](#technologies)
- [Features](#features)
  - [First Section](#first-section)
  - [Second Section](#second-section)
  - [Features Left to Implement](#features-left-to-implement)
- [Testing](#testing)
  - [Testing App Functions](#testing-homepage-functions)
  - [Validator Testing](#validator-testing)
  - [Bugs & Problems](#bugs--problems)
  - [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Tutorials](#tutorials)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)

# Live Demo 

![A screenshot of the Sorting Hat app on different screen sizes]()

**You can see a deployed version of my app [here](https://magical-sorting-hat-d52437409b26.herokuapp.com/)**

# How to Play  

The user starts on the main page that shows the Hogwarts Coat of Arms and enters the school by typing 'yes'. There is a short introduction about the procedure and the characteristics of the four houses. The Sorting Hat is put on the users head to determine which house they should attend. It asks for their name and says that the decision is more difficult than expected; that it needs to get to know them better to be able to sort them into a house. The user then can enter 'yes' to start the display of questions. For each question there are 4 - 6 answers the user can choose from. They need to enter their chosen answer in the input field and are forewarded to the next question. After 15 questions the house scores are evaluated for the first time. If there is a clear winner (a house that has received the most answers) the user will be forwarded and shown the winning houses' Coat of Arms as well as a 'Welcome to the House'-text. If there is a tie between two or more houses after question 15 it continues to question 16, 17, ... and 20 at last. In the unlikely case that the user ends up with the 20th question and there is still a tie they can choose which house they would like to belong to.

# Flowchart

![image](assets/readme_assets/sorting-hat-flowchart.png)

# Technologies

- Python for creating the sorting hat quiz code
- Heroku for deployment in a mock terminal

# Features 

## First Section

## Second Section

## Features Left to Implement

### Accessibility

# Testing 

## Testing App Functions
    
## Validator Testing

- I confirm that no errors were returned when passing through the CI Python Linter [pep8ci](https://pep8ci.herokuapp.com/).

<br /><br />
![A screenshot of the CI Python Linter result]()  

## Bugs & Problems

- When a user input would be checked within the increase_score function the score for the respective house was supposed to increase by 1. When the scores for all houses were printed after this step to double check if everything works correctly it would show an increase by 2 instead of 1 for the respective house. It took me a while to figure out that this was due to the step that comes straight after this: running the increase_score function again to see if the user input was valid (point gained = True) or invalid (no point gained = False) by checking for the returned value that would trigger the next question (True) or repeat the current one (False). In the process of running the increase_function a second time, even if it was only to check for a True or False return value, the respective house score would be increased by 1 for the second time so that the outcome would be 2 points instead of 1. My solution was to separate the increase_score function from the valid/invalid input check by creating a second function check_if_true. The latter would then only have the purpose to return either a True or False value and not increase any score.    

- In the check if true function I first wrote: "if input in gryffindor_answers or slytherin_answers or ravenclaw_answers or hufflepuff_answers: return True" and was wondering why it did not work but skipped to the next question even if the answer was wrong. Later I realized that I would have to put "input in" before each of the houses, not only in the beginning.

## Unfixed Bugs

No unfixed bugs.

# Deployment

1. Add requirements for deployment in requirements.txt file
2. Log in to Heroku and create new app
3. Add Python and Nodejs Buildpacks
4. Go to deployment section and connect to GitHub account
5. Search for project repository and connect to Heroku
6. Deploy branch via manual deploy

The live project can be found here: https://magical-sorting-hat-d52437409b26.herokuapp.com/ 

# Credits 

- House descriptions by [wizardingworld.com](https://www.wizardingworld.com/news/discover-your-hogwarts-house-on-wizarding-world)

- Quiz questions by [wizardmore.com](https://wizardmore.com/sorting-hat-x/) and [buzzfeed.com](https://www.buzzfeed.com/perpetua/lazy-harry-potter-hogwarts-sorting-hat-quiz)

- House welcome texts taken from [harry-potter.fandom.com](https://harry-potter.fandom.com/de/wiki/Kategorie:Begriffskl%C3%A4rung?from=B)

## Tutorials 

[1] How to clear the console
https://www.youtube.com/watch?v=VAStmLsFQZ8

[2] How to add input validation
https://www.copahost.com/blog/input-python/#:~:text=Input%20validation%20using%20the%20module,print(%22Entry%20is%20valid!

[3] How to add Colorama
https://www.youtube.com/watch?v=u51Zjlnui4Y 

[4] How to block calls to print
https://stackoverflow.com/questions/8391411/how-to-block-calls-to-print

[5] 

## Media

- ASCII art by [emojicombos.com](https://emojicombos.com/harry-potter-ascii-art)

## Acknowledgements

- Help and feedback from my mentor Oluwafemi Medale