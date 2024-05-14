hidden_number = 9
print("Guess the number (1-9):")
guess = int(input("Guess: "))
guessNumber = 0

while guess != hidden_number:
    guessNumber += 1
    print(f"guess number {guessNumber}")
    if guessNumber == 3: {
        print("Out of guesses");
    }
    break
    print("Guess again")
    guess = int(input("Guess: "))

    if guess == hidden_number: {
        print("You win")
    }



