from random import shuffle
import os
import re 

import colorama
from colorama import Fore, Back, Style
colorama.init()

# Variables

# All questions and answers in pairs
question_one = "\n1. Which element resonates most with you? \n"
answers_one = ["fire", "water", "air", "earth"]

question_two = "\n2. Which of the following would you most hate people to call you? \n"
answers_two = ["cowardly", "ordinary", "ignorant", "selfish"]

question_three = "\n3. How would you like to be known to history? \n"
answers_three = ["the bold", "the great", "the wise", "the good"]

question_four = "\n4. After you have died, what would you most like people to do when they hear your name? \n"
answers_four = ["ask for more stories about your adventures", "i don't care what people think of me after i'm dead, it's what they think of me while I'm alive that counts", "think with admiration of your achievements", "miss you, but smile"]

question_five = "\n5. Given the choice, would you rather invent a potion that would guarantee you: \n" 
answers_five = ["glory", "power", "wisdom", "love"]

question_six = "\n6. Once every century, the Flutterby bush produces flowers that adapt their scent to attract the unwary. If it lured you, it would smell of: \n" 
answers_six = ["a crackling log fire", "the sea", "fresh parchment", "home"]

question_seven = "\n7. Four goblets are placed before you. Which would you choose to drink? \n" 
answers_seven = ["the golden liquid so bright that it hurts the eye, and which makes sunspots dance all around the room.", "The mysterious black liquid that gleams like ink, and gives off fumes that make you see strange visions.", "the foaming, frothing, silvery liquid that sparkles as though containing ground diamonds.", "the smooth, thick, richly purple drink that gives off a delicious smell of chocolate and plums."]

question_eight = "\n8. You enter an enchanted garden. What would you be most curious to examine first? \n" 
answers_eight = ["the statue of an old wizard with a strangely twinkling eye", "the bubbling pool, in the depths of which something luminous is swirling", "the silver leafed tree bearing golden apples", "the fat red toadstools that appear to be talking to each other"]

question_nine = "\n9. Four boxes are placed before you. Which would you try and open? \n" 
answers_nine = ["the small pewter box, unassuming and plain, with a scratched message upon it that reads ‘I open only for the worthy.'", "the gleaming jet black box with a silver lock and key, marked with a mysterious rune that you know to be the mark of Merlin.", "The ornate golden casket, standing on clawed feet, whose inscription warns that both secret knowledge and unbearable temptation lie within.", "the small tortoiseshell box, embellished with gold, inside which some small creature seems to be squeaking."]

question_ten = "\n10. You and two friends need to cross a bridge guarded by a river troll who insists on fighting one of you before he will let all of you pass. Do you: \n" 
answers_ten = ["volunteer to fight", "suggest that all three of you should fight (without telling the troll)?", "attempt to confuse the troll into letting all three of you pass without fighting?", "suggest drawing lots to decide which of you will fight?"]

question_eleven = "\n11. Which would you rather be: \n" 
answers_eleven = ["trusted", "praised", "envied", "feared", "imitated", "liked"]

question_twelve = "\n12. If you could have any power, which would you choose? \n" 
answers_twelve = ["the power of invisibility", "the power to read minds", "the power to change your appearance at will", "the power to change the past", "the power of superhuman strength", "the power to speak to animals"]

question_thirteen = "\n13. What are you most looking forward to learning at Hogwarts? \n" 
answers_thirteen = ["apparition and disapparition (being able to materialize and dematerialize at will)", "transfiguration (turning one object into another object)", "flying on a broomstick", "hexes and jinxes", "all about magical creatures, and how to befriend/care for them", "every area of magic I can"]

question_fourteen = "\n14. Which of the following would you most like to study? \n" 
answers_fourteen = ["centaurs", "ghosts", "werewolves", "goblins", "merpeople", "trolls"]

question_fifteen = "\n15. A Muggle confronts you and says that they are sure you are a witch or wizard. Do you: \n" 
answers_fifteen = ["ask what makes them think so?", "agree, and ask whether they'd like a free sample of a jinx?", "agree, and walk away, leaving them to wonder whether you are bluffing?", "tell them that you are worried about their mental health, and offer to call a doctor."]

question_sixteen = "\n16. Which road tempts you most? \n" 
answers_sixteen = ["the wide, sunny, grassy lane", "the narrow, dark, lantern-lit alley", "the twisting, leaf-strewn path through woods", "the cobbled street lined with ancient buildings"]

question_seventeen = "\n17. Late at night, walking alone down the street, you hear a peculiar cry that you believe to have a magical source. Do you: \n" 
answers_seventeen = ["proceed with caution, keeping one hand on your concealed wand and an eye out for any disturbance?", "draw your wand and try to discover the source of the noise?", "draw your wand and stand your ground?", "withdraw into the shadows to await developments, while mentally reviewing the most appropriate defensive and offensive spells, should trouble occur?"]

question_eighteen = "\n18. One of your house mates has cheated in a Hogwarts exam by using a Self-Spelling Quill. Now he has come top of the class in Charms, beating you into second place. Professor Flitwick is suspicious of what happened. He draws you to one side after his lesson and asks you whether or not your classmate used a forbidden quill. What do you do? \n" 
answers_eighteen = ["lie and say you don't know (but hope that somebody else tells professor flitwick the truth).", "tell professor flitwick that he ought to ask your classmate (and resolve to tell your classmate that if he doesn't tell the truth, you will).", "tell professor flitwick the truth. if your classmate is prepared to win by cheating, he deserves to be found out. also, as you are both in the same house, any points he loses will be regained by you, for coming first in his place.", "you would not wait to be asked to tell professor flitwick the truth. If you knew that somebody was using a forbidden quill, you would tell the teacher before the exam started."]

question_nineteen = "\n19. How would other people describe you? \n" 
answers_nineteen = ["honest, brave and adventurous", "deceitful, malevolent and sexy", "curious, analytical and witty", "friendly, happy and dorky"]

question_twenty = "\n20. Which house would you want to be in? \n" 
answers_twenty = ["gryffindor", "slytherin", "ravenclaw", "hufflepuff"]


