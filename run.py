from random import shuffle
import os
import re
import sys

import colorama
from colorama import Fore, Back, Style
colorama.init()

# Variables

# All questions and answers in pairs
question_one = Fore.MAGENTA + '\033[1m' + "\n1. Which element resonates most \
with you? \n" + '\033[0m' + Fore.RESET
answers_one = ["- Fire\n", "- Water\n", "- Air\n", "- Earth\n"]

question_two = Fore.MAGENTA + '\033[1m' + "\n2. Late at night, walking alone \
down the street, you hear a peculiar cry that you believe to have a magical \
    source. Do you: \n" + '\033[0m' + Fore.RESET

answers_two = ["- Proceed with caution, keeping one hand on your concealed \
wand and an eye out for any disturbance?\n", "- Draw your wand and try to \
discover the source of the noise?\n", "- Draw your wand and stand your \
ground?\n", "- Withdraw into the shadows to await developments, while \
mentally reviewing the most appropriate defensive and offensive spells, \
should trouble occur?\n"]

question_three = Fore.MAGENTA + '\033[1m' + "\n3. One of your house mates \
has cheated in a Hogwarts exam by using a Self-Spelling Quill. Now he has \
come top of the class in Charms, beating you into second place. Professor \
Flitwick is suspicious of what happened. He draws you to one side after \
his lesson and asks you whether or not your classmate used a forbidden \
quill. What do you do? \n" + '\033[0m' + Fore.RESET

answers_three = ["- Lie and say you don't know (but hope that somebody \
else tells professor flitwick the truth).\n", "- Tell professor flitwick \
that he ought to ask your classmate (and resolve to tell your classmate \
that if he doesn't tell the truth, you will).\n", "- Tell professor \
flitwick the truth. if your classmate is prepared to win by cheating, \
he deserves to be found out. also, as you are both in the same house, \
any points he loses will be regained by you, for coming first in his \
place.\n", "- You would not wait to be asked to tell professor flitwick \
the truth. If you knew that somebody was using a forbidden quill, you \
would tell the teacher before the exam started.\n"]

question_four = Fore.MAGENTA + '\033[1m' + "\n4. After you have died, \
what would you most like people to do when they hear your name? \
\n" + '\033[0m' + Fore.RESET

answers_four = ["- Ask for more stories about your adventures\n", "- \
I don't care what people think of me after I'm dead, it's what they \
think of me while I'm alive that counts\n", "- Think with admiration \
of your achievements\n", "- Miss you, but smile\n"]

question_five = Fore.MAGENTA + '\033[1m' + "\n5. You enter an enchanted \
garden. What would you be most curious to examine first? \
\n" + '\033[0m' + Fore.RESET

answers_five = ["- The statue of an old wizard with a strangely \
twinkling eye\n", "- The bubbling pool, in the depths of which \
something luminous is swirling\n", "- The silver leafed tree \
bearing golden apples\n", "- The fat red toadstools that \
appear to be talking to each other\n"]

question_six = Fore.MAGENTA + '\033[1m' + "\n6. Once every century, \
the Flutterby bush produces flowers that adapt their scent to attract \
the unwary. If it lured you, it would smell of: \n" + '\033[0m' + Fore.RESET

answers_six = ["- A crackling log fire\n", "- The sea\n", "- Fresh \
parchment\n", "- Home\n"]

question_seven = Fore.MAGENTA + '\033[1m' + "\n7. Four goblets are \
placed before you. Which would you choose to drink? \
\n" + '\033[0m' + Fore.RESET

answers_seven = ["- The golden liquid so bright that it hurts the eye, \
and which makes sunspots dance all around the room.\n", "- The mysterious \
black liquid that gleams like ink, and gives off fumes that make you see \
strange visions.\n", "- The foaming, frothing, silvery liquid that sparkles \
as though containing ground diamonds.\n", "- The smooth, thick, richly \
purple drink that gives off a delicious smell of chocolate and plums.\n"]

question_eight = Fore.MAGENTA + '\033[1m' + "\n8. Which road tempts you \
most? \n" + '\033[0m' + Fore.RESET

answers_eight = ["- The wide, sunny, grassy lane\n", "- The narrow, dark, \
lantern-lit alley\n", "- The twisting, leaf-strewn path through woods\n", "- \
The cobbled street lined with ancient buildings\n"]

question_nine = Fore.MAGENTA + '\033[1m' + "\n9. Four boxes are placed before \
you. Which would you try and open? \n" + '\033[0m' + Fore.RESET

