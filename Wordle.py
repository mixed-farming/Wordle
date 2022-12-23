import random
import string
import pyttsx3
from PyDictionary import PyDictionary

from colorama import Fore, Back, Style
def prRed(skk): print("\033[91m {}\033[00m".format(skk))
def prGreen(skk): print("\033[92m{}\033[00m".format(skk), end="")
def prYellow(skk): print("\033[93m{}\033[00m".format(skk), end="")
def prOrange(skk): print("\033[33m{}\033[00m".format(skk), end="")

def checkpoint(guess, a):
    flag = 1
    for i in range(0, 5, 1):
        if guess[i] == a[i]:
            prGreen(guess[i])
            # print('The letter',guess[i],'is in the word and in the correct spot')
        else:
            flag = 0
            for j in range(0, 5, 1):
                if guess[i] == a[j]:
                    flag = 1;
                    prOrange(guess[i])
                    # print('The letter', guess[i], 'is in the word but in the wrong spot')
                    break;

            if flag == 0:
                print(guess[i], end="")
                # print('The letter', guess[i], 'is not in the word in any spot')

title = 'Welcome to WORD-DARE'
heading = title.center(150)
print(Fore.BLACK + Back.GREEN + heading)
print(Style.RESET_ALL)
with open("dictionary.txt", "r") as file:
    data = file.read()
    words = data.split()

    # Generating a random number for word position
    word_pos = random.randint(0, len(words) - 1)
    answer = words[word_pos]
    # print(word)
    # print("Word:", words[word_pos])
    # print("Position in the dictionary:", word_pos)

# alphabet_set=[]
alphabet_set = list(string.ascii_lowercase)
alphabet_set[0]= (Fore.GREEN + alphabet_set[0])
# print(alphabet_set[0])
# print('Letter set :', Fore.YELLOW + alphabet_set[0],end=" ")
# print(Fore.GREEN + alphabet_set[1])

guess1 = input('\nEnter your first guess of the word : ')
if guess1 not in data:
    while guess1 not in data:
        guess1 = input('Not in word list. Enter a valid word : ')
if answer == guess1:
    prGreen(answer)
    print('\nGENIUS!!!...That is correct\nYou won \U0001F929')
else:
    checkpoint(guess1, answer)
    guess2 = input('\n\nEnter your second guess of the word : ')
    if guess2 not in data:
        while guess2 not in data:
            guess2 = input('Not in word list. Enter a valid word : ')
    if answer == guess2:
        prGreen(answer)
        print('\nMAGNIFICENT!...That is correct\nYou won \U0001F929')
    else:
        checkpoint(guess2, answer)
        guess3 = input('\n\nEnter your third guess of the word : ')
        if guess3 not in data:
            while guess3 not in data:
                guess3 = input('Not in word list. Enter a valid word : ')
        if answer == guess3:
            prGreen(answer)
            print('\nImpressive!...That is correct\nYou won \U0001F929')
        else:
            checkpoint(guess3, answer)
            guess4 = input('\n\nEnter your fourth guess of the word : ')
            if guess4 not in data:
                while guess4 not in data:
                    guess4 = input('Not in word list. Enter a valid word : ')
            if answer == guess4:
                prGreen(answer)
                print('\nSplendid!...That is correct\nYou won \U0001F929')
            else:
                checkpoint(guess4, answer)
                guess5 = input('\n\nEnter your fifth guess of the word : ')
                if guess5 not in data:
                    while guess5 not in data:
                        guess5 = input('Not in word list. Enter a valid word : ')
                if answer == guess5:
                    prGreen(answer)
                    print('\nGreat!...That is correct\nYou won \U0001F929')
                else:
                    checkpoint(guess5, answer)
                    guess6 = input('\n\nEnter your last guess of the word : ')
                    if guess6 not in data:
                        while guess6 not in data:
                            guess6 = input('Not in word list. Enter a valid word : ')
                    if answer == guess6:
                        prGreen(answer)
                        print('\nPhew!...That is correct\nYou won \U0001F929')
                    else:
                        print('Answer : ', answer)
                        print('Hard cheese \U00002639\t Better luck next time')

class Speaking:
    def speak(self, audio):
        # Having the initial constructor of pyttsx3
        # and having the sapi5 in it as a parameter
        engine = pyttsx3.init('sapi5')

        # Calling the getter and setter of pyttsx3
        voices = engine.getProperty('voices')

        # Method for the speaking of the assistant
        engine.setProperty('voice', voices[0].id)
        engine.say(audio)
        engine.runAndWait()


class My:
    def Dictionary(self):
        speak = Speaking()
        dic = PyDictionary()
        # speak.speak("Which word do u want to find the meaning sir")

        # Taking the string input
        query = answer
        word = dic.meaning(query)
        print(len(word))

        for state in word:
            print(word[state])
            speak.speak("The meaning of the word" + answer + "is" + str(word[state]))

My()
My.Dictionary(self=None)

'''
TASKS TO BE DONE:
- wordle engine to show possible answers
- Generate alphabet set after every word entry
'''
