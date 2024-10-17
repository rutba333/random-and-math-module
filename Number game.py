import random
playing=True
number=str(random.randint(10,20))

print("I will generate a number between 1 to 9 and you have to guess the number one digit for one time")
print("The game ends you will get a hero!")

while playing:
    guess=input("Give me your best guess.\n")
    if number==guess:
        print("Well done your guess is correct!")
        print("The number was:",number)
        break
    else:
        print("your guess is not right")