answers_nine = ["- The small pewter box, unassuming and plain, with a \
scratched message upon it that reads ‘I open only for the worthy.'\
\n", "- The gleaming jet black box with a silver lock and key, \
marked with a mysterious rune that you know to be the mark of \
Merlin.\n", "- The ornate golden casket, standing on clawed feet, \
whose inscription warns that both secret knowledge and unbearable \
temptation lie within.\n", "- The small tortoiseshell box, \
embellished with gold, inside which some small creature seems to \
be squeaking.\n"]

question_ten = Fore.MAGENTA + '\033[1m' + "\n10. You and two friends need to \
cross a bridge guarded by a river troll who insists on fighting one of \
you before he will let all of you pass. Do you: \n" + '\033[0m' + Fore.RESET

answers_ten = ["- Volunteer to fight\n", "- Suggest that all three of you \
should fight (without telling the troll)?\n", "- Attempt to confuse the \
troll into letting all three of you pass without fighting?\n", "- \
Suggest drawing lots to decide which of you will fight?\n"]

question_eleven = Fore.MAGENTA + '\033[1m' + "\n11. Which would you rather \
be: \n" + '\033[0m' + Fore.RESET

answers_eleven = ["- Trusted\n", "- Praised\n", "- Envied\n", "- Feared\
\n", "- Imitated\n", "- Liked\n"]

question_twelve = Fore.MAGENTA + '\033[1m' + "\n12. If you could have \
any power, which would you choose? \n" + '\033[0m' + Fore.RESET

answers_twelve = ["- The power of invisibility\n", "- The power to read \
minds \n", "- The power to change your appearance at will\n", "- The \
power to change the past\n", "- The power of superhuman strength\
\n", "- The power to speak to animals\n"]

question_thirteen = Fore.MAGENTA + '\033[1m' + "\n13. What are you \
most looking forward to learning at Hogwarts? \
\n" + '\033[0m' + Fore.RESET

answers_thirteen = ["- Apparition and disapparition (being able to \
materialize and dematerialize at will)\n", "- Transfiguration \
(turning one object into another object)\n", "- Flying on a \
broomstick\n", "- Hexes and jinxes\n", "- All about magical \
creatures, and how to befriend/care for them\n", "- Every area \
of magic I can\n"]

question_fourteen = Fore.MAGENTA + '\033[1m' + "\n14. Which of the following \
would you most like to study? \n" + '\033[0m' + Fore.RESET

answers_fourteen = ["- Centaurs\n", "- Ghosts\n", "- Werewolves\n", "- Goblins\
\n", "- Merpeople\n", "- Trolls\n"]

question_fifteen = Fore.MAGENTA + '\033[1m' + "\n15. A Muggle confronts \
you and says that they are sure you are a witch or wizard. Do you: \n" + '\
\033[0m' + Fore.RESET

answers_fifteen = ["- Ask what makes them think so?\n", "- Agree, and \
ask whether they'd like a free sample of a jinx?\n", "- Agree, and \
walk away, leaving them to wonder whether you are bluffing?\n", "- \
Tell them that you are worried about their mental health, and offer \
to call a doctor.\n"]

question_sixteen = Fore.MAGENTA + '\033[1m' + "\n16. How would you \
like to be known to history? \n" + '\033[0m' + Fore.RESET

answers_sixteen = ["- The Bold\n", "- The Great\n", "- The Wise\n", "- \
The Good\n"]

question_seventeen = Fore.MAGENTA + '\033[1m' + "\n17. Given the choice, \
would you rather invent a potion that would guarantee you: \
\n" + '\033[0m' + Fore.RESET

answers_seventeen = ["- Glory\n", "- Power\n", "- Wisdom\n", "- Love\n"]

question_eighteen = Fore.MAGENTA + '\033[1m' + "\n18. Which of the \
following would you most hate people to call you? \n" + '\
\033[0m' + Fore.RESET

answers_eighteen = ["- Cowardly\n", "- Ordinary\n", "- Ignorant\
\n", "- Selfish\n"]

question_nineteen = Fore.MAGENTA + '\033[1m' + "\n19. How would other \
people describe you? \n" + '\033[0m' + Fore.RESET

answers_nineteen = ["- Honest, brave and adventurous\n", "- Deceitful, \
malevolent and sexy\n", "- Curious, analytical and witty\n", "- \
Friendly, happy and dorky\n"]

