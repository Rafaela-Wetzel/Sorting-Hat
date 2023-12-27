# Code Institute: Python Project by Rafaela Wetzel

The third milestone project is about creating a Python command-line application and showcasing the Python skills I have attained over the past 5 weeks at Code Institute. It is deployed on a Code Institute mock terminal on Heroku and the third out of five projects.  

# Sorting Hat

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

**You can see a deployed version of my app [here]()**

# How to Play  

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

The live project can be found here:

# Credits 

- House descriptions by [wizardingworld.com](https://www.wizardingworld.com/news/discover-your-hogwarts-house-on-wizarding-world)

- Quiz questions by [wizardmore.com](https://wizardmore.com/sorting-hat-x/) and [buzzfeed.com](https://www.buzzfeed.com/perpetua/lazy-harry-potter-hogwarts-sorting-hat-quiz)

- ASCII art by [emojicombos.com](https://emojicombos.com/harry-potter-ascii-art)

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

## Acknowledgements

- Help and feedback from my mentor Oluwafemi Medale