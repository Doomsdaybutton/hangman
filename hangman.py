import random

words = ["berg", "banane", "automobil", "cool", "desoxyribonukleinsäure"]
word = random.choice(words)
maxMistakes = len(word)
maxGuesses = len(word) * 2
letters = []
guesses = 0
mistakes = 0

def printWord(word):
    final = ""
    for i in word:
        if i in letters:
            final += i + ' '
        else:
            final += " _ "
    print(final)

def won(word):
    for i in word:
        if i in letters:
            continue
        else:
            return False
    return True


while(guesses < maxGuesses):
    guesses += 1
    print("Guess " + str(guesses) + " | Mistakes: " + str(mistakes))
    printWord(word)
    guess = input("Type guess...")
    while(len(guess) != 1):
        print("Unvalid guess!")
        guess = input("Type new guess...")
    if guess in letters:
        print("You already guessed that one!")
        guesses -= 1
    else:
        letters.append(guess)
        if guess in word:
            print("Good guess!")
        else:
            print("Bad guess!")
            mistakes += 1
    if mistakes >= maxMistakes:
        print("To many mistakes: You lost!")
        break
    else:
        if won(word):
            print("You won!")
            print("The word was: " + word)
            break
else:
  print("No guesses left: You lost!")