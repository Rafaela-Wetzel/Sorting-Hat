import os
import re 
from random import shuffle

question_1 = "\nFirst placeholder question: \n"
question_2 = "\nSecond placeholder question: \n"

answers_1 = ["Gryffindor 1", "Slytherin 1", "Ravenclaw 1", "Hufflepuff 1"]
answers_2 = ["Gryffindor 2", "Slytherin 2", "Ravenclaw 2", "Hufflepuff 2"]

gryffindor_answers = ["Gryffindor 1", "Gryffindor 2", "Gryffindor 3", "Gryffindor 4"]
slytherin_answers = ["Slytherin 1", "Slytherin 2", "Slytherin 3", "Slytherin 4"]
ravenclaw_answers = ["Ravenclaw 1", "Ravenclaw 2", "Ravenclaw 3", "Ravenclaw 4"]
hufflepuff_answers = ["Hufflepuff 1", "Hufflepuff 2", "Hufflepuff 3", "Hufflepuff 4"]

gryffindor = 0
slytherin = 0
ravenclaw = 0
hufflepuff = 0

def print_hogwarts_emblem():
    """
    Prints Hogwarts Coat of Arms
    """
    print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣶⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠿⠛⠉⠉⠉⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣿⠟⠁⠀⠀⠀⠀⠀⠈⠣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡿⠿⢿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣄⡀⠀⠀⠀⣠⣤⣤⣤⣤⣶⡿⠋⣀⣠⣤⣄⣀⠀⠀⠀⠀⠀⠈⠢⣄⣀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⣠⣶⣶⣾⣿⣿⣿⣿⣿⣿⠀⣶⣦⠙⣿⣿⣿⠿⠻⠿⣿⣿⣿⣿⣿⣦⣀⣼⡿⠿⠿⢛⣿⣵⣶⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⢀⣴⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀
    ⠀⠀⢰⣿⡿⠿⠿⢿⣿⣿⣿⣿⣿⣧⠙⢻⠀⣿⡿⠁⠀⠀⠀⢈⣿⣿⣿⣿⣿⣿⠋⠀⠀⣠⣾⠿⢻⣿⠿⠋⠁⠀⠈⣿⣿⣷⠀⣴⣿⣿⠟⠉⠉⠉⢿⣿⡀⠀⠀⠀
    ⠀⠀⢸⣿⡅⠀⠀⠀⠙⢿⣿⣿⣿⣿⣧⣾⢀⣿⡗⠀⠀⠀⠀⠀⢀⣈⣿⣿⣿⣿⠀⠀⠠⣿⣿⠿⠛⠁⠀⠀⠀⠀⣠⣿⣿⡟⣼⣿⡿⠁⠀⠀⠀⢀⣾⣿⠀⠀⠀⠀
    ⠀⠀⠘⢿⣷⣄⠀⠀⠀⠀⢻⣿⣿⣿⣿⡏⣼⣿⡆⠀⠀⠀⠀⢠⣤⣼⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿⣿⣿⠟⢰⣿⣿⠁⠀⠀⢀⣴⣿⡿⠁⠀⠀⠀⠀
    ⠀⠀⠀⠈⠻⢿⣷⣦⣀⠀⠀⣿⣿⣿⡿⢰⣿⣿⡟⠢⢀⠀⠀⠀⠀⠙⢿⣿⣿⣿⠀⠀⠀⠀⠀⣴⣾⣿⣿⣿⠿⠟⠋⠀⠀⢸⣿⡟⠀⢀⣴⡿⠟⠁⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠉⠛⠻⠇⠀⢸⣿⣿⠃⣾⣿⡟⠀⠀⠀⠀⠀⠀⣰⣶⣾⣿⣿⣿⠀⠀⠀⢠⣾⣿⣿⠟⠉⠀⠀⠀⠀⣀⡀⢸⣿⡇⠀⠘⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠻⠋⠀⠀⠀⢀⣶⣤⣀⡀⠉⠉⠻⣿⣿⠀⠀⠠⣿⣿⣿⣷⣶⡄⠀⣠⣶⣿⣿⣿⣾⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⡄⠀⠀⠀⠠⣿⣿⡿⡻⠿⠿⠿⠛⢿⣿⣶⠛⠻⠿⠟⠛⢿⣿⡿⣾⣿⠟⣛⣙⢿⣧⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⠿⠃⠀⢀⠄⠀⢸⣿⣿⣿⡄⠀⢠⣷⣾⣿⣿⣿⡆⠀⠀⣷⣼⣿⢻⣟⣵⣿⡿⠿⣷⣭⡜⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⣠⣴⣏⠀⢰⣿⣿⣿⣿⡇⠀⢸⣿⣿⠿⣿⣿⡇⠀⢸⡿⣿⡿⠾⢸⣿⣿⣤⣼⣿⣿⠛⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣷⠀⠉⢻⣿⣧⡈⠛⠻⣿⣿⡇⠀⠈⠉⠀⠀⠈⠛⠃⠀⠈⠟⣸⣧⣤⣤⣭⣟⣛⣛⣻⣧⣤⣼⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⡿⠿⠿⠿⣿⣿⣿⣿⣿⣶⣶⣿⣫⡄⠀⠀⣶⣶⣤⣤⣶⣦⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⠏⠀⠀⠀⣀⣤⠴⣦⡀⠀⠀⢸⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⣿⡟⠉⠁⠈⣯⠉⠛⠿⣿⣿⣿⣿⠀⠙⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣰⣿⣿⠋⠀⠀⢀⣼⣿⡇⣴⣀⣙⣦⡀⣸⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⡟⠀⠀⣿⣿⣿⣿⣿⣄⠀⠀⠀⢹⣿⣿⠋⠀⠀⠈⢿⣿⣄⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⣾⣿⣿⠃⠀⠀⢀⣾⣿⣿⣷⣬⡭⠿⠟⠁⣿⣿⣿⠏⠀⠀⠻⢿⣿⣿⡻⠃⠀⡀⠹⠟⣿⣿⣿⠏⠀⠀⠀⠘⠟⠁⠀⠀⠀⠀⠈⢿⣿⣷⣄⠀⠀⠀⠀
    ⠀⠀⠀⣴⣿⣿⠟⣿⣿⣶⣤⣿⣿⣿⣿⣿⣿⣶⣤⣀⠘⣿⣿⣷⣶⣶⠿⠟⠛⢻⣿⣿⣿⣿⡿⢶⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠘⣿⣿⣿⣷⣄⡀⠀
    ⠀⣠⣾⣿⠟⠁⠀⠈⠻⢿⠿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣦⣌⡙⠋⠁⠀⠀⠀⠀⢸⣿⣿⣿⣿⠁⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⢳⢀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣆
    ⢾⣿⣿⡋⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⢸⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡿⠋
    ⠀⠙⢿⣿⣦⣠⣄⠀⠀⣀⣼⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⢸⣿⣿⣿⣿⠀⠀⠀⠀⠰⡄⠀⠀⠀⠀⠀⢠⣿⣿⣞⡀⡀⡀⡄⢸⣿⣿⣿⠏⠀⠀
    ⠀⠀⠀⠉⠻⣿⣿⣿⠟⠛⠛⠉⠁⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⢸⣿⣿⣿⣿⡆⠀⠀⠀⠀⣷⠀⠀⠀⠀⢀⣾⣿⣿⣿⣷⣷⡇⢹⣸⣿⡟⠁⠀⠀⠀
    ⠀⠀⠀⠀⠀⠈⠻⣿⣄⠀⢀⣠⣄⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢸⣿⣿⣿⣿⣷⠀⠀⡀⣷⣿⣧⠀⣀⡀⢸⣿⠟⣿⣿⣿⣿⣿⣼⣿⠋⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠘⣿⣶⣿⣿⣿⣷⣄⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⢿⣿⣆⠀⢸⣿⣿⣿⣿⣿⡄⡄⣿⣿⣿⡟⢰⣿⡇⠈⣱⣷⣿⠿⢿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⠋⠀⠙⢿⣿⣧⡀⣠⣤⣤⣿⣿⡟⣿⣿⡀⢿⣿⡆⢸⣿⣿⣿⣿⣿⣇⣷⣿⣿⡟⢠⣿⡟⣠⣧⣿⡟⠁⠀⠀⠉⠛⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⠋⢉⣁⣿⣿⠷⠀⠉⠁⢸⣿⣿⣿⣿⣿⣿⣿⡿⠋⣠⣶⣬⣷⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⢿⣿⣿⣿⣅⡀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣱⣾⣿⣿⡿⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠿⣿⣷⣤⡀⢸⣿⣿⣿⣿⣿⡿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣼⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

