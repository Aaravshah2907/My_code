import time

from random_word import RandomWords
import time as t

r = RandomWords()
word = r.get_random_word()
word = word.upper()

set_letters = set(word)
if len(set_letters)>4:
    set_letters.pop()
    set_letters.pop()
    set_letters.pop()


def word_display():
    temp = word
    for element in set_letters:
        temp = temp.replace(element, '-')
    return temp


loop_left = int(len(set_letters)*3-2)
print("Tries received:", loop_left)

print("Word left            :   ", word_display())

while loop_left > 0:
    guess = input("Enter Your Guess Letter : ")
    guess = guess.upper()
    if guess in set_letters:
        set_letters.remove(guess)
        print("Word left            :   ", word_display())
        if word_display() == word:
            loop_left = 0
    elif guess in word:
        print("Letter Already used")
    else:
        loop_left -= 1
        print("Guess Again")
        print("Tries left : ", loop_left)
        print("Word left            :   ", word_display())

if word == word_display():
    print("Congrats, U won")
else:
    print("Sorry, better luck next time")
    print("The word was :", word)

time.sleep(5.50)
