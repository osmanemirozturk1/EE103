from secret_number_w3 import secretNum

attempts = 0

while True:
    guess = int(input("Guess the secret number: "))
    attempts += 1

    if guess  == secretNum:
        print("Congratulations! You found it.")
        break
    elif guess < secretNum:
        print("Too low")
    else:
        print("Too high")    

    if attempts >= 5:
        print("You failed after 5th guess!")
        while True:
            print("Oh! Nooooooo...")
            