# All answers sorted by houses
gryffindor_answers = ["fire", "cowardly", "the bold", "adventures", "glory", "log fire", "golden liquid", "statue", "plain box", "volunteer", "trusted", "praised", "invisibility", "change past", "change appearance", "apparition", "flying", "centaurs", "ghosts", "werewolves", "bluffing", "woods", "discover source", "ask classmate", "honest", "gryffindor"]
slytherin_answers = ["water", "ordinary", "the great", "don't care", "glory", "sea", "black liquid", "bubbling pool", "black box", "all three fight", "envied", "feared", "read minds", "superhuman strength", "change past", "apparition", "hexes", "goblins", "merpeople", "trolls", "jinx", "dark alley", "stand your ground", "not wait", "deceitful", "slytherin"]
ravenclaw_answers = ["air", "ignorant", "the wise", "achievements", "wisdom", "parchment", "silvery liquid", "silver tree", "golden casket", "confuse troll", "envied", "imitated", "read minds", "speak to animals", "change appearance",  "transfiguration", "every area", "centaurs", "goblins", "ghosts", "what makes them think so", "ancient buildings", "withdraw", "tell truth", "curious", "ravenclaw"]
hufflepuff_answers = ["earth", "selfish", "the good", "miss", "love", "home", "purple drink", "toadstools", "tortoiseshell box", "drawing lots", "trusted", "liked", "invisibility", "superhuman strength", "speak to animals", "flying", "magical creatures", "merpeople", "werewolves", "trolls", "mental health", "sunny lane", "proceed with caution", "lie", "friendly", "hufflepuff"]

# House score
gryffindor = 0
slytherin = 0
ravenclaw = 0
hufflepuff = 0

# Functions

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
    print('\nWelcome to' + Fore.MAGENTA + "\033[1m" + ' Hogwarts School of Witchcraft and Wizardry!' + "\033[22m" + Fore.RESET + '\n\nNow that you have come here it is time for you\nto create your own history and leave behind a legacy in Hogwarts\nonce you have completed your magical studies.\nNow before you embark on your journey becoming a wizard*ess\nwe have to sort out an important detail:\nwhich house you will devote yourself to.\n\nThere is the house of' + Fore.RED + "\033[1m" + ' Gryffindor ' + "\033[22m" + Fore.RESET + 'known for its bravery and determination;\nalong with the house of' + Fore.BLUE + "\033[1m" + " Ravenclaw " + "\033[22m" + Fore.RESET + 'represented by its intelligence and wisdom;\nthe house of' + Fore.GREEN + "\033[1m" + " Slytherin " + "\033[22m" + Fore.RESET + 'characterized by its ambition and leadership\nand the house of' + Fore.YELLOW + "\033[1m" + " Hufflepuff " + "\033[22m" + Fore.RESET + 'which brings forth hard-working, loyal and honest wizards.\n\nPlease, have a seat on this ceremony chair. The Sorting Hat will know where you belong...\n')
    check_name()

 
def check_name():
    """
    Asks for user name input and checks if it is a valid string
    """
    your_name = input("\x1B[3mYoung wizard*ess, " + Fore.CYAN + "what is your name? \x1B[0m" + Fore.RESET)
    if re.match(r"[a-zA-Z]", your_name):
        print("\x1B[3m\nHello " + Fore.CYAN + your_name + Fore.RESET + "!\n\nLet me see what house will bring forth the best in you...\n\n...\n...\n...\n")
        print("....Now, this is unexpected! The decision is more complex than I thought.\nI will need to get to know you better to find the right house for you.")
        need_more_information()
    else:
        print("\nPlease enter a string that consists of letters a-z or A-Z\n")
        check_name()


def need_more_information():
    """
    Asks user if they are ready to start answering the Sorting Hats' questions and sends them back to start screen when 'no' or anything else than 'yes' or 'no' is entered 
    """
    confirm_start = input(Fore.CYAN + "\n\nAre you ready to dive deeper with me? (yes/no) \n\n" + Fore.RESET).lower()
    if confirm_start == "yes":
        print(Fore.YELLOW + "\nINSTRUCTIONS: " + Fore.RESET + "Choose the answer for each question that describes your personality best. Please enter the identical answer in the input field. After the Sorting Hat has learned enough about you it will place you in the house you belong to...good luck!\n")
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


def increase_score(input):
    """
    Checks which answer the user chose and increases resp. house score by one
    """
    if input in gryffindor_answers:
        global gryffindor
        gryffindor += 1
    elif input in slytherin_answers:
        global slytherin
        slytherin += 1
    elif input in ravenclaw_answers:
        global ravenclaw
        ravenclaw += 1
    elif input in hufflepuff_answers:
        global hufflepuff
        hufflepuff += 1
    elif input == "leave":
        print("...")
    else:
        print("\nPlease enter one of the given answers")


def check_if_true(input):
    """
    If the check_if_true function returns True (= if a house has gained one point) it will trigger the next question
    If the check_if_true function returns False (= no house has gained any point / the user has entered invalid input) 
    it will trigger the same question again until the user has entered valid input
    """
    if input in gryffindor_answers or input in slytherin_answers or input in ravenclaw_answers or input in hufflepuff_answers:
        return True
    else:
        return False    


def exit():
    """
    Brings back user to quiz start page
    """
    print("While you are trying to sneak away from the Sorting Ceremony you are being discovered by a grim looking Hogwarts teacher. You can hear him quietly whisper\x1B[3m\033[1m Obliviate \033[0m\x1B[0mbefore your memories start to fade... you find yourself at platform 9¾ at King's Cross Station in London and scratch your head while looking at the platform number. But platform 9¾ does not exist... or does it?\n")
    input("Press any key to go home\n\n")
    os.system('clear')
    print_hogwarts_emblem()
    enter_hogwarts() 


def check_score():
    '''
    Checks final score. If one house has the most points this particular house function will be triggered
    If there is a tie, there will be more questions until one house has gained the majority of points
    '''
    if gryffindor > slytherin and gryffindor > hufflepuff and gryffindor > ravenclaw:
        enter_gryffindor()
        print("Gryffindor wins!")
    elif slytherin > gryffindor and slytherin > hufflepuff and slytherin > ravenclaw:
        enter_slytherin()
        print("Slytherin wins!")
    elif hufflepuff > gryffindor and hufflepuff > slytherin and hufflepuff > ravenclaw:
        enter_hufflepuff()
        print("Hufflepuff wins!")
    elif ravenclaw > hufflepuff and ravenclaw > gryffindor and ravenclaw > slytherin:
        enter_ravenclaw()
        print("Ravenclaw wins!")
    else:
        print("Nobody wins")