question_twenty = Fore.MAGENTA + '\033[1m' + "\n20. This seems to be a very \
special and unique situation. You have traits that fit more than one house... \
let me ask you: where would you like be placed? Will it be Gryffindor, \
Slytherin, Ravenclaw or Hufflepuff?\
\n" + '\033[0m' + Fore.RESET

answers_twenty = ["- Gryffindor\n", "- Slytherin\n", "- Ravenclaw\n", "- \
Hufflepuff\n"]

# All answers sorted by houses
gryffindor_answers = ["fire", "cowardly", "the bold", "adventures", "glory", "\
log fire", "golden liquid", "statue", "plain box", "volunteer", "trusted", "\
praised", "invisibility", "change past", "change appearance", "apparition", "\
flying", "centaurs", "ghosts", "werewolves", "bluffing", "woods", "discover \
source", "ask classmate", "honest", "gryffindor"]

slytherin_answers = ["water", "ordinary", "the great", "don't care", "glory\
", "sea", "black liquid", "bubbling pool", "black box", "all three fight", "\
envied", "feared", "read minds", "superhuman strength", "change past", "\
apparition", "hexes", "goblins", "merpeople", "trolls", "jinx", "dark alley\
", "stand your ground", "not wait", "deceitful", "slytherin"]

ravenclaw_answers = ["air", "ignorant", "the wise", "achievements", "wisdom\
", "parchment", "silvery liquid", "silver tree", "golden casket", "confuse \
troll", "envied", "imitated", "read minds", "speak to animals", "change \
appearance",  "transfiguration", "every area", "centaurs", "goblins", "\
ghosts", "what makes them think so", "ancient buildings", "withdraw", "\
tell truth", "curious", "ravenclaw"]

