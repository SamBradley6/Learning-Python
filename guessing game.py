hidden_number = 9
print("Guess the number (1-9):")

guess = int(input("Guess: "))
guessNumber = 1

while guess != hidden_number:
    if guessNumber < 4:
        print(guess);
        guessNumber += 1
else:
    print("You failed")

print("done")