def enter_gryffindor():
    """
    Prints Gryffindor Coat of Arms and lets user know they have been placed in the Gryffindor house
    """
    print(Fore.RED + """
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣦⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⡟⠛⠋⠉⠉⣹⡍⠁⠀⠀⠀⢠⣿⡇⣶⣶⣶⣶⣾⣿⣿⣿⣭⣽⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣷⡄⠀⠀⢰⣿⣿⠄⠀⠤⣤⣭⣟⣡⣽⣻⣿⣿⣿⣿⡟⠈⣿⣿⣿⢹⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣄⢠⣿⢿⣋⣾⣿⣿⣿⣿⣿⣿⠛⠿⠊⠻⢿⣿⣿⣶⣿⣿⣿⣏⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⠃⠀⠵⣿⣿⣿⣿⣿⣿⠿⠓⠀⠀⠀⠤⣤⠄⠉⠛⢻⣿⣿⣿⣿⡜⣿⣿⣿⣿⣦⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣦⣤⣤⣴⣾⣿⣿⣿⣿⣿⣿⠃⠀⠀⣾⣿⣿⣿⣿⣿⠠⠶⠆⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⣜⢿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠈⠃⠀⠀⠼⣿⣿⣿⣿⣿⣿⣦⣄⣀⠀⠀⠀⠀⣴⣷⣶⣶⣴⣿⣿⣿⣿⣿⣿⠗⠀⠀⠈⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⡿⢿⡟⠋⠀⠀⠀⣴⡀⢀⠾⣻⣿⣿⣿⣿⣿⣿⣿⣷⡆⠀⠀⠀⠻⠿⠿⠿⣿⣏⠀⣹⣿⣿⠇⠀⠀⠀⢰⣶⡎⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⠀⣾⣿⣄⠀⠀⣼⣿⣿⢄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⣿⣿⣷⣿⣿⣿⡄⠀⠀⠀⣿⣿⡇⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⣾⣿⣿⣿⠆⠸⣿⣏⡵⠿⡻⣿⡿⣻⣿⣿⣿⣿⠋⢿⣿⣿⣷⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⣰⣿⣿⡇⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⣿⣿⣿⣿⡏⣿⣿⡏⠀⠀⠙⣿⡿⠃⠀⠘⢱⣿⣿⣿⣿⠃⠀⠀⠻⢿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⢠⣿⣿⣿⣿⡇⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⠟⠉⠈⠙⠢⣄⠀⠀⠈⠁⠀⠀⠀⠘⢸⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⢿⣿⡿⠃⠀⠀⠀⣸⣿⣿⢿⣿⡇⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀⢀⣤⠒⢄⠑⢄⣼⣦⠀⠀⠀⢠⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡇⠀⠀⠀⢀⣿⣿⡁⢈⣿⡇⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢹⣿⡄⠀⣾⢁⣾⣧⡀⠱⡀⠹⣿⣧⡀⢠⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠑⠤⢄⣀⣀⡀⢹⠀⠀⠀⣼⣿⣿⣷⣾⣿⢱⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣦⣽⣾⣿⣿⡗⠀⣷⠀⢹⡿⠁⠸⣿⣿⣿⣧⠀⠀⡠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠒⠚⠛⠛⠛⠻⠿⠿⢸⣿⣿⣿⣿⣤⣤⣄⠀⠀⠀
⠀⣰⣾⣿⣿⣿⣿⣿⣿⣿⡎⢿⣿⠁⠀⢸⠀⢸⠁⠀⠀⠹⣿⠋⠸⠀⠐⢋⠇⣠⠀⣀⡄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣿⣿⣿⣿⣿⣿⣷⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢀⣁⣀⣀⣼⠀⢸⣤⣤⣤⣤⣤⣤⣤⠀⠀⠸⠊⠘⠊⠈⠉⠉⠉⠁⠀⠀⠉⡝⢷⣶⣶⣶⡶⠂⣤⣀⠀⡀⢀⣿⣿⣿⣿⣿⣿⣿⠁⠀
⠀⠘⠿⢿⠿⢿⣿⣿⣿⣿⣷⢻⡿⠻⣿⣿⠀⢸⣿⣿⡟⢻⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠈⢻⣿⡿⠁⠀⠹⣿⣿⣿⣿⣿⣿⡏⠻⠿⠛⠁⠀⠀
⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⢸⣇⢠⣿⡿⠀⢸⣿⣿⣄⣠⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣎⠀⠀⠀⢠⣿⡇⠀⠀⢀⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡿⠞⠿⠟⠛⡇⠀⣾⣿⣿⣿⣿⡏⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣿⣿⣿⣄⣀⣰⣿⣿⣿⡄⢀⣾⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡖⠉⠉⠉⠉⢀⣀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⣀⡀⠀⠀
⠠⣴⣾⣿⣷⡀⠀⣠⡾⠻⣿⣷⣄⡀⠀⡏⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⢀⣤⢶⡦⢀⣴⠶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⡤⠀⠀⠈⠛⠉⠙⠿⠛⠿⢿⣿⣿⣿⠇
⠀⠈⢻⣿⡏⠀⣰⣿⠃⠀⠈⣿⠟⠁⢰⠃⠀⣀⢀⠀⠀⢀⠄⠀⢀⡀⢸⣿⣤⠀⣸⣿⠴⢛⣧⠀⠀⡀⠀⣀⠀⠀⠀⢈⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀
⠀⠀⢸⣿⡇⠀⣿⣿⠀⠀⠀⠀⠀⠀⢸⠀⢾⣿⠻⠗⠸⣿⣄⣼⠏⠐⢻⣿⠀⠐⣿⣿⠀⣿⡏⠀⣾⡟⢻⣿⠀⣾⡿⢻⣿⡇⣰⡶⢶⣄⢠⣶⣶⣶⡀⠀⣿⡟⠀⠀
⠀⠀⢸⣿⡇⠐⣿⡟⠀⠀⢀⣀⣀⡀⢸⠀⢸⣿⠀⠀⠀⢹⣿⠏⠀⠀⢸⣿⠀⠀⢻⣿⠀⣼⣿⠀⣿⡇⢸⣿⠀⣿⡇⢸⣿⡇⣿⡇⢸⣿⠀⣿⡇⠛⠁⠀⣿⡇⠀⠀
⠀⠀⢸⣿⡇⠀⣿⣧⠀⠈⢹⣿⣿⠁⠸⠀⠼⠿⠄⠀⣀⡼⠋⠀⢀⣀⣸⡿⠀⣀⣼⡏⠀⠛⠛⠠⠟⠓⠾⠿⠄⢿⡷⣾⣿⡇⢿⣇⣸⡿⢀⣿⡇⠀⠀⠀⣿⡇⠀⠀
⠀⠀⣸⣿⡇⠀⢿⣿⣇⠀⠀⣿⣿⡀⠀⠀⠀⠀⠙⠟⠋⠀⠀⠀⠀⠙⠛⠁⠀⠙⠛⠁⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠉⠉⠙⠂⠀⠸⣿⡇⠀⠀
⠀⠀⣿⣿⡇⠀⠈⣿⣿⣦⣀⣿⡿⠷⠀⣦⣤⣴⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣤⣤⣤⣤⣤⣄⠀⠀⠀⠀⠀⣿⡇⠀⠀
⠀⠀⣿⣿⡇⠀⠀⠘⠿⠛⠉⠀⠀⠀⠀⣿⣿⣿⣟⢿⠏⠉⠉⠉⢻⣿⣿⣁⣿⡏⠙⢤⡀⠀⠀⠀⠈⢫⡉⢉⣍⣉⣿⣿⣿⣿⡟⠿⠿⢿⣿⣿⣶⣶⣶⣤⣿⣇⠀⠀
⠀⠀⣿⠿⣇⣀⡀⠀⠀⠤⠔⠒⠒⠒⠺⣿⣿⣿⣿⣷⡄⠀⠀⠀⠈⠿⠿⠿⢿⡇⣠⣿⣿⣦⡀⠀⠀⠀⠈⠉⠻⣿⣿⣿⣿⠏⠀⠀⠀⠀⠉⠉⠙⠛⠛⠛⠿⠿⠀⠀
⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣦⣀⣀⠀⠀⠀⡄⣨⡇⠘⣿⣿⡿⢙⣦⣀⣀⣀⣢⣠⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣮⣙⠿⣿⡇⠀⠈⢟⣤⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠋⠙⢿⣿⣿⣿⣷⣮⣅⣠⣴⣿⣿⣿⣿⠟⠉⠀⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⠟⠁⠀⠀⠀⠀⠀
    """ + Fore.RESET)


