#Program shd generate a random number, in a certain range ; (0-10)
#Ask the user to guess it - INPUT from user required
#The program shd be able to give feedback whether the guess is too high or too low
#shd quit right away if the guess ''' is right

#Need to implement where the user decides the range and decide attempts

import random
from art import text2art

print("")
print("")

print("WELCOME TO GUESS GAME" + "\033[3m by AndrewPyrookie\033[0m") #italicizing and center 


print("")
print("")

go = text2art("GO!", font="block")
print(go)

print("")
c = input("Continue 'y':")
print("")

print('''Hello There !
      The instructions are : Just Try to guess the right number😄.
      Good Luck!!''')


print("")
c = input("Continue 'y':")
print('''You get to decide the range you want to play within:
      x =takes minimum
      y = takes max...range x to y
      Choose a short range about 10 numbers, make it easier for you!!
      If you choose a longer range ,try increasing attempts.''')

x = int(input("x,the minimum : "))
y = int(input("y,the maximum : "))

print(f"Guess in the range {x} - {y} ")

print("")
c = input("Continue 'y':")
print("")

constant = random.randint(x, y) #Setting the answer
Guess = 0
n = 0

print("")
attempts = int(input("How many attempts do you prefer? : "))
print("")

while n != attempts:
    Guess = int(input("Guess Attempt : "))
    if int(Guess) == constant:
        print(f"Correct guess {constant}, is the correct")
        break
    else:
        if int(Guess) > constant:
            print("That Guess is too big!!")
        else:
            print("That Guess is too less!!")
    n = n + 1
else:
    print("Sorry,You have reached maximum guessing trials!!")   
     