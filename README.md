# Wordle

<!-- <p align="center"><img width="75%" src="" alt="wordle game gif" /> -->

## Gameplay
  The rules of this word guessing game are simple and straightforward. A word of 5 letters is randomly generated from the dictionary file I have included. You get a total of 6 chances to get the word right. Once a guess is made the letters of that word turn grey, yellow, or green, indicating whether you are on the correct track to guess the word. If the box turns to green colour, it tells you that both the letter and the letter's position are right. If the space turns yellow, it implies that even though the letter is right, it is placed wrongly. The letter is incorrect if the box turns grey.
  
## Requirements
Linux Terminal
OR
Python compiler: PyCharm
  
## Play it on terminal
### Installation:
```
wget https://raw.githubusercontent.com/mixed-farming/Wordle/main/Wordle.py
```
```
wget https://raw.githubusercontent.com/mixed-farming/Wordle/main/dictionary.txt
```
### Upgrade pip:
```
python3 -m pip install --upgrade pip
```
### Install necessary libraries:
#### pyttsx3 is a text-to-speech conversion library in Python.
```
pip install pyttsx3
```
#### PyDictionary is a Dictionary Module for Python 2/3 to get meanings, translations, synonyms and Antonyms of words.
```
pip install PyDictionary
```
#### comtypes is a pure Python COM package based on the ctypes ffi foreign function library.
```
pip install comtypes
```
### Running:
```
python3 Wordle.py
```

## Things to be done
- Wordle engine to show possible answers
- Generate alphabet set after every word entry
- Computer generated voice revealing the word with it's meaning
