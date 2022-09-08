import random
from colorama import Fore, Back, Style

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m{}\033[00m".format(skk),end="")
def prYellow(skk): print("\033[93m{}\033[00m".format(skk),end="")

def checkpoint(guess,a):
    flag=1
    for i in range(0,5,1):
        if guess[i]==a[i]:
            prGreen(guess[i])
            # print('The letter',guess[i],'is in the word and in the correct spot')
        else:
            flag=0
            for j in range(0,5,1):
                if guess[i]==a[j]:
                    flag=1;
                    prYellow(guess[i])
                    # print('The letter', guess[i], 'is in the word but in the wrong spot')
                    break;

            if flag==0:
                print(guess[i],end="")
                # print('The letter', guess[i], 'is not in the word in any spot')

title='Welcome to WORD-DARE'
str=title.center(150)
print(Fore.BLACK + Back.GREEN + str)
print(Style.RESET_ALL)
with open("dictionary.txt", "r") as file:
    data = file.read()
    words = data.split()

    # Generating a random number for word position
    word_pos = random.randint(0, len(words) - 1)
    word=words[word_pos]
    # print(word)
    # print("Word:", words[word_pos])
    # print("Position in the dictionary:", word_pos)

guess1=input('\nEnter your first guess of the word : ')
if guess1 not in data:
    while guess1 not in data:
        guess1=input('Not in word list. Enter a valid word : ')
if word==guess1:
    prGreen(word)
    print('\nGENIUS!!!...That is correct\nYou won \U0001F929')
else:
    checkpoint(guess1,word)
    guess2 = input('\n\nEnter your second guess of the word : ')
    if guess2 not in data:
        while guess2 not in data:
            guess2 = input('Not in word list. Enter a valid word : ')
    if word==guess2:
        prGreen(word)
        print('\nMAGNIFICENT!...That is correct\nYou won \U0001F929')
    else:
        checkpoint(guess2, word)
        guess3 = input('\n\nEnter your third guess of the word : ')
        if guess3 not in data:
            while guess3 not in data:
                guess3 = input('Not in word list. Enter a valid word : ')
        if word == guess3:
            prGreen(word)
            print('\nImpressive!...That is correct\nYou won \U0001F929')
        else:
            checkpoint(guess3, word)
            guess4 = input('\n\nEnter your fourth guess of the word : ')
            if guess4 not in data:
                while guess4 not in data:
                    guess4 = input('Not in word list. Enter a valid word : ')
            if word == guess4:
                prGreen(word)
                print('\nSplendid!...That is correct\nYou won \U0001F929')
            else:
                checkpoint(guess4, word)
                guess5 = input('\n\nEnter your fifth guess of the word : ')
                if guess5 not in data:
                    while guess5 not in data:
                        guess5 = input('Not in word list. Enter a valid word : ')
                if word == guess5:
                    prGreen(word)
                    print('\nGreat!...That is correct\nYou won \U0001F929')
                else:
                    checkpoint(guess5, word)
                    guess6 = input('\n\nEnter your last guess of the word : ')
                    if guess6 not in data:
                        while guess6 not in data:
                            guess6 = input('Not in word list. Enter a valid word : ')
                    if word == guess6:
                        prGreen(word)
                        print('\nPhew!...That is correct\nYou won \U0001F929')
                    else:
                        print('Answer : ',word)
                        print('Hard cheese \U00002639\t Better luck next time')


'''
TASKS TO BE DONE: 
- word size == 5, !>5 && !<5
- wordle engine to show possible answers
- Generate alphabet set after every word entry
'''