def enter_slytherin():
    """
    Prints Slytherin Coat of Arms and lets user know they have been placed in the Slytherin house
    """
    print(Fore.GREEN + """
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣄⣶⣶⣶⣶⣾⣿⣿⣿⣶⣶⣶⣦⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⣦⣄⣀⠀⠀⠀⠀⣀⣀⡀⠀⢀⣀⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⡿⠿⣟⠻⠏⢩⢹⣿⣿⣿⣿⡿⠿⢿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣘⠻⠯⢑⣊⣉⣀⠀⠀⢸⡘⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⡆⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠙⠛⠛⠿⢿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡏⠀⣠⡾⠛⠻⣿⡿⠟⠃⠸⡇⢀⣴⣷⠀⠀⠀⠀⠀⠀⢀⣴⣧⡀⢹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢧⡀⠀⠀⠀⠀⠀
⠀⠀⡀⠄⠒⡇⠀⣿⣦⡀⠀⠉⠀⠀⠀⠀⡇⠀⣿⣿⠀⠀⣀⠀⠀⣀⢨⣿⡏⠀⢸⣿⣧⣴⣦⡀⠀⣴⣶⣶⣄⠀⣀⣴⣤⣤⡀⠀⣿⠇⠀⠀⠀⠀⠈⠧⠤⢄⡀⠀
⣠⠊⠀⠀⠀⠃⠀⠙⣿⣿⣶⣄⠀⠀⠀⠀⡇⠀⣿⣿⠘⣿⣿⠀⣿⡇⢸⣿⡇⠀⢸⣿⠃⢹⣿⡇⢸⣿⠁⣸⠿⠀⣿⣿⠛⠟⠁⣤⣴⡆⢀⣀⣠⡀⠀⠀⠀⠀⠉⡦
⠈⠢⣤⠀⠀⢸⠀⠀⠈⠻⣿⣿⣿⣦⡀⠀⠇⠀⣿⣿⠀⠸⣿⣦⣿⠁⠘⣿⣇⠄⣸⣿⡀⢸⣿⡇⢸⣿⡋⢀⡆⠀⣿⣿⠀⠀⢀⣿⡿⠀⢸⣿⡿⢻⣿⡆⠀⢀⠞⠁
⠀⠀⠀⠰⡀⣸⣤⣤⣤⣄⠈⠻⣿⣿⣧⠀⠀⠀⠾⠿⠂⠀⢹⡿⠃⠀⠈⠛⠁⠈⠉⠁⠀⠚⠛⠓⠈⠛⠷⠛⠁⠠⠿⠿⠄⠀⣼⣿⡇⠀⣸⣿⠁⢸⣿⠇⢠⠋⠀⠀
⠀⠀⠀⠀⣿⣿⠋⠁⠉⢿⣷⠀⠸⣿⣿⠀⢠⠀⠀⣴⣷⡾⠟⠁⣀⡤⠔⠒⠉⠉⠉⠉⠉⠓⠢⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠠⠿⠇⢀⣾⣿⠀⢳⠀⠀⠀
⠀⠀⠀⢸⣿⠁⠀⢦⣤⣾⡿⠀⢠⣿⣿⠂⢸⠀⣀⠠⣄⣒⢉⡿⠋⠀⠀⠀⢰⣄⣠⣀⣄⢀⠀⠀⠈⠣⣉⣲⢶⣤⣤⣀⣀⣀⠀⠀⠀⠀⠀⠀⠉⠙⠃⢀⡏⠀⠀⠀
⠀⠀⠀⢹⣿⣆⠀⠀⠀⠀⠀⢀⣾⣿⠟⠀⠸⠉⢰⣿⣿⢏⡞⠀⠀⠀⣠⣾⢟⣻⣯⣭⣟⡻⢿⣄⠀⠀⢶⣶⣍⠚⠋⠉⢽⢻⣷⣦⣄⡀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀
⠀⠀⠀⠀⠻⣿⣿⣶⣦⣴⡶⠟⠋⣁⣀⡤⠃⢀⣼⣿⡟⣼⡃⠀⠀⢰⡟⠀⠈⢻⡟⠁⠈⢻⣇⢿⡇⠀⣠⣤⠔⠒⠤⡂⢌⣿⣿⣿⣿⣿⣷⣦⣄⡀⠀⡜⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⠀⠀⣀⠤⣒⣭⡍⢰⣾⣿⣿⣿⣿⣿⡇⡟⡁⠀⠀⢸⡇⣄⠰⣿⣿⠆⣴⣿⣿⣮⡳⡀⠹⡇⠐⠢⡔⣿⣿⣿⣿⡿⢿⣿⣿⣿⡇⠉⠙⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠧⠒⠉⣶⣿⣿⣿⡇⠈⢿⣿⣿⣿⠿⢻⣇⢿⣷⠀⠀⠀⠙⢎⡳⣌⣡⣾⣿⣿⣿⣿⡇⠀⣥⣢⠅⣒⠛⣢⣽⡿⠋⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⣤⡙⣿⢱⢹⢸⣿⣌⢿⣷⣀⠀⠀⠀⠙⠢⢝⡻⢿⣿⣿⣿⣷⣠⣿⣿⣿⣶⣶⣿⣫⣶⣄⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⢸⣿⣿⡌⢸⠀⣞⢿⣿⣷⣝⠿⣷⣦⣄⣀⡀⠀⠉⠐⠨⢝⡻⢿⣿⣿⣿⣿⣿⠟⠹⣿⣿⣿⠆⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⢹⡟⡱⠟⣇⠘⢷⡒⢭⡻⣷⣮⣝⡻⣿⣿⣦⣀⠀⠀⠀⠉⠒⢭⡻⠿⢟⣅⠀⠀⣹⣿⡁⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⡇⢠⡿⡸⠁⢸⡾⢦⡀⠳⡀⠹⡽⣿⣿⣿⣷⠍⠻⢿⣿⣶⣤⣀⠀⠀⠈⢳⣝⢿⡆⢴⣿⣿⣷⡄⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠸⡇⡇⠀⢾⡀⣀⡷⠰⣧⠀⡇⣹⣿⣿⣿⣄⣠⣶⣭⡻⢿⣿⣷⠄⠀⠈⠻⢧⡀⠈⢻⡿⠋⠀⣼⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⢀⣷⢻⣄⠀⠉⠉⠀⢀⡿⢠⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣝⢿⣷⣄⠀⠀⠀⢻⣀⣾⣷⣄⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠘⣿⣷⢉⣓⠶⠾⣴⣾⠃⢸⠇⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠹⣿⣦⠀⠀⢈⣇⣿⣿⡿⠁⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡇⠀⢈⣴⣿⣿⣿⣿⢹⣿⠀⢿⢠⣾⣿⣿⣿⣿⡿⣿⣿⣿⣿⣷⣄⣤⢻⣿⠀⠀⠸⣿⣹⣯⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⢰⣿⣿⣿⣿⡿⠿⢸⣿⠀⢸⣼⣿⣿⣿⠿⣫⣾⣮⠻⣿⣿⣿⣿⡿⣼⣿⠀⢠⣀⡇⣿⣿⣷⡄⣿⣿⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⡅⢀⢸⣿⠀⠸⣷⡻⠟⠁⠀⠹⣿⠋⠀⠈⠻⣿⠟⣱⣿⠏⢀⣿⣿⠁⣿⣿⣿⡇⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⡜⣿⣧⡀⠉⢹⢤⡀⠀⣴⣿⣦⠀⠀⣀⣴⡾⠟⠀⢀⣾⣿⣇⣰⣿⣿⣿⡇⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣷⡘⠻⢿⣿⣿⣿⣿⣿⣼⣿⣿⣶⡀⠀⠉⠛⠒⠒⠶⠟⠛⠋⠉⢀⣠⣶⣿⣿⣿⣿⣿⡿⢟⣫⣵⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣷⣦⣈⠙⠻⠿⠟⣱⣦⣍⡻⢿⣿⣿⣿⣆⣠⣶⣦⣤⣴⡾⠿⠛⣋⡻⣿⠿⣋⣥⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠙⠻⠿⠛⢷⣶⣬⡭⣭⣭⣭⡭⣥⣴⣶⠊⠻⢟⣫⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠈⠻⡏⠀⢘⣿⣟⠀⠈⡿⣋⣤⣶⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⡚⠿⢟⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⡿⠟⠋⠁⠀⠀⠀
    """ + Fore.RESET) 