""")


def enter_hogwarts():
    """
    Asks user if they want to start the game, and sends them back to start screen when 'no' or anything else than 'yes' or 'no' is entered 
    """
    enter = input("                       =======================\n                       ENTER HOGWARTS (yes/no)\n                       =======================\n")
    if enter == "yes":
        welcome_greeting()
    elif enter == "no":
        print("\nYou just missed your chance to become a great wizard*ess...\n")
        input("Press any key to take the Hogwarts Express back to London")
        os.system('clear')
        print_hogwarts_emblem()
        enter_hogwarts()
    else:
        print("\nOnly yes or no answers are valid\n")
        input("Press any key to return")
        os.system('clear')
        print_hogwarts_emblem()
        enter_hogwarts()


def welcome_greeting():
    """
    Prints welcome text
    """
    print("\nWelcome to Hogwarts School of Witchcraft and Wizardry!\n\nNow that you have come here it is time for you\nto create your own history and leave behind a legacy in Hogwarts\nonce you have completed your magical studies.\nNow before you embark on your journey becoming a wizard*ess\nwe have to sort out an important detail:\nwhich house you will devote yourself to.\n\nThere is the house of Gryffindor known for its bravery and determination;\nalong with the house of Ravenclaw represented by its intelligence and wisdom;\nthe house of Slytherin characterized by its ambition and leadership\nand the house of Hufflepuff which brings forth hard-working, loyal and honest wizards.\n\nPlease, have a seat on this ceremony chair. The Sorting Hat will know where you belong...\n")
    check_name()


def check_name():
    """
    Asks for user name input and checks if it is a valid string
    """
    your_name = input("\x1B[3mYoung wizard*ess, what is your name? \x1B[0m")
    if re.match(r"[a-zA-Z]", your_name):
        print("\x1B[3m\nHello " + your_name + "!\n\nLet me see what house will bring forth the best in you...\n.\n..\n...\n")
        print("....Now, this is unexpected! The decision is more complex than I thought.\nI will need to get to know you better to find the right house for you...")
        need_more_information()
    else:
        print("\nPlease enter a string that consists of letters a-z or A-Z\n")
        check_name()


def need_more_information():
    """
    Asks user if they are ready to start answering the Sorting Hats' questions and sends them back to start screen when 'no' or anything else than 'yes' or 'no' is entered 
    """
    confirm_start = input("\n\nAre you ready to dive deeper with me? (yes/no) ").lower()
    if confirm_start == "yes":
        first_question()
    elif confirm_start == "no": 
        print("\nMaybe this is not yet the right time for you to discover the world of wizardry.\nI might see you again in a couple of years...\n")
        input("Press any key to take the Hogwarts Express back to London ")
        os.system('clear')
        print_hogwarts_emblem()
        enter_hogwarts()       
    else:
        print("\nOnly yes or no answers are valid\n")
        need_more_information()


"""
def questions(question_x, answers_x_copy, answers_x, x_input, true_input, false_input):
    '''
    This was supposed to be a template for all quiz questions that takes parameters 
    but it does not work. Error message: line 142, in first_question
    questions(question_1, answers_1, first_input, second_question(), first_question())
                                     ^^^^^^^^^^^
    NameError: name 'first_input' is not defined
    '''
    print(question_x)
    answers_x_copy = list(answers_x)
    shuffle(answers_x_copy)
    print(*answers_x_copy, sep = '\n', end = '\n\n')  
    x_input = input()
    increase_score(x_input)

    if check_if_true(x_input) == True:
        true_input
    else:
        false_input

