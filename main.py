#  Guess Game generation codes
import random

c = 0
while c < 5:
    x = random.randint(1, 50)

    n = int(input("Enter your guess between 1 to 50: "))

    if n > x:
        print("You choose bigger number")

    elif n < x:
        print("you choose smaller number")

    elif n == x:
        print("Congrats! you guessed the number ")
        print("the no of chances the user took:", c)
        break
    else:
        continue

    c = c + 1

    if c == 5:
        print("the no of chances the user took:", c)
        print(x)
        break

    else:
        continue
