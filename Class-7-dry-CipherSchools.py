guess = 1
number = int(input("guess a number between 1 and 100 : "))
game_over = False
while not game_over:
    if number == winning-number:
        print(f"you win, and you guessed this number in {guess} times")
        break
    else:
        if number < winning-number:
            print("too low")
        else:
            print("too high")

        guess += 1
        continue
    # Dry - don't repeat yourself