def enter_hufflepuff():
    """
    Prints Hufflepuff Coat of Arms and lets user know they have been placed in the Hufflepuff house
    """
    print(Fore.YELLOW + """
    ⠀⠀⠀⠀⠀⣀⣠⣤⣶⣾⣿⢿⣻⣿⢛⣿⡿⣿⢿⣧⣿⣿⣿⣷⡾⢿⣷⣂⣴⡿⣳⣾⣿⣿⣿⣷⡾⡿⣿⣻⣯⢨⣻⣿⣽⣯⣿⡿⣿⣶⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠰⣾⣿⣻⣯⣿⡭⣿⣿⢿⡿⣿⣿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣵⣯⣿⣽⡿⣿⠿⠿⢽⣷⣿⣿⣿⣿⣹⣽⣧⣾⣿⣼⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣾⡿⢿⣿⠿⣿⣯⠀⠀⠻⣾⣻⢽⣷⣄⠀⢹⠈⠁⠀⢤⠀⠉⠉⠀⠀⠀⠀⠈⠿⡏⠛⠻⢿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⢿⣿⢿⣿⣿⣧⡀⠀⠻⣿⣣⢟⣷⡀⠀⠘⢿⣷⢫⣟⣦⣸⠀⠀⢱⣿⡿⠀⠀⠀⣤⣿⣴⠀⠀⠀⢀⡖⠀⣿⣿⣿⣻⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⡾⣿⡿⣡⣿⢿⣿⣹⢷⣄⠀⠈⢿⣟⡾⣷⠶⡄⠀⠹⣿⡼⢯⣿⡀⠀⠀⠙⠃⠀⠀⠀⡷⡿⠃⠀⠀⠠⢿⣟⠧⣿⣷⣿⣇⣿⣿⣷⣄⣀⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠰⣶⣾⣿⣿⢟⣵⢿⣿⣿⠿⣾⢽⡻⣦⡀⠀⣻⡾⠿⠷⠾⢤⣀⠈⢿⣟⢾⡇⣤⠀⠀⠀⠀⣤⠀⠀⠀⠀⢀⡀⠀⠈⠋⠀⠘⣿⣯⣿⢷⣾⣿⣿⣿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠹⣿⡿⣿⣿⣿⣿⣿⡁⠀⢨⠟⠛⣉⣍⣻⣿⣴⣤⣄⣀⠀⠈⠓⢦⡹⣿⡟⣿⡛⠀⠀⢾⣿⠗⠀⠀⢠⣾⣷⠄⠀⢀⣴⣷⡈⠻⣿⣿⣿⣿⣻⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣿⣿⢳⣿⣿⣟⢿⣦⡹⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠙⢾⡇⠙⠀⠀⠀⠈⠿⠀⠀⠀⠈⠹⠇⠀⠀⠈⢹⡿⠀⢰⣿⣿⣿⢹⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣼⣿⣿⣿⢧⣿⣿⡟⢻⠿⠟⠛⠛⠻⠻⢿⣿⣿⣿⣿⣧⡀⠀⠛⠧⣄⡀⠀⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⣼⣿⣟⣿⣼⣿⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣿⣻⣿⢯⣿⣿⣗⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠿⣿⡆⠀⢰⣾⡿⠀⠀⠰⣿⣿⠇⠀⠀⠀⣴⣿⢶⠀⠀⠀⣿⣿⣞⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣷⡿⣿⣾⣻⣹⣿⡿⡇⠀⠀⢀⣤⣀⣀⣀⣀⠀⠀⠀⢀⣀⣻⣦⣀⣼⣿⣿⣤⡀⠀⠘⠃⠀⠀⢀⡀⢡⠿⠀⠀⠀⠘⣿⣷⣿⢂⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⢿⣿⣿⡟⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣽⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⣴⣾⣷⢄⣀⣤⡴⠿⠴⠿⠿⠿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣻⣿⣻⣿⡏⣄⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠴⠶⠛⢛⣛⡽⠯⠥⠔⠚⠒⢂⣠⣴⣤⡀⢠⣩⣝⠳⢤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣈⣿⣿⣷⣿⣿⣿⣿⣿⣿⡏⢃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⢋⣉⣥⠤⠖⠒⠀⠀⠀⠀⠀⠀⢀⡤⠶⣿⣿⠙⡋⢱⣿⡏⢻⡷⠀⡙⣦⡀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣯⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⠁⠁⣎⣿⣹⣟⣿⣿⡿⠟⡛⠉⢀⡴⠖⠚⠉⠀⠀⢀⣴⣴⣦⡀⣠⣴⡏⢶⣿⡇⣸⣿⣿⠛⠁⣸⣿⣷⢶⣷⡄⠙⣾⣿⠄
⠀⠀⠀⠀⠀⠀⢠⣾⣿⠿⣿⣿⣿⢿⣿⣿⣿⣷⣄⠀⣠⣾⠿⠛⣻⣉⣀⣴⡿⠟⣵⣿⠁⠀⠀⣀⡀⠰⣿⣿⠉⣿⣷⢸⣿⡇⢸⣿⡇⠸⣿⣿⠀⠀⢹⣿⡇⠀⢿⡇⠐⣾⡟⠀
⠀⠀⣴⣶⠶⠶⣿⣱⣯⣼⣯⠾⣧⠟⠉⢽⣿⡿⢟⣻⠉⠀⢀⣾⡟⠿⣹⣿⣧⠄⢹⣿⠀⣠⣿⢻⣿⡖⣿⣿⠀⣿⣿⢸⣿⣇⣸⣿⣧⠀⣿⣿⡀⠀⢸⣿⡇⠀⠈⠠⣼⣾⠁⠀
⠀⠀⢻⠆⠂⠀⢘⣡⡾⡋⢁⣠⣶⡏⡄⣺⣷⡺⠟⠃⠀⠀⣼⣿⣷⠾⣿⣿⡏⠀⢸⣿⠀⣿⣿⠼⠋⡀⣿⣿⠞⠟⠋⠈⠛⠉⠉⠉⠀⠀⣿⣿⠀⠀⢸⣿⡇⠀⠶⢜⣾⡟⠀⠀
⠀⠀⢺⡀⢶⣾⣿⣿⣿⠙⢻⣿⣿⡇⡇⢸⡷⠚⢁⢠⣴⡟⢿⣿⡏⠀⣻⣿⡇⠀⣸⣿⠀⣿⣿⢀⣾⡇⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠰⣾⡿⠟⠀⠈⠿⢟⢁⣀⡙⠳⣽⣇⠀⠀
⠀⠀⢸⡇⠘⣿⣿⣿⣸⠀⢸⣿⣿⡇⠇⢸⠐⣿⣿⠀⣿⡇⢸⣿⡇⠀⢸⣿⡇⠀⣼⡿⠆⠙⠻⠞⠋⠀⣿⣿⠶⢀⣀⣠⣴⣖⣾⣿⣷⠾⣶⣶⣶⣿⣾⣷⠶⢦⣍⡙⢮⣿⡀⠀
⠀⣠⣾⣷⢶⣿⣿⣿⣧⣤⣸⣿⣿⡇⠀⢸⡇⣹⣿⠀⣿⣧⣸⣿⡇⠀⣼⣿⡇⠈⠁⢀⣀⡤⠴⠒⣀⣴⣯⣴⣶⣾⣿⣿⣿⣿⣯⡟⣽⣦⣹⣿⡻⣿⣿⣹⡇⠈⣿⡝⢷⣿⡇⠀
⣼⣿⢉⣇⡔⣿⣿⣿⢻⠯⢽⣿⣿⣷⣤⢸⡆⢹⣿⠟⠻⠋⢸⣿⡇⢠⡿⠟⠠⠒⣋⣭⣥⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⣻⣿⣿⣿⣿⢻⣿⡇⠀⣿⡛⠘⣿⣧⠀
⠻⣿⣾⡿⠀⢿⣿⣿⣾⠀⠀⣿⣿⣇⡇⢸⣯⣬⡂⠄⠀⣰⣿⠋⣀⣠⣤⣶⠞⠋⠉⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣹⡟⣹⣿⣯⣿⣼⣿⣇⠸⣿⣴⣾⣿⡿⠀
⠀⠀⠹⡇⠀⣸⣿⣿⡇⠀⢰⣿⣿⣿⡡⢸⣿⣳⠠⢶⣚⣭⠶⠻⡿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠈⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣴⡡⣿⣷⣻⣿⡿⣿⠀⠙⠿⠿⠛⠁⠀
⠀⠀⠐⡇⠀⣿⣿⣿⢻⡄⢸⣿⠛⢫⣥⢸⣿⣶⠛⠋⠁⠀⠀⠈⠃⢻⣿⣿⣿⣿⣿⣦⡄⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⡇⠐⢩⠒⢻⣷⣿⡇⣽⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⡇⡼⡟⠙⠚⠉⠱⠋⠀⠉⠉⣀⣾⣏⠀⠀⠀⠀⡀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⠀⠀⢀⣹⣿⣿⣿⣿⣿⣿⣿⠇⠀⣠⠊⢹⣿⣻⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠘⠻⠷⠶⠶⣶⣶⣶⣶⣶⣿⣿⠉⣱⣿⣶⠀⢀⣾⡷⢖⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣶⣿⣭⣿⣿⣟⣾⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣾⡟⣿⢿⣿⡆⠀⢻⠃⠀⠀⠘⠟⠯⣏⣿⢻⡿⡿⠛⠉⠀⠀⣿⠈⢿⣗⡯⣿⣿⠟⣿⢟⣿⣿⣿⣿⠟⠛⢿⣧⢿⣿⣿⣿⠟⣽⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⢿⣿⣟⡿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠉⠈⠁⠉⠀⠀⠀⡀⠀⢻⡄⠀⠻⣿⣝⠿⣯⠈⠋⠻⣯⢯⢿⣦⡀⢀⣹⣿⣿⢯⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣻⣿⠿⣷⡿⣿⣷⣾⣧⣤⣀⠀⣠⣼⣷⡆⠀⢰⣾⣷⡆⢹⣿⣦⠀⠈⢿⡿⣹⢷⡀⢀⣹⣿⣾⣷⣿⣿⡿⣿⡟⣻⡿⣽⠟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣷⣽⣿⣽⡯⣿⡿⣿⣿⣿⣿⣾⣧⣥⣀⡈⠘⠇⠀⢸⣷⢾⣷⣀⣠⣿⣿⣿⣿⣿⡿⣟⡿⣿⡷⢿⣿⢿⣿⣿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢾⣧⣻⣿⣯⣽⣷⣷⡿⠻⣿⣞⡿⣻⣿⣷⣦⣄⣸⣻⣷⣿⣿⣿⣻⣽⣧⣿⣛⣉⣿⢿⣿⣷⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠓⠿⣾⣿⣿⣟⢿⣿⣟⣿⣿⣽⣿⣿⣿⣿⣏⣿⢋⣭⣿⣏⣿⣿⠿⢛⢛⠁⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """ + Fore.RESET)


