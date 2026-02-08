# import libraries, standard followed by personal
import random

import walkertools

GAME_RULES = (
    "In Rock Paper Scissors, two players simultaneously choose one of three symbols: "
    "Rock (beats Scissors), Paper (beats Rock), or Scissors (beats Paper). "
    "In this terminal version, you will play against the computer in a Best of Three match, "
    "meaning the first player to win two rounds is declared the overall victor. "
    "If both players choose the same symbol, the round is a draw and must be replayed "
    "until a winner for that round is determined."
)

print(walkertools.create_banner("Rock! Paper! Scissors!", "*"))
walkertools.print_blank_lines(2)
wants_rules = input("Do you need a refresher on the rules? Y/N: ").lower()

if wants_rules.startswith("y"):
    walkertools.print_blank_lines(2)
    print(GAME_RULES)
    walkertools.print_blank_lines(2)

print("Well then, let's begin")
input("Press Enter to continue...")
walkertools.clear_screen()


# print scoreboard and kickoff game
def print_scoreboard(p_score, c_score):
    scoreboard_width = 36
    print("*" * scoreboard_width)
    print("Scoreboard".center(scoreboard_width))
    print(f"Player Score: {p_score} Computer Score: {c_score}".center(scoreboard_width))
    print("*" * scoreboard_width)


WINNING_SCORE = 2
player_score = 0
computer_score = 0

print_scoreboard(player_score, computer_score)
walkertools.print_blank_lines(3)


def get_player_choice():
    VALID_CHOICES = ["rock", "paper", "scissors"]

    while True:
        choice = input("Choose: Rock, Paper, or Scissors: ").lower()
        if choice in VALID_CHOICES:
            return choice
        print(f"Sorry, {choice} is not a valid choice")


def get_computer_choice():
    VALID_CHOICES = ["rock", "paper", "scissors"]
    computer_choice = random.choice(VALID_CHOICES)
    print(f"The computer chose {computer_choice}.")
    return computer_choice


def play_round(p_score, c_score):
    # get choices
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
'''
All this needs to be rewritten to reflect the new data stucture needed for rpsls.
    # handle ties
    if player_choice == computer_choice:
        print("Tie game. No score.")
        input("\nPress enter to continue...")
        return p_score, c_score

    player_wins_round = False

    # determine winner
    if player_choice == "rock" and computer_choice == "scissors":
        player_wins_round = True
    elif player_choice == "paper" and computer_choice == "rock":
        player_wins_round = True
    elif player_choice == "scissors" and computer_choice == "paper":
        player_wins_round = True

    # update score
    if player_wins_round:
        print("You won this round!")
        p_score += 1
    else:
        print("Computer won this round!")
        c_score += 1
'''

    input("\nPress Enter to continue...")
    return p_score, c_score


# game loop, exits when win-condition met
while player_score < WINNING_SCORE and computer_score < WINNING_SCORE:
    player_score, computer_score = play_round(player_score, computer_score)
    walkertools.clear_screen()
    print_scoreboard(player_score, computer_score)
    walkertools.print_blank_lines(3)

# game loop over, setup and display final score
walkertools.clear_screen()

if player_score == WINNING_SCORE:
    final_message = "CONGRATULATIONS! YOU ARE THE CHAMPION!"
    char = "!"
else:
    final_message = "GAME OVER - THE MACHINES HAVE WON"
    char = "X"


print(walkertools.create_banner(final_message, char))
walkertools.print_blank_lines(2)
print_scoreboard(player_score, computer_score)

walkertools.print_blank_lines(2)
print("W\u00fcnderbar! Thanks for playing.".center(80))
walkertools.print_blank_lines(2)