def first_question():
    questions(question_1, answers_1, first_input, second_question(), first_question())

def second_question():
    question(question_2, answers_2_copy, answers_2, second_input, print("Score increased!"), second_question())
"""


def first_question():
    """
    Triggers first question and asks user for answer input
    """
    print(question_1)
    answers_1_copy = list(answers_1)
    shuffle(answers_1_copy)
    print(*answers_1_copy, sep = '\n', end = '\n\n')  
    first_input = input()
    increase_score(first_input)

    if check_if_true(first_input) == True:
        second_question()
    else:
        first_question()

def second_question():
    """
    Triggers second question and asks user for answer input
    """
    print(question_2)
    answers_2_copy = list(answers_2)
    shuffle(answers_2_copy)
    print(*answers_2_copy, sep = '\n', end = '\n\n')  
    second_input = input()
    increase_score(second_input)
    if check_if_true(second_input) == True:
        #third_question()
        print("Score increased!")
    else:
        second_question()


def increase_score(input):
    """
    Checks which answer the user chose and increases resp. house score by one
    """
    #if input == answers_1[0] or input == answers_2[0]:
    if input in gryffindor_answers:
        global gryffindor
        gryffindor += 1
        print("Gryffindor: " + str(gryffindor))
    #elif input == answers_1[1] or input == answers_2[1]:
    elif input in slytherin_answers:
        global slytherin
        slytherin += 1
        print("Slytherin: " + str(slytherin))
    #elif input == answers_1[2] or input == answers_2[2]:
    elif input in ravenclaw_answers:
        global ravenclaw
        ravenclaw += 1
        print("Ravenclaw: " + str(ravenclaw))
    #elif input == answers_1[3] or input == answers_2[3]:
    elif input in hufflepuff_answers:
        global hufflepuff
        hufflepuff += 1
        print("Hufflepuff: " + str(hufflepuff))
    else:
        print("\nPlease enter one of the given answers")


def check_if_true(input):
    """
    If the check_if_true function returns True (= if a house has gained one point) it will trigger the next question
    If the check_if_true function returns False (= no house has gained any point / the user has entered invalid input) 
    it will trigger the same question again until the user has entered valid input
    """
    #if input == answers_1[0] or input == answers_2[0]:
    if input in gryffindor_answers or slytherin_answers or ravenclaw_answers or hufflepuff_answers:
        return True
    else:
        return False


def main():
    """
    Calls all functions
    """
    print_hogwarts_emblem()
    enter_hogwarts()

main()