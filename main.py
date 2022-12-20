import random

number = random.randint(1, 11)
player = input("Hello, What is your name? ")
number_of_guesses = 0
print('Okay! ' + player + ' I will think of a number between 1 to 10')
print('Guess the Number.')

while number_of_guesses <= 5:
    guess = int(input())
    number_of_guesses += 1
    if guess > number:
        print("The guess is high")
    elif guess < number:
        print("The guess is lower")
    elif guess == number:
        break

if guess == number:
    print("You have guessed the number correct in " + str(number_of_guesses) + " Attempts")
else:
    print("You did not guess the number correctly. The correct number is " + str(number))