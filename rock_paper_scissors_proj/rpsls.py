# import libraries, standard followed by personal
import random

import walkertools

# Global Constants
VALID_CHOICES = ("rock", "paper", "scissors")
CHOICE_MAP = {"rock": 0, "paper": 1, "scissors": 2}

RESULTS = (("tie", "lose", "win"), ("win", "tie", "lose"), ("lose", "win", "tie"))

GAME_RULES = (
    "In Rock Paper Scissors, two players simultaneously choose one of three symbols: "
    "Rock (beats Scissors), Paper (beats Rock), or Scissors (beats Paper). "
    "In this terminal version, you will play against the computer in a Best of Three match, "
    "meaning the first player to win two rounds is declared the overall victor. "
    "If both players choose the same symbol, the round is a draw and must be replayed "
    "until a winner for that round is determined."
)


# print scoreboard
def print_scoreboard(p_score, c_score):
    scoreboard_width = 36
    print("*" * scoreboard_width)
    print("Scoreboard".center(scoreboard_width))
    print(f"Player Score: {p_score} Computer Score: {c_score}".center(scoreboard_width))
    print("*" * scoreboard_width)


def get_player_choice():
    while True:
        choice = input("Choose: Rock, Paper, or Scissors: ").lower()
        if choice in VALID_CHOICES:
            return choice
        print(f"Sorry, {choice} is not a valid choice")


def get_computer_choice():
    computer_choice = random.choice(VALID_CHOICES)
    print(f"The computer chose {computer_choice}.")
    return computer_choice


def play_round():
    # get choices
    player_choice_str = get_player_choice()
    computer_choice_str = get_computer_choice()
    # convert to index
    player_choice_index = CHOICE_MAP[player_choice_str]
    computer_choice_index = CHOICE_MAP[computer_choice_str]
    # calculate results
    round_result = RESULTS[player_choice_index][computer_choice_index]
    return round_result


####################START OF PROGRAM#############################

# Set win conditions, starting score score
WINNING_SCORE = 3
player_score = 0
computer_score = 0

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

print_scoreboard(player_score, computer_score)
walkertools.print_blank_lines(3)


# Main game loop, exits when win-condition met
while player_score < WINNING_SCORE and computer_score < WINNING_SCORE:
    result = play_round()
    if result == "win":
        player_score += 1
    elif result == "lose":
        computer_score += 1
    walkertools.clear_screen()
    print_scoreboard(player_score, computer_score)

    # Show the result of the round and pause
    if result == "win":
        print("You won this round!")
    elif result == "lose":
        print("Computer won this round!")
    else:
        print("Round tied, no points awarded")

    walkertools.print_blank_lines(1)
    input("Press Enter to continue...")
# Game loop over, setup and display final score
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
