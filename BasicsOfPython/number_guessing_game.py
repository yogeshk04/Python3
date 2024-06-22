import random

winning_number = random.randint(1,50)
# winning_number = 44
guess = 1
number = int(input('Guess a number between 1 to 50: '))
# game_over = False

# while not game_over:
while True:
    if number == winning_number:
        print(f'You own the game and you have guess this in {guess} number.')
        # game_over = True
        break
    else:
        if number < winning_number:
            print("Your guess is too low.")
            # guess += 1
            # number = int(input("Please try again: "))
        else:
            print("Your guess is high")
            # guess += 1
            # number = int(input('Please try again: '))
        guess += 1
        number = int(input('Please try again: '))
