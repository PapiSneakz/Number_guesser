import random

while True:
    print("------------------------------------")
    print("say the range I should choose the number from")
    number1 = int(input("Number 1: "))
    number2 = int(input("Number 2: "))
    Player = int(input("Guess the number im thinking of: "))
    Number = random.randint(number1,number2)
    Guesses = 1

    while True:
        if Player != Number:
            if Player > number2:
                print("How did you choose above your range...")
            else:
                print("Wrong hihi")
            Player = int(input("Try again: "))
            Guesses += 1
        if Player == Number:
            break
    print("You guessed it in " + str(Guesses) + " attempts")
    print("-----------------------------------------")

    play_again = input("Do you wanna play again?(yes or no): ")
    play_again.lower()
    if play_again != "yes":
        print("Okay bye bye")
        break
