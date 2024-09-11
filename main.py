import random

def validate_number_choice(choice, lower, upper):
    # Could raise a ValueError if the input cannot be converted to an int
    num = int(choice)
    
    if num < lower or num > upper:
        raise ValueError("Supplied number was out of range")

    return num

def get_guess():
    guess = input("Enter a number between 1 and 10: ")
    return validate_number_choice(guess, 1, 10)

def guess_a_number():
    picked_num = random.randint(1, 10)
    got_guess = False

    while not got_guess:
        try:
            guess = get_guess()
            got_guess = True
        except ValueError:
            pass

    if guess == picked_num:
        print(f"You win! The number was {picked_num}")
    else:
        print(f"You lose! The number was {picked_num}")
        
# Uncomment to play game
# guess_a_number()