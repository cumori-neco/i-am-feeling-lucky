import random

# 0 - rock ; 1 - paper ; 2 - scissors
# 0 beats 2, 2 beats 1, 1 beats 0
next_move = random.randint(0, 2)

def game() -> bool:
    try:
        player_move = int(input("Rock, Paper, Scissors (input 0, 1, 2) : "))
    except ValueError:
        print("Invalid input, enter a number between 0 and 2.")
        return game()

    if player_move not in (0, 1, 2):
        print("Invalid input, kindly fuck off")
        return False

    if player_move == next_move:
        print("Tie, another one.")
        return game()

    match next_move:
        case 0:
            print("Computer chose rock.")
        case 1:
            print("Computer chose paper.")
        case 2:
            print("Computer chose scissors.")

    match (player_move, next_move):
        case (1, 0) | (2, 1) | (0, 2):
            print("You won.")
            return True
        case _:
            print("You lost...")
            return False