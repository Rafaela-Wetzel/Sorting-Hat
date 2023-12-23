from random import shuffle

# Variables

# All questions and answers in pairs
question_one = "\n1. First placeholder question: \n"
answers_one = ["Gryffindor 1", "Slytherin 1", "Ravenclaw 1", "Hufflepuff 1"]

question_two = "\n2. Second placeholder question: \n"
answers_two = ["Gryffindor 2", "Slytherin 2", "Ravenclaw 2", "Hufflepuff 2"]

question_three = "\n3. Third placeholder question: \n"
answers_three = ["Gryffindor 3", "Slytherin 3", "Ravenclaw 3", "Hufflepuff 3"]

question_four = "\n4. Fourth placeholder question: \n"
answers_four = ["Gryffindor 4", "Slytherin 4", "Ravenclaw 4", "Hufflepuff 4"]

question_five = "\n5. Fifth placeholder question: \n" 
answers_five = ["Gryffindor 5", "Slytherin 5", "Ravenclaw 5", "Hufflepuff 5"]
# and so on...

# All answers sorted by houses
gryffindor_answers = ["Gryffindor 1", "Gryffindor 2", "Gryffindor 3", "Gryffindor 4"]
slytherin_answers = ["Slytherin 1", "Slytherin 2", "Slytherin 3", "Slytherin 4"]
ravenclaw_answers = ["Ravenclaw 1", "Ravenclaw 2", "Ravenclaw 3", "Ravenclaw 4"]
hufflepuff_answers = ["Hufflepuff 1", "Hufflepuff 2", "Hufflepuff 3", "Hufflepuff 4"]

def print_question_answers(question_x, answers_x):
    """
    Prints answers and questions
    """
    print(question_x)
    shuffle(answers_x)
    print(*answers_x, sep = '\n', end = '\n\n')  


def first_question():
    """
    Triggers first question and asks user for answer input
    """
    print_question_answers(question_one, answers_one) 
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
    print_question_answers(question_two, answers_two) 
    second_input = input()
    increase_score(second_input)
    
    if check_if_true(second_input) == True:
        third_question()
    else:
        second_question()


def third_question():
    """
    Triggers third question and asks user for answer input
    """
    print_question_answers(question_three, answers_three)
    third_input = input()
    increase_score(third_input)
    if check_if_true(third_input) == True:
        #fourth_question()
        print("\nCurrent scores:\n")
        print("Gryffindor: " + str(gryffindor))
        print("Slytherin: " + str(slytherin))
        print("Ravenclaw: " + str(ravenclaw))
        print("Hufflepuff: " + str(hufflepuff))
    else:
        third_question()