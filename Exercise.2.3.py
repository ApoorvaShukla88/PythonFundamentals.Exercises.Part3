import random


def evaluate_number(guessTaken, number):

    if number < guessTaken :
       print("Too Low")
    elif number > guessTaken :
        print("Too High")
    elif number == guessTaken :
       print("Your number is " + str(number))
    elif number != guessTaken :
        print("")


guessTaken = random.randint(1, 5)
print("Guessed number is  " + str(guessTaken))
number = input("Give the number ")
evaluate_number (int(guessTaken), int(number))
