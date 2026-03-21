# import libraries, standard followed by personal
import os
import random


# Utility Functions
def create_banner(text: str, char: str = "#"):
    """
    Wraps text in a decorative border for terminal output.

    Args:
        text: The string to be highlighted.
        char: The character used for the border (default is '#').

    Returns:
        A formatted string representing the banner.
    """
    line_length = len(text) + 2
    border = char * line_length

    return f"{border}\n {text}\n{border}"


def print_blank_lines(num_of_lines):
    print("\n" * num_of_lines, end="")


# request and validate a single input
def ask_for(data_type, prompt, low, high):
    while True:
        try:
            x = data_type(input(prompt))
            if x < low or x > high:
                print(f"Must print a value between {low} and {high}")
            else:
                return x
        except ValueError:
            print("Invalid value, try again")


def clear_screen():
    """
    Clears the terminal screen based on the operating system.
    """
    # 'nt' is the internal name for Windows.
    # Otherwise, we assume it's a POSIX system (Linux/Mac).
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# print scoreboard
def print_scoreboard(p_score, c_score):
    scoreboard_width = 36
    print("*" * scoreboard_width)
    print("Scoreboard".center(scoreboard_width))
    print(f"Player Score: {p_score} Computer Score: {c_score}".center(scoreboard_width))
    print("*" * scoreboard_width)


# Game Functions


def get_player_choice():
    while True:
        choice = input("Choose: Rock, Paper, Scissors, Lizard, or Spock: ").lower()
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
    return round_result, player_choice_str, computer_choice_str


# Global Constants
WINNING_SCORE = 3

VALID_CHOICES = ("rock", "paper", "scissors", "lizard", "spock")
CHOICE_MAP = {"rock": 0, "paper": 1, "scissors": 2, "lizard": 3, "spock": 4}

RESULTS = (
    # Rock    Paper  Sciss.  Lizard  Spock
    ("tie", "lose", "win", "win", "lose"),  # Rock
    ("win", "tie", "lose", "lose", "win"),  # Paper
    ("lose", "win", "tie", "win", "lose"),  # Scissors
    ("lose", "win", "lose", "tie", "win"),  # Lizard
    ("win", "lose", "win", "lose", "tie"),  # Spock
)

GAME_RULES = """The game follows a circular logic where each of the five symbols 
    defeats two others and loses to two others. Scissors cuts Paper and 
    decapitates Lizard; Paper covers Rock and disproves Spock; Rock crushes 
    Lizard and Scissors; Lizard poisons Spock and eats Paper; and Spock 
    vaporizes Rock and smashes Scissors. If both players choose the same 
    symbol, the round is a draw. No points are awarded for a draw and 
    the round will be replayed until a win."""

# Set/reset starting score
player_score = 0
computer_score = 0

#################### START OF PROGRAM #############################

print(create_banner("Rock! Paper! Scissors! Lizard! Spock!", "*"))
print_blank_lines(2)
wants_rules = input("Do you need a refresher on the rules? Yes/No: ").lower().strip()

if wants_rules.startswith("y"):
    print_blank_lines(2)
    print(GAME_RULES)
    print_blank_lines(2)

print("Well then, let's begin")
input("Press Enter to continue...")
clear_screen()


# Meta game loop - allows players to continue playing
while True:
    # reset after last game
    clear_screen()
    player_score = 0
    computer_score = 0
    print_scoreboard(player_score, computer_score)
    print_blank_lines(3)

    # Main game loop, exits when win-condition met
    while player_score < WINNING_SCORE and computer_score < WINNING_SCORE:
        result, player_choice, computer_choice = play_round()
        if result == "win":
            player_score += 1
        elif result == "lose":
            computer_score += 1
        clear_screen()
        print_scoreboard(player_score, computer_score)
        # Show game choices
        print(f"Computer chose: {computer_choice.capitalize()}")
        print(f"You chose: {player_choice.capitalize()}")

        # Show the result of the round and pause
        if result == "win":
            print("You won this round!")
        elif result == "lose":
            print("Computer won this round!")
        else:
            print("Round tied, no points awarded")

        print_blank_lines(1)
        input("Press Enter to continue...")
    # Game loop over, setup and display final score
    clear_screen()

    if player_score == WINNING_SCORE:
        final_message = "CONGRATULATIONS! YOU ARE THE CHAMPION!"
        char = "!"
    else:
        final_message = "GAME OVER - THE MACHINES HAVE WON"
        char = "X"

    print(create_banner(final_message, char))
    print_blank_lines(2)
    print_scoreboard(player_score, computer_score)

    print_blank_lines(1)
    keep_going = input("Would you like to play again? Yes/No: ").lower().strip()
    if keep_going.startswith("n"):
        clear_screen()
        print_blank_lines(3)
        print("W\u00fcnderbar! Thanks for playing.".center(80))
        print_blank_lines(3)
        break