hufflepuff_answers = ["earth", "selfish", "the good", "miss", "love", "\
home", "purple drink", "toadstools", "tortoiseshell box", "drawing lots\
", "trusted", "liked", "invisibility", "superhuman strength", "speak to \
animals", "flying", "magical creatures", "merpeople", "werewolves", "\
trolls", "mental health", "sunny lane", "proceed with caution", "lie\
", "friendly", "hufflepuff"]

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
    Asks user if they want to start the game, and sends them back to start \
    screen when 'no' or anything else than 'yes' or 'no' is entered
    """
    enter = input("                       =========================\
    \n                       ENTER HOGWARTS (YES / NO)\
    \n                       =========================\n")
    if enter == "yes":
        welcome_greeting()
    elif enter == "no":
        print("\nYou just missed your chance to become a great \
        wizard*ess...\n")
        input("Press any key to take the Hogwarts Express back \
        to London\n")
        os.system('clear')
        print_hogwarts_emblem()
        enter_hogwarts()
    else:
        print("\nOnly yes or no answers are valid\n")
        input("Press any key to return\n")
        os.system('clear')
        print_hogwarts_emblem()
        enter_hogwarts()


def welcome_greeting():
    """
    Prints welcome text
    """
    print('\nWelcome to' + Fore.MAGENTA + "\033[1m" + ' Hogwarts \
    School of Witchcraft and Wizardry!' + "\033[22m" + Fore.RESET + '\
    \n\nNow that you have come here it is time for you\nto create \
    your own history and leave behind a legacy in Hogwarts\nonce \
    you have completed your magical studies\nNow before you embark \
    on your journey becoming a wizard*ess\nwe have to sort out an \
    important detail:\nwhich house you will devote yourself to.\n\n\
    You might belong in' + Fore.RED + "\033[1m" + ' Gryffindor ' + "\
    \033[22m" + Fore.RESET + '\nwhere dwell the brave at heart\ntheir \
    daring, nerve and chivalry\nset Gryffindors apart.\n\nOr yet in \
    wise old' + Fore.BLUE + "\033[1m" + " Ravenclaw " + "\033[22m\
    " + Fore.RESET + '\nif you’ve a ready mind\nwhere those of wit \
    and learning\nwill always find their kind.\n\nOr perhaps in\
    ' + Fore.GREEN + "\033[1m" + " Slytherin " + "\033[22m\
    " + Fore.RESET + '\nyou’ll make your real friends,\nthose cunning \
    folk use any means\nto achieve their ends.\n\nOr you might belong \
    in' + Fore.YELLOW + "\033[1m" + " Hufflepuff " + "\033[22m\
    " + Fore.RESET + '\nwhere they are just and loyal\nthose patient \
    Hufflepuffs are true\nand unafraid of toil.\n\nPlease, have a seat \
    on this ceremony chair.\nThe Sorting Hat will know where you belong\
    ...\n')
    print("(The Sorting Hat is placed on your head and it starts talking \
    to you)\n")
    check_name()


def check_name():
    """
    Asks for user name input and checks if it is a valid string
    """
    your_name = input(Fore.CYAN + "\x1B[3m\033[1mYoung wizard*ess, what \
    is your name?\033[0m \x1B[0m\n" + Fore.RESET)
    if re.match(r"[a-zA-Z]", your_name):
        print(Fore.CYAN + '\033[1m' "\x1B[3m\nHello " + your_name + "!\n\n\
        Let me see what house will bring forth the best in you...\n\n...\
        \n...\n...\n")
        print("....now, this is unexpected! The decision is more complex \
        than I thought.\nI will need to get to know you better to find the \
        right house for you.")
        need_more_information()
    else:
        print("\nPlease enter a string that consists of letters a-z or A-Z\n")
        check_name()


def need_more_information():
    """
    Asks user if they are ready to start answering the Sorting Hats' \
    questions and sends them back to start screen when 'no' or anything \
    else than \'yes' or 'no' is entered
    """
    confirm_start = input("\033[1m\n\nAre you ready to dive deeper \
    with me? (YES / NO) \n\033[0m\n" + Fore.RESET).lower()
    if confirm_start == "yes":
        print(Fore.YELLOW + "\033[1m\nI N S T R U C T I O N S: \
        \033[0m" + Fore.RESET + "Choose the answer for each question \
        that describes your personality best. Please enter the identical \
        answer in the input field. After the Sorting Hat has learned \
        enough about you it will place you in the house you belong to...\
        good luck!\n")
        first_question()
    elif confirm_start == "no":
        print("\nMaybe this is not yet the right time for you to discover \
        the world of wizardry.\nI might see you again in a couple of years\
        ...\n")
        input("Press any key to take the Hogwarts Express back to London \n")
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
        exit()
    else:
        print("\nPlease enter one of the given answers")


def check_if_true(input):
    """
    If the check_if_true function returns True (= if a house has gained \
    one point) it will trigger the next question
    If the check_if_true function returns False (= no house has gained \
    any point / the user has entered invalid input) it will trigger the \
    same question again until the user has entered valid input
    """
    if input in gryffindor_answers or input in slytherin_answers or input in ravenclaw_answers or input in hufflepuff_answers:
        return True
    else:
        return False


def exit():
    """
    Brings back user to quiz start page
    """
    reset_score()
    print("\nWhile you are trying to sneak away from the Sorting Ceremony \
    you are being discovered by a grim looking Hogwarts teacher. You can \
    hear him quietly whisper\x1B[3m\033[1m Obliviate \033[0m\x1B[0mbefore \
    your memories start to fade... you find yourself at platform 9¾ at \
    King's Cross Station in London and scratch your head while looking \
    at the platform number. But platform 9¾ does not exist... or does it?\n")
    input("Press any key to go home\n\n")
    os.system('clear')
    print_hogwarts_emblem()
    enter_hogwarts()


def reset_score():
    global gryffindor
    gryffindor = 0
    global slytherin
    slytherin = 0
    global ravenclaw
    ravenclaw = 0
    global hufflepuff
    hufflepuff = 0


def check_score():
    '''
    Checks final score. If one house has the most points this particular \
    house function will be triggered
    If there is a tie, there will be more questions until one house has \
    gained the majority of points
    '''
    if gryffindor > slytherin and gryffindor > hufflepuff and gryffindor > ravenclaw:
        enter_gryffindor()
        return True
    elif slytherin > gryffindor and slytherin > hufflepuff and slytherin > ravenclaw:
        enter_slytherin()
        return True
    elif hufflepuff > gryffindor and hufflepuff > slytherin and hufflepuff > ravenclaw:
        enter_hufflepuff()
        return True
    elif ravenclaw > hufflepuff and ravenclaw > gryffindor and ravenclaw > slytherin:
        enter_ravenclaw()
        return True
    else:
        print("\nMmmmmhhhhh..... it is not an easy decision. I need more \
        time to figure it out...")
        return False


def enter_gryffindor():
    """
    Prints Gryffindor Coat of Arms and lets user know they have been placed \
    in the Gryffindor house
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
    reset_score()
    print("Congratulations! I am prefect Percy Weasley, and I am delighted to \
    welcome you to" + Fore.RED + '\033[1m' + ' GRYFFINDOR HOUSE. ' + '\
    \033[22m' + Fore.RESET + "Our emblem is the lion, the bravest of all \
    creatures; our house colors are scarlet and gold, and our common room lies \
    up in Gryffindor Tower.\n\nThis is, quite simply, the best house at Hogwarts. \
    It is where the bravest and boldest end up - for instance: Albus Dumbledore! \
    Yes, Dumbledore himself, the greatest wizard of our time, was a Gryffindor! \
    If that is not enough for you, I do not know what is.\n\nI will not keep you \
    long, as all you need to do to find out more about your house is to follow \
    Harry Potter and his friends as I lead them up to their dormitories. Enjoy \
    your time at Hogwarts - but how could you fail to? You have become part of \
    the best house in the school.\n")
    input("Press any key to go back to the main hall\n")
    os.system('clear')
    print_hogwarts_emblem()
    enter_hogwarts()