def enter_ravenclaw():
    """
    Prints Ravenclaw Coat of Arms and lets user know they have been placed in the Ravenclaw house
    """
    print(Fore.BLUE + """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢲⣤⡀⠀⠀⢀⠀⠀⠀⠈⡇⣿⡄⠀⢰⡇⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣄⠀⢸⣷⡀⠀⠀⡇⣿⣷⠀⣾⢣⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⡄⠀⣿⣧⠀⣿⡇⣿⣿⣴⡏⣼⡿⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣄⣿⣿⢀⣿⠇⣿⣿⡟⢰⣿⣇⡜⣱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⡿⢰⣿⡿⢠⣿⣿⠟⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡿⠁⣾⣿⢁⣿⣿⢏⣼⣿⣟⣠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣶⣶⣤⣤⣤⣤⣤⣴⣶⣶⣶⣿⡇⣿⣿⣿⣿⡿⠁⣸⣿⡇⣾⡿⢁⣾⣿⣿⠟⡡⢠⣤⣤⣄⣀⣀⣠⣤⣤⣤⣶⣶⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢱⣿⣿⣿⡿⠁⢠⣿⣿⣧⠋⣠⣿⡿⢋⣵⠞⣡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⣼⣿⣿⣿⢡⣾⣿⣿⣿⣯⣼⠿⣫⣶⣿⣯⣤⣶⠀⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣤⣤⠤⠤⠤⢾⣿⣿⣿⣿⣿⠰⣶⡄⠰⢂⣤⡄⣿⣿⣿⡇⢸⣿⣿⣿⣿⢟⣥⣾⠿⢋⣥⣾⡿⠋⡘⣿⠀⠘⣣⡄⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⠉⠀⢀⣀⣤⣤⣤⣤⣀⠀⠈⠉⢻⡈⠃⣴⣿⣿⡇⢻⣿⣿⡇⠸⢹⣿⣿⣵⣿⠟⣡⣾⣿⣿⡿⢛⣿⠃⠛⣐⣚⣛⣃⣿⣿⠿⠿⠿⠤⠤⢄⣀⠀⠀⠀⠀
⠀⢀⣠⣿⣶⣿⣿⣿⡿⠋⠹⣿⣿⣷⡄⠀⢸⠛⠒⠒⠶⠶⠶⠾⠿⠿⠿⠀⠿⠿⠿⠟⠁⠾⠿⠿⠟⠉⠐⠛⠋⠉⡉⠉⠉⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠈⠹⣆⠀⠀
⢠⡿⢋⣿⡀⢸⣿⣿⡇⠀⠀⢹⣿⣿⣿⡄⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⢴⣿⣷⡀⠀⢠⡏⠀⠀
⣿⠀⣿⣿⣿⡎⣿⣿⣿⠀⠀⠀⣿⣿⣿⡇⣿⠀⠀⢀⡀⠀⠀⠀⠀⠀⡀⠀⠀⣀⡀⠀⠀⠀⢀⡀⠀⠀⣀⣀⠀⣿⡇⠀⣠⣤⣄⠀⢀⡀⠀⠀⢻⣿⡇⢀⣾⣅⠀⠀
⢻⣷⣤⣿⠟⠀⣿⣿⣿⠀⢀⣼⣿⣿⠏⠀⣿⠀⣾⠟⢻⣷⡄⣿⡇⠀⣿⢠⣾⠙⣿⡆⢺⡗⢻⣷⢠⣾⠉⠛⠁⣿⡇⠘⠏⠁⣿⣿⣿⡇⢰⡇⠀⣿⡇⣼⠁⠈⢳⡄
⠀⠈⠉⣿⠀⠀⢻⣿⣿⠙⢿⣿⣦⡀⠀⠀⣿⠀⣠⡤⢸⣿⡇⣿⡇⠀⣿⣿⣿⠋⠙⠁⢸⡇⠘⣿⢸⣿⠀⠀⠀⣿⡇⢠⣾⠃⣿⣿⣿⡇⢸⣿⢠⡿⢡⡇⠀⠀⢠⡟
⠀⠀⠀⣿⠀⠀⢸⣿⣿⠀⠀⣿⣿⣿⡄⠀⣿⠀⢿⣧⣸⣿⠇⢻⣧⡴⠋⠻⣿⠀⡶⠀⣸⡇⢀⣿⠘⠿⣄⠜⠀⣿⡇⠘⢿⡦⣿⠟⠛⠿⠋⠘⠛⠁⢸⠇⠀⢠⡟⠀
⠀⠀⠀⣿⠀⠀⢸⣿⣿⠀⠀⣿⣿⣿⣿⠀⣿⡄⠈⠉⠉⠁⠀⠀⠁⠀⠀⠀⠈⠉⠀⠀⠀⠀⠘⠁⠀⠀⣀⣀⣀⣀⣡⣤⣤⡤⣤⣤⣤⣤⣤⣤⣄⡀⢸⠀⠀⡟⠀⠀
⠀⠀⠀⢿⠀⠀⢸⣿⡏⠀⠐⠛⠛⠿⠿⠇⣿⣟⠓⠒⠶⠶⠦⠤⠤⠤⣤⡤⠶⠶⠖⠒⢒⣶⠟⠋⢹⣿⣿⣿⠿⡿⢯⣿⣾⣿⢸⣿⣿⣿⣿⡏⠀⠙⣿⠀⢸⠃⠀⠀
⠀⠀⠀⢸⣄⣀⣴⣿⣷⠶⣶⣶⣶⣤⣤⣤⣿⡏⡇⢸⣿⠀⣿⡇⢸⣇⣿⡇⠀⠀⣀⠀⢀⣤⡖⠀⣾⣿⣿⣿⣿⣭⣭⠽⣳⣿⢸⣿⣿⣿⣿⣷⣦⡤⠟⠀⢸⠀⠀⠀
⠀⠀⠀⠈⠉⠁⠀⣿⡏⠀⣿⣿⣿⣿⣿⡇⣶⣶⡇⠸⣛⣤⠭⠴⠶⠶⢾⡇⠀⢠⡿⠀⣾⣿⠗⠀⣿⣿⣿⣿⣿⣿⠗⣲⣼⣯⢸⣿⣿⣿⣿⣧⣤⡴⠚⠛⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⣿⣿⣿⣿⣿⡇⣿⡿⢣⣾⢡⣄⣠⣤⣶⣦⣄⠀⢀⣿⣇⣼⣿⣿⣷⣾⣿⣿⣿⣿⣿⠿⢛⣴⣿⣿⢸⣿⣿⣿⣿⡇⠈⣷⣶⠾⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⣿⣿⣿⣿⣿⡇⣿⢱⠟⠉⣩⣿⣿⣿⣿⣿⣿⡆⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢣⣿⣿⣿⡿⣼⣿⣿⣿⣿⡇⠀⣇⡎⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⠁⠀⢿⣿⣿⣿⣿⣇⢸⡸⣆⣴⢋⣭⣭⡝⢿⣿⣿⣷⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢫⣾⣿⣿⣿⡇⣿⣿⣿⣿⣿⡇⠀⠹⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⢸⣷⣮⣥⣾⡿⢋⡄⠀⣛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⢿⣧⡙⢿⣿⣿⢟⣥⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡘⣿⣿⠿⣋⠀⣿⡇⠀⣿⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣌⡛⠶⣌⡑⠿⢿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⡇⢛⡅⢸⣿⠀⣿⡇⢠⣿⡇⢸⡟⢿⡟⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢮⣝⡳⢦⣬⣙⡛⠻⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠸⡇⢸⣿⠀⣿⡇⢸⣿⡇⣸⢃⣾⠁⣼⣿⣿⣿⢫⡭⠛⠿⡿⣿⡮⣝⠺⣽⣳⢦⣭⣝⣛⠿⠶⠦⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣇⠁⢸⣿⠀⣛⡃⢸⠿⣡⣯⣾⡟⢠⣿⣿⣿⠟⠊⣴⡇⢸⣿⠈⣙⠺⣽⣷⣿⣟⡷⠭⡝⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣆⢸⡇⣿⡿⠛⠷⠾⢿⣿⡿⢣⣿⣿⠟⣵⣶⠀⣿⡇⢸⣿⡇⠋⣼⣷⣮⣥⣤⣤⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣆⠱⡜⠶⣠⠀⡠⠤⣀⠁⢸⣯⣃⠀⣿⣿⠀⣿⡇⢸⣿⢃⣾⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣷⡙⢿⣧⣭⣼⣿⡦⢱⣀⢏⣿⠀⣿⣿⠀⣿⡇⠘⣱⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣦⣙⠿⠟⣩⠀⣾⡆⢸⣿⠀⣿⣿⠀⠟⣡⣾⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣷⣤⡙⠀⣿⡇⢸⣿⠀⣿⠟⣠⣾⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣷⣦⣅⡘⢛⣠⣴⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⣿⡿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""" + Fore.RESET)


