import math
import random

# Taking inputs
lower = int(input("Enter lower bound: - "))
upper = int(input("Enter upper bound: - "))

# Generating number between lower and higher
x = random.randint(lower, upper)
print("\n\tYou've only", round(math.log(upper - lower + 1, 2)),
      "chances to guess the number!")

# Number of guesses
counter = 0

while counter < int(math.log(upper - lower + 1, 2)):
    counter += 1

    # taking guessing number
    guess = int(input("Guess a number: - "))

    # Condition testing
    if x == guess:
        print("Congrats you guessed it in ", counter, "try")
        break
    elif x > guess:
        print("You guessed too small")
    elif x < guess:
        print("You guessed too high")

if counter >= int(math.log(upper - lower + 1, 2)):
    print("\nThe number is %d" % x)
    print("\t Better luck next time")