def enter_slytherin():
    """
    Prints Slytherin Coat of Arms and lets user know they have been placed in \
    the Slytherin house
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
    reset_score()
    print("Congratulations! I am prefect Gemma Farley, and I am delighted to \
    welcome you to" + Fore.GREEN + '\033[1m' + ' SLYTHERIN HOUSE. ' + '\
    \033[22m' + Fore.RESET + "Our emblem is the serpent, the wisest of \
    creatures; our house colors are emerald green and silver, and our common \
    room lies behind a concealed entrance down in the dungeons. As you will \
    see, its windows look out into the depths of the Hogwarts lake. We often \
    see the giant squid swooshing by - and sometimes more interesting \
    creatures. We like to feel that our hangout has the aura of a mysterious\
    , underwater shipwreck.\n\nNow, there are a few things you should know \
    about Slytherin and a few you should forget. Firstly, let us dispel a \
    few myths. You might have heard rumours about Slytherin house – that we \
    are all into the Dark Arts, and will only talk to you if your great-\
    grandfather was a famous wizard, and rubbish like that. Well, you do \
    not want to believe everything you hear from competing houses. I am not \
    denying that we have produced our share of Dark wizards, but so have \
    the other three houses – they just do not like admitting it. And yes, \
    we have traditionally tended to take students who come from long lines \
    of witches and wizards, but nowadays you will find plenty of people in \
    Slytherin house who have at least one Muggle parent.\n\nHere is a \
    little-known fact that the other three houses do not bring up much: \
    Merlin was a Slytherin. Yes, Merlin himself, the most famous wizard \
    in history! He learned all he knew in this very house! Do you want \
    to follow in the footsteps of Merlin?\n\nSlytherin is the coolest and \
    edgiest house in this school. We play to win because we care about the \
    honour and traditions of Slytherin. We also get respect from our fellow \
    students. Yes, some of that respect might be tinged with fear, because \
    of our Dark reputation, but you know what? It can be fun, having a \
    reputation for walking on the wild side. Chuck out a few hints that you \
    have got access to a whole library of curses, and see whether anyone \
    feels like nicking your pencil case.\n\nBut we are not bad people. We \
    are like our emblem, the snake: sleek, powerful, and frequently \
    misunderstood. Because you know what Salazar Slytherin looked for in \
    his chosen students? The seeds of greatness. You have been chosen by \
    this house because you have got the potential to be great, in the true \
    sense of the word.\n\nA few more things you might need to know: our \
    house ghost is the Bloody Baron. If you get on the right side of him, \
    he will sometimes agree to frighten people for you. Just do not ask him \
    how he got bloodstained; he does not like it.\n\nWell, I think that is \
    all for now. I am sure you will like our dormitories. We sleep in ancient \
    four-posters with green silk hangings, and bedspreads embroidered with \
    silver thread. Medieval tapestries depicting the adventures of famous \
    Slytherins cover the walls, and silver lanterns hang from the ceilings. \
    You will sleep well; it is very soothing, listening to the lake water \
    lapping against the windows at night.\n")
    input("Press any key to go back to the main hall\n")
    os.system('clear')
    print_hogwarts_emblem()
    enter_hogwarts()


def enter_hufflepuff():
    """
    Prints Hufflepuff Coat of Arms and lets user know they have been placed \
    in the Hufflepuff house
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
    reset_score()
    print("Congratulations! I am Prefect Gabriel Truman, and I am delighted \
    to welcome you to" + Fore.YELLOW + '\033[1m' + ' HUFFLEPUFF HOUSE. ' + '\
    \033[22m' + Fore.RESET + "Our emblem is the badger, an animal that is \
    often underestimated, because it lives quietly until attacked, but \
    which, when provoked, can fight off animals much larger than itself, \
    including wolves. Our house colours are yellow and black, and our \
    common room lies one floor below the ground, on the same corridor \
    as the kitchens.\n\nHufflepuffs are trustworthy and loyal. We do \
    not shoot our mouths off, but cross us at your peril; like our \
    emblem, the badger, we will protect ourselves, our friends and \
    our families against all-comers. Nobody intimidates us.\n\nWhat \
    else do you need to know? Oh yes, the entrance to the common room \
    is concealed in a stack of large barrels in a nook on the right \
    hand side of the kitchen corridor. Tap the barrel two from the \
    bottom, middle of the second row, in the rhythm of Helga \
    Hufflepuff, and the lid will swing open. We are the only house\
     at Hogwarts that also has a repelling device for would-be \
    intruders. If the wrong lid is tapped, or if the rhythm of the \
    tapping is wrong, the illegal entrant is doused in vinegar. Once \
    you have opened the barrel, crawl inside and along the passageway \
    behind it, and you will emerge into the cosiest common room of them \
    all. It is round and earthy and low-ceilinged; it always feels \
    sunny, and its circular windows have a view of rippling grass and \
    dandelions. There is a lot of burnished copper about the place, and \
    many plants, which either hang from the ceiling or sit on the \
    windowsills. Our Head of house, Professor Pomona Sprout, is Head \
    of Herbology, and she brings the most interesting specimens (some \
    of which dance and talk) to decorate our room – one reason why \
    Hufflepuffs are often very good at Herbology.\n\nOur house ghost \
    is the friendliest of them all: the Fat Friar. You will recognise \
    him easily enough; he is plump and wears monks robes, and he is \
    very helpful if you get lost or are in any kind of trouble.\n\nI \
    think that is nearly everything. Once again: congratulations on \
    becoming a member of the friendliest, most decent and most \
    tenacious house of them all.\n")
    input("Press any key to go back to the main hall\n")
    os.system('clear')
    print_hogwarts_emblem()
    enter_hogwarts()