# All quiz questions

def print_question_answers(question_x, answers_x):
    """
    Template to print answers and questions
    """
    print("\nEnter 'leave' to exit the Great Hall\n")
    print(question_x)
    shuffle(answers_x)
    print(*answers_x, sep = '\n', end = '\n\n') 


def first_question():
    """
    Triggers first question and asks user for answer input.
    Same function description for all questions.
    """
    print_question_answers(question_one, answers_one) 
    first_input = input()
    increase_score(first_input)
    if first_input == "leave":
        exit()

    if check_if_true(first_input) == True:
        second_question()
    else:
        first_question()


def second_question():

    print_question_answers(question_two, answers_two) 
    second_input = input()
    increase_score(second_input)
    if second_input == "leave":
        exit()

    if check_if_true(second_input) == True:
        third_question()
    else:
        second_question()


def third_question():

    print_question_answers(question_three, answers_three)
    third_input = input()
    increase_score(third_input)
    if third_input == "leave":
        exit()

    if check_if_true(third_input) == True:
        fourth_question()
    else:
        third_question()


def fourth_question():
   
    print_question_answers(question_four, answers_four) 
    fourth_input = input()
    increase_score(fourth_input)
    if fourth_input == "leave":
        exit()

    if check_if_true(fourth_input) == True:
        fifth_question()
    else:
        fourth_question()


