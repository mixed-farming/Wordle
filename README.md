# Wordle

<!-- <p align="center"><img width="75%" src="" alt="wordle game gif" /> -->

## Game's rule
  The rules of this word guessing game are simple and straightforward. A word of 5 letters is randomly generated from the dictionary file I have included. You get a total of 6 chances to get the word right. Once a guess is made the letters of that word turn grey, yellow, or green, indicating whether you are on the correct track to guess the word. If the box turns to green colour, it tells you that both the letter and the letter's position are right. If the space turns yellow, it implies that even though the letter is right, it is placed wrongly. The letter is incorrect if the box turns grey.
  
## Play it on terminal
### Upgrade pip
```
python3 -m pip install --upgrade pip
```
### Install necessary libraries
```
pip install pyttsx3
```
```
pip install PyDictionary
```
```
pip install comtypes
```

## Things to be done
- wordle engine to show possible answers
- Generate alphabet set after every word entry
