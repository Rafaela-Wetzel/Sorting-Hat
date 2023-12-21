import os
from random import shuffle

answers_1 = ["Gryffindor 1", "Slytherin 1", "Ravenclaw 1", "Hufflepuff 1"]
answers_2 = ["Gryffindor 2", "Slytherin 2", "Ravenclaw 2", "Hufflepuff 2"]

global gryffindor
gryffindor = 0
global slytherin
slytherin = 0
global ravenclaw
ravenclaw = 0
global hufflepuff
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
    Prints welcome text and asks for user name input
    """
    print("\nWelcome to Hogwarts School of Witchcraft and Wizardry!\n\nNow that you have come here it is time for you\nto create your own history and leave behind a legacy in Hogwarts\nonce you have completed your magical studies.\nNow before you embark on your journey becoming a wizard*ess\nwe have to sort out an important detail:\nwhich house you will devote yourself to.\n\nThere is the house of Gryffindor known for its bravery and determination;\nalong with the house of Ravenclaw represented by its intelligence and wisdom;\nthe house of Slytherin characterized by its ambition and leadership\nand the house of Hufflepuff which brings forth hard-working, loyal and honest wizards.\n\nPlease, have a seat on this ceremony chair. The Sorting Hat will know where you belong...\n")

    your_name = input("\x1B[3mYoung wizard*ess, what is your name? \x1B[0m")
    print("\x1B[3m\nHello " + your_name + "!\n\nLet me see what house will bring forth the best in you...\n.\n..\n...\n")
    print("....Now, this is unexpected! The decision is more complex than I thought.\nI will need to get to know you better to find the right house for you...")
    need_more_information()

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


def second_question():
    """
    Same as above
    """
    question_2 = "\nSecond placeholder question: \n"
    print(question_2)
    answers_2_copy = list(answers_2)
    shuffle(answers_2_copy)
    print(*answers_2_copy, sep = '\n', end = '\n\n')  
    second_input = input()
    increase_score(second_input)
    '''
    If the increase_score function returns True (= if a house has gained one point) it will trigger the next question
    If the increase_score function returns False (= no house has gained any point / the user has entered invalid input) 
    it will trigger the same question again until the user has entered valid input
    '''
    if check_if_true(second_input) == True:
        #third_question()
        print("Score increased!")
    else:
        second_question()


def first_question():
    """
    Triggers first quiz question, input field and increase_score() function. Creates a copy of the answer list 
    and shuffles the copies. The original answer list is not touched so it is still possible to target the elements by index later on
    to increase the house scores. This would not be possible if the order of elements in the original list constantly changed.
    """
    question_1 = "\nFirst placeholder question: \n"
    print(question_1)
    answers_1_copy = list(answers_1)
    shuffle(answers_1_copy)
    print(*answers_1_copy, sep = '\n', end = '\n\n')  
    first_input = input()
    increase_score(first_input)
    '''
    If the increase_score function returns True (= if a house has gained one point) it will trigger the next question
    If the increase_score function returns False (= no house has gained any point / the user has entered invalid input) 
    it will trigger the same question again until the user has entered valid input
    '''
    if check_if_true(first_input) == True:
        second_question()
    else:
        first_question()


def increase_score(input):
    """
    Checks which answer the user chose and increases resp. house score by one
    """
    if input == answers_1[0] or input == answers_2[0]:
        global gryffindor
        gryffindor += 1
        print("Gryffindor: " + str(gryffindor))
    elif input == answers_1[1] or input == answers_2[1]:
        global slytherin
        slytherin += 1
        print("Slytherin: " + str(slytherin))
    elif input == answers_1[2] or input == answers_2[2]:
        global ravenclaw
        ravenclaw += 1
        print("Ravenclaw: " + str(ravenclaw))
    elif input == answers_1[3] or input == answers_2[3]:
        global hufflepuff
        hufflepuff += 1
        print("Hufflepuff: " + str(hufflepuff))
    else:
        print("\nPlease enter one of the given answers")


def check_if_true(input):
    if input == answers_1[0] or input == answers_2[0]:
        return True
    elif input == answers_1[1] or input == answers_2[1]:
        return True
    elif input == answers_1[2] or input == answers_2[2]:
        return True
    elif input == answers_1[3] or input == answers_2[3]:
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