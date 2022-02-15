import random

count = 0

guessed_number = random.randint(1, 20)

name = input("Hello! What is your name?\n")

print("Well", name, "I am thinking of a number between 1 and 20.", sep=", ")
guess = 0
while guess != guessed_number:
    count += 1
    guess = int(input("Take a guess.\n"))
    if guess != guessed_number and guess < guessed_number:
        print("Your guess is too low.")
    elif guess != guessed_number and guess > guessed_number:
        print("Your guess is too high.")

if guess == guessed_number:
    print("Good job, " + name + "! You guessed my number in " + str(count) + " guesses!", sep="")