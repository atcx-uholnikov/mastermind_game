"""
1. Generate a 4 color random code
2. Make the user guess the code
3. Compare the guess with real code
4. Tie the game together
"""

import random

COLORS = ["R", "G", "B", "Y", "W", "O"] # Red, Green, Blue, Yellow, White, Orange
TRIES = 5
CODE_LENGTH = 4 #number of code elements > e.g.: code = ["R", "G", "B", "O"])

#creates a random code combination of colors (code elemets)
def generate_code():
    code = []

    for i in range(CODE_LENGTH):
        code_element = random.choice(COLORS)
        code.append(code_element)

    return code

def guess_code():

    while True:

        #convert str input into a list | e.g.: "G G R B".split(" ") -> ["G", "G", "R", "B"]
        guess = input("Enter you guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"Plese enter only {CODE_LENGTH} colors")
            continue #returns to while loop

        for color in guess:
            if color not in COLORS:
                print(f"'{color}' is invalid color. Try again.")
                break

        else: #will execute only if while loop is not terminated by other break or return statements
            break

    return guess

def check_code(guess, code):

    wrong = 0

    correct = []

    for ind, color in enumerate(guess):
        if color != code[ind]:
            wrong += 1
            correct.append("-")
        else:
            correct.append(color)

    print(f"In your guess {wrong} wrong possitions:", *correct)

    return wrong

def play():

    print("Hi! It`s a Mastermind game.")
    print(f"Guess the code in {TRIES} tries. Valid colors are:", *COLORS)

    code = generate_code()
    #print(code)
    attempt = 0
    for attempts in range(1, TRIES+1):
        guess = guess_code()
        wrong = check_code(guess, code)
        attempt += 1

        if wrong == 0:
            print("The code is:", *code, "| your guess is:", *guess)
            print(f"YOU GUESSED THE CODE IN {attempt} ATTEMPT(S)! CONGRATS!")
            break

        print(f"You have {TRIES-attempt} attempt(s)")

    else:
        print("You ran out of tries. Code was:", *code)

if __name__ == "__main__":
    play()
