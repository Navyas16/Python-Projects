#importing random module
import random

name = input("Your name: ")
print("Hello " + name)

lower_limit = int(input("Enter ur lower limit:"))
upper_limit = int(input("Enter ur upper limit:"))

#Generating random number using random.randint function
number = random.randint(lower_limit,upper_limit)

chances = 7

print("You have only 7 chances")
while chances > 0:
    guess = int(input("Your guess: "))
    if guess == number:
        print("You have successfully guessed the number")
        print("Congratulations !!")
        print(f"The number is {number}")
        break
    elif guess > number:
         print("its too high")  
    else:
        print("its too low")
    chances-=1
    
if chances == 0:
    print("Better luch next time")
    print(f"The number is {number}")
    
