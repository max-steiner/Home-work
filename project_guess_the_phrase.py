# פרוייקט משחק הניחושים

import random
import time
import sys


store = ["Act without expectation", "All is well", "Always be honest", "Always be yourself", "Be constantly curious",
           "Be here now", "Be the change", "Be the communication", "Believe in yourself", "Believe you can",
           "Change is good", "Connection builds trust", "Do it now", "Do your best", "Dreams come true",
           "Drill your skills", "Focus and win", "Friends are treasures", "Get over it", "Hope trumps all",
           "Just be awesome", "Keep it cool", "Keep it simple", "Knowledge is power", "Learn from yesterday",
           "Life is awesome", "Life is beautiful", "Live life daily", "Love is everything", "Never give up",
           "Never look back"]

def lets_play():
    print()
    print('''                   LET's PLAY THE GAME.\n
    I'll come up with a phrase. You will guess it by the letters.
              For each letter sold you get 5 points.
               For every mistake you lose 1 point.\n''')
    answer = int(input('''DISCLAMER: This game contains scenes of violence, hard sex, rudeness.
           The game is recommended for age 40+.
           If you want to play - press 1 and ENTER. If you don't ready for all this - press 0 and ENTER: '''))
    if answer == 1:
        print("\n")
        print("We start the game.\n")
    else:
        print("\n")
        print("I wish you happiness)))")
        sys.exit()


def get_phrase(store):
    num = random.randint(0, len(store))
    phrase = [word.upper() for word in store[num].split()]
    return phrase


def get_dash(phrase):
    dash = ["_" * len(word) for word in phrase]
    return dash


def counter_letters(phrase):
    num_letter = len(set([letter for word in phrase for letter in word]))
    return num_letter


def make_attempt(dash, phrase, num_attempt, old):
    attempt = input(f"Attempt № {num_attempt}. Please, enter a letter: ").strip().upper()
    while attempt.isalpha() == False or len(attempt) != 1:
        print("Input Error. Enter correct data")
        attempt = input(f"Attempt № {num_attempt}. Please, enter a letter: ").strip().upper()
    while attempt in old:
        print("This letter has already been.")
        attempt = input(f"Attempt № {num_attempt}. Please, enter a letter: ").strip().upper()
    old = old.append(attempt)
    dash_old = dash
    for i, word in enumerate(phrase):
        for j, letter in enumerate(word):
            dash_letter = [list(dash[i]) for i in range(len(dash))]
            if phrase[i][j] == attempt:
                dash_letter[i][j] = attempt
                dash = ["".join(word) for word in dash_letter]
    if dash_old != dash:
        return dash, True
    else:
        return dash, False


def count_score(result, score, attempt_result, mistake):
    if result == True:
        score += 5
        attempt_result += 1
    else:
        score -= 1
        mistake += 1
    return score, attempt_result, mistake


def output_result(dash, result, score):
    l = (50 - len([letter for word in dash for letter in word])) // 2
    if result == True:

        print(f"                 Guess the word or die                  ")
        print(f"#######################################################\n"
              f"##                                                   ##\n"
              f"##       Congratulations!!! Excellent result!        ##\n"
              f"##                                                   ##")
        print(" " * l, *dash, " " * l)
        print(f"##                                                   ##\n"
              f"##                Score in the game: {str(score).ljust(3)}             ##\n"
              f"##                   ( ͡° ͜ʖ ͡°) ✌                   ##\n"
              f"#######################################################")
    else:
        print(f"                 Guess the word or die                  ")
        print(f"#######################################################\n"
              f"##                                                   ##\n"
              f"##              Don't despair! Try again!            ##\n"
              f"##                                                   ##")
        print(" " * l, *dash, " " * l)
        print(f"##                                                   ##\n"
              f"##                Score in the game: {str(score).ljust(3)}             ##\n"
              f"##                 ¯\_( ͡° ͜ʖ ͡°)_/¯                 ##\n"
              f"#######################################################")


def get_end(score, num_attempt, counter_letters, mistake):
    print("\n" * 100)
    print("Congratulations!!! Game over.")
    if num_attempt == counter_letters:
        print("You havn't made any mistakes. For this you get a bonus - 100 points.")
        print(f"Your score: {score + 100}")
    elif counter_letters * 2 > num_attempt > counter_letters * 1.25:
        print("Excellent result")
        print(f"Your score: {score}")
    else:
        print("")
        print("אתה קצת טיפש אחי")
        print()
        print(f"You were wrong {mistake} times. Your score: {score}")

# main

lets_play()
phrase = get_phrase(store)
dash = get_dash(phrase)
#print(phrase)
print(*dash)
print()
counter_letters = counter_letters(phrase)
num_attempt = 0
attempt_result = 0
mistake = 0
score = 0
old = []

start_time = time.time()
time_limit = counter_letters * 7

while attempt_result != counter_letters:
    num_attempt += 1
    dash, result = make_attempt(dash, phrase, num_attempt, old)
    score, attempt_result, mistake = count_score(result, score, attempt_result, mistake)
    print("\n" * 100)
    output_result(dash, result, score)
    if time.time() - start_time > time_limit:
        print("אתה קצת טיפש אחי, חושב יותר מדי זמן אחי. התחל את המשחק מחדש")
        print("#######################################################")
        sys.exit()

if (time.time() - start_time) <= 30:
    score += 100

get_end(score, num_attempt, counter_letters, mistake)