def enter_ravenclaw():
    """
    Prints Ravenclaw Coat of Arms and lets user know they have been \
    placed in the Ravenclaw house
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
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⣿⡿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

⠀⠀⠀⠀⠀⠀
    """ + Fore.RESET)
    reset_score()
    print("Congratulations! I am prefect Robert Hilliard, and I am delighted \
    to welcome you to" + Fore.BLUE + '\033[1m' + ' RAVENCLAW HOUSE. ' + '\
    \033[22m' + Fore.RESET + "Our emblem is the eagle, which soars where \
    others cannot climb; our house colors are blue and bronze, and our \
    common room is found at the top of Ravenclaw Tower, behind a door \
    with an enchanted knocker. The arched windows set into the walls of \
    our circular common room look down at the school grounds: the lake, \
    the Forbidden Forest, the Quidditch pitch and the Herbology gardens. \
    No other house in the school has such stunning views.\n\nWithout wishing \
    to boast, this is the house where the cleverest witches and wizards live. \
    Our founder, Rowena Ravenclaw, prized learning above all else – and so do \
    we. Unlike the other houses, who all have concealed entrances to their \
    common rooms, we do not need one. The door to our common room lies at the \
    top of a tall, winding staircase. It has no handle, but an enchanted \
    bronze knocker in the shape of an eagle. When you rap on the door, this \
    knocker will ask you a question, and if you can answer it correctly, you \
    are allowed in. This simple barrier has kept out everyone but Ravenclaws \
    for nearly a thousand years. Some first-years are scared by having to \
    answer the eagles questions, but do not worry. Ravenclaws learn quickly, \
    and you will soon enjoy the challenges the door sets. It is not unusual \
    to find twenty people standing outside the common room door, all trying \
    to work out the answer to the days question together. This is a great way \
    to meet fellow Ravenclaws from other years, and to learn from them – \
    although it is a bit annoying if you have forgotten your Quidditch robes \
    and need to get in and out in a hurry. In fact, I would advise you to \
    triple-check your bag for everything you need before leaving Ravenclaw \
    Tower.\n\nAnother cool thing about Ravenclaw is that our people are the \
    most individual – some might even call them eccentrics. But geniuses are \
    often out of step with ordinary folk, and unlike some other houses we \
    could mention, we think you have got the right to wear what you like, \
    believe what you want, and say what you feel. We are not put off by \
    people who march to a different tune; on the contrary, we value them!\
    \n\nI think that is nearly everything. Oh yes, our house ghost is the \
    Grey Lady. The rest of the school thinks she never speaks, but she \
    will talk to Ravenclaws. She is particularly useful if you are lost, \
    or you have mislaid something. And once again: well done on becoming \
    a member of the cleverest, quirkiest and most interesting house at \
    Hogwarts!\n")
    input("Press any key to go back to the main hall\n")
    os.system('clear')
    print_hogwarts_emblem()
    enter_hogwarts()


