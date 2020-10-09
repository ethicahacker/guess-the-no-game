#  Guess Game generation codes
import random

c = 0
while c < 5:
    x = random.randint(1, 50)

    n = eval(input("Enter your guess between 1 to 50: "))

    if n < x or :
        print("You choice very small number")

     elif n > (x + 5):
         print("You are very near to the number")
    
     elif n > (x + 3):
         print("you are near to the number")

    elif n > x:
        print("you choice is bigger than the number")

     elif n < (x + 5):
         print("you are very after the number")
    
     elif n < (x + 3):
         print("you are a little after the number")

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
