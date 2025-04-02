import random

maxatt=5
att=1

number=random.randint(20,50)

while att <= 5:

    print(f"\nYou have  {maxatt}  chances left")
    guess=int(input("Guess the number between 20 t0 50 :"))

    if number==guess:
        print("you won!")
        break
    elif number <guess:
        print("Too high! try again")
    else:
        print("Too low! try again")
    att += 1
    maxatt -= 1 
if att==6:
    print(f"out of attempt. The correct number was  {number}")