def fifth_question():

    print_question_answers(question_five, answers_five) 
    fifth_input = input()
    increase_score(fifth_input)
    if fifth_input == "leave":
        exit()

    if check_if_true(fifth_input) == True:
        sixth_question()
    else:
        fifth_question()


def sixth_question():

    print_question_answers(question_six, answers_six) 
    sixth_input = input()
    increase_score(sixth_input)
    if sixth_input == "leave":
        exit()

    if check_if_true(sixth_input) == True:
        seventh_question()
    else:
        sixth_question()


def seventh_question():

    print_question_answers(question_seven, answers_seven) 
    seventh_input = input()
    increase_score(seventh_input)
    if seventh_input == "leave":
        exit()

    if check_if_true(seventh_input) == True:
        eighth_question()
    else:
        seventh_question()


def eighth_question():

    print_question_answers(question_eight, answers_eight) 
    eighth_input = input()
    increase_score(eighth_input)
    if eighth_input == "leave":
        exit()

    if check_if_true(eighth_input) == True:
        ninth_question()
    else:
        eighth_question()


def ninth_question():

    print_question_answers(question_nine, answers_nine) 
    ninth_input = input()
    increase_score(ninth_input)
    if ninth_input == "leave":
        exit()

    if check_if_true(ninth_input) == True:
        tenth_question()
    else:
        ninth_question()


def tenth_question():

    print_question_answers(question_ten, answers_ten) 
    tenth_input = input()
    increase_score(tenth_input)
    if tenth_input == "leave":
        exit()

    if check_if_true(tenth_input) == True:
        eleventh_question()
    else:
        tenth_question()


def eleventh_question():

    print_question_answers(question_eleven, answers_eleven) 
    eleventh_input = input()
    increase_score(eleventh_input)
    if eleventh_input == "leave":
        exit()

    if check_if_true(eleventh_input) == True:
        twelfth_question()
    else:
        eleventh_question()


def twelfth_question():

    print_question_answers(question_twelve, answers_twelve) 
    twelfth_input = input()
    increase_score(twelfth_input)
    if twelfth_input == "leave":
        exit()

    if check_if_true(twelfth_input) == True:
        thirteenth_question()
    else:
        twelfth_question()


def thirteenth_question():

    print_question_answers(question_thirteen, answers_thirteen) 
    thirteenth_input = input()
    increase_score(thirteenth_input)
    if thirteenth_input == "leave":
        exit()

    if check_if_true(thirteenth_input) == True:
        fourteenth_question()
    else:
        thirteenth_question()


def fourteenth_question():

    print_question_answers(question_fourteen, answers_fourteen) 
    fourteenth_input = input()
    increase_score(fourteenth_input)
    if fourteenth_input == "leave":
        exit()

    if check_if_true(fourteenth_input) == True:
        fifteenth_question()
    else:
        fourteenth_question()


def fifteenth_question():

    print_question_answers(question_fifteen, answers_fifteen) 
    fifteenth_input = input()
    increase_score(fifteenth_input)
    if fifteenth_input == "leave":
        exit()

    if check_if_true(fifteenth_input) == True:
        sixteenth_question()
    else:
        fifteenth_question()


def sixteenth_question():

    print_question_answers(question_sixteen, answers_sixteen) 
    sixteenth_input = input()
    increase_score(sixteenth_input)
    if sixteenth_input == "leave":
        exit()

    if check_if_true(sixteenth_input) == True:
        print("This was the last question!")
        print("\nFinal scores:\n")
        print("Gryffindor: " + str(gryffindor))
        print("Slytherin: " + str(slytherin))
        print("Ravenclaw: " + str(ravenclaw))
        print("Hufflepuff: " + str(hufflepuff))
        check_score()


# Call first two functions
print_hogwarts_emblem()
enter_hogwarts()