# Quiz Questions

def print_question_answers(question_x, answers_x):
    """
    Template to print answers and questions
    """
    print("\nEnter" + Fore.YELLOW + "\033[1m" + " L E A V E " + "\
    \033[0m" + "to \
    exit the Great Hall\n" + Fore.RESET)
    print(question_x)
    shuffle(answers_x)
    print(*answers_x, sep='\n', end='\n\n')


def first_question():
    """
    Triggers first question and asks user for answer input.
    The same function description is applicable for all
    questions and therefore omitted after this one.
    """
    print_question_answers(question_one, answers_one)
    first_input = input().lower()
    increase_score(first_input)

    if check_if_true(first_input) is True:
        second_question()
    elif check_if_true(first_input) is False:
        first_question()
    elif first_input == "leave":
        exit()


def second_question():

    print_question_answers(question_two, answers_two)
    second_input = input().lower()
    increase_score(second_input)

    if check_if_true(second_input) is True:
        third_question()
    elif check_if_true(second_input) is False:
        second_question()
    elif second_input == "leave":
        exit()


def third_question():

    print_question_answers(question_three, answers_three)
    third_input = input().lower()
    increase_score(third_input)

    if check_if_true(third_input) is True:
        fourth_question()
    elif check_if_true(third_input) is False:
        third_question()
    elif third_input == "leave":
        exit()


def fourth_question():

    print_question_answers(question_four, answers_four)
    fourth_input = input().lower()
    increase_score(fourth_input)

    if check_if_true(fourth_input) is True:
        fifth_question()
    elif check_if_true(fourth_input) is False:
        fourth_question()
    elif fourth_input == "leave":
        exit()


def fifth_question():

    print_question_answers(question_five, answers_five)
    fifth_input = input().lower()
    increase_score(fifth_input)

    if check_if_true(fifth_input) is True:
        print("\nCurrent scores:\n")
        print("Gryffindor: " + str(gryffindor))
        print("Slytherin: " + str(slytherin))
        print("Ravenclaw: " + str(ravenclaw))
        print("Hufflepuff: " + str(hufflepuff))
        sixth_question()
    elif check_if_true(fifth_input) is False:
        fifth_question()
    elif fifth_input == "leave":
        exit()


def sixth_question():

    print_question_answers(question_six, answers_six)
    sixth_input = input().lower()
    increase_score(sixth_input)

    if check_if_true(sixth_input) is True:
        seventh_question()
    elif check_if_true(sixth_input) is False:
        sixth_question()
    elif sixth_input == "leave":
        exit()


def seventh_question():

    print_question_answers(question_seven, answers_seven)
    seventh_input = input().lower()
    increase_score(seventh_input)

    if check_if_true(seventh_input) is True:
        eighth_question()
    elif check_if_true(seventh_input) is False:
        seventh_question()
    elif seventh_input == "leave":
        exit()


def eighth_question():

    print_question_answers(question_eight, answers_eight)
    eighth_input = input().lower()
    increase_score(eighth_input)

    if check_if_true(eighth_input) is True:
        ninth_question()
    elif check_if_true(eighth_input) is False:
        eighth_question()
    elif eighth_input == "leave":
        exit()


def ninth_question():

    print_question_answers(question_nine, answers_nine)
    ninth_input = input().lower()
    increase_score(ninth_input)

    if check_if_true(ninth_input) is True:
        tenth_question()
    elif check_if_true(ninth_input) is False:
        ninth_question()
    elif ninth_input == "leave":
        exit()


def tenth_question():

    print_question_answers(question_ten, answers_ten)
    tenth_input = input().lower()
    increase_score(tenth_input)

    if check_if_true(tenth_input) is True:
        eleventh_question()
    elif check_if_true(tenth_input) is False:
        tenth_question()
    elif tenth_input == "leave":
        exit()


def eleventh_question():

    print_question_answers(question_eleven, answers_eleven)
    eleventh_input = input().lower()
    increase_score(eleventh_input)

    if check_if_true(eleventh_input) is True:
        twelfth_question()
    elif check_if_true(eleventh_input) is False:
        eleventh_question()
    elif eleventh_input == "leave":
        exit()


def twelfth_question():

    print_question_answers(question_twelve, answers_twelve)
    twelfth_input = input().lower()
    increase_score(twelfth_input)

    if check_if_true(twelfth_input) is True:
        thirteenth_question()
    elif check_if_true(twelfth_input) is False:
        twelfth_question()
    elif twelfth_input == "leave":
        exit()


def thirteenth_question():

    print_question_answers(question_thirteen, answers_thirteen)
    thirteenth_input = input().lower()
    increase_score(thirteenth_input)

    if check_if_true(thirteenth_input) is True:
        fourteenth_question()
    elif check_if_true(thirteenth_input) is False:
        thirteenth_question()
    elif thirteenth_input == "leave":
        exit()


def fourteenth_question():

    print_question_answers(question_fourteen, answers_fourteen)
    fourteenth_input = input().lower()
    increase_score(fourteenth_input)

    if check_if_true(fourteenth_input) is True:
        print("\nCurrent scores:\n")
        print("Gryffindor: " + str(gryffindor))
        print("Slytherin: " + str(slytherin))
        print("Ravenclaw: " + str(ravenclaw))
        print("Hufflepuff: " + str(hufflepuff))
        fifteenth_question()
    elif check_if_true(fourteenth_input) is False:
        fourteenth_question()
    elif fourteenth_input == "leave":
        exit()


def fifteenth_question():

    print_question_answers(question_fifteen, answers_fifteen)
    fifteenth_input = input().lower()
    increase_score(fifteenth_input)

    if check_if_true(fifteenth_input) is True and check_score() is False:
        sixteenth_question()
    elif check_if_true(fifteenth_input) is False:
        fifteenth_question()
    elif fifteenth_input == "leave":
        exit()


def sixteenth_question():

    print_question_answers(question_sixteen, answers_sixteen)
    sixteenth_input = input().lower()
    increase_score(sixteenth_input)

    if check_if_true(sixteenth_input) is True and check_score() is False:
        seventeenth_question()
    elif check_if_true(sixteenth_input) is False:
        sixteenth_question
    elif sixteenth_input == "leave":
        exit()


def seventeenth_question():

    print_question_answers(question_seven, answers_seven)
    seventeenth_input = input().lower()
    increase_score(seventeenth_input)

    if check_if_true(seventeenth_input) is True and check_score() is False:
        eighteenth_question()
    elif check_if_true(seventeenth_input) is False:
        seventeenth_question()
    elif seventeenth_input == "leave":
        exit()


def eighteenth_question():

    print_question_answers(question_eight, answers_eight)
    eighteenth_input = input().lower()
    increase_score(eighteenth_input)

    if check_if_true(eighteenth_input) is True and check_score() is False:
        nineteenth_question()
    elif check_if_true(eighteenth_input) is False:
        eighteenth_question()
    elif eighteenth_input == "leave":
        exit()


def nineteenth_question():

    print_question_answers(question_nineteen, answers_nineteen)
    nineteenth_input = input().lower()
    increase_score(nineteenth_input)

    if check_if_true(nineteenth_input) is True and check_score() is False:
        twentieth_question()
    elif check_if_true(nineteenth_input) is False:
        nineteenth_question()
    elif nineteenth_input == "leave":
        exit()


def twentieth_question():
    """
    In the unlikely case that there should be a tie
    still after the twentieth question the user
    can vote which house they want to belong to.
    """
    print_question_answers(question_twenty, answers_twenty)
    twentieth_input = input().lower()
    increase_score(twentieth_input)
    blockPrint()
    if check_if_true(twentieth_input) is True and check_score() is False:
        enablePrint()
        if twentieth_input == "gryffindor":
            enter_gryffindor()
        elif twentieth_input == "slytherin":
            enter_slytherin()
        elif twentieth_input == "ravenclaw":
            enter_ravenclaw()
        elif twentieth_input == "hufflepuff":
            enter_hufflepuff()
    elif check_if_true(twentieth_input) is False:
        twentieth_question()
    elif twentieth_input == "leave":
        exit()


def blockPrint():
    """
    Marks beginning of blocking the print function.
    Here used within twentieth_question to prevent check_score
    print statement to be shown which in this case is
    not applicable anymore
    """
    sys.stdout = open(os.devnull, 'w')


def enablePrint():
    """
    Marks ending of blocking the print function.
    """
    sys.stdout = sys.__stdout__


# Call first two functions
print_hogwarts_emblem()
enter_hogwarts()