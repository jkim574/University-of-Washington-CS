from random import *

# I'm thinking of a number between 1 and 100...
# Your guess? 50
# It's lower.
# Your guess? 25
# It's lower.
# Your guess? 10
# It's lower.
# Your guess? 5
# It's higher.
# Your guess? 7
# You got it right in 5 guesses
# Do you want to play again? y

# Overall results:
#   total games   = 3
#   total guesses = 19
#   guesses/game  = 6.33
#   best game     = 5


def play_games():
    MAX = randint(2,100)
    print("")
    print("I'm thinking of a number between 1 and ", MAX, "...")
    answer = randint(1,MAX)
    #the real number
    print(answer)
    num_guess = 0
    game_over = False

    while(game_over == False):
        guess = int(input("Your guess? "))
        num_guess += 1
        if guess == answer:
            print("You got it right in ", num_guess, "guesses")
            game_over = True
        elif guess > answer:
            print("It's lower")
        else:
            print("It's higher")

    return num_guess


def game_stats(total_games, total_num_guess, best_game_number):
    """The number of total games, total guesses, and best game, which had the
    fewest number of guess in trial.

    Note: Best game number starts from 0.
    """
    print("Overall results:")
    print("    total games   =", total_games)
    print("    total guesses =", total_num_guess)
    print("    guesses/game  =", total_num_guess / total_games)
    print("    Best game     =", best_game_number + 1)


if __name__ == "__main__":
    gameOver = False
    games = 0
    guess = 0
    total_guess = 0


  # Maintaine a list of number of guesses for each game
    num_guesses = []
    while gameOver == False:
        guess = play_games()
        total_guess += guess
        #add number of guesses to the list
        num_guesses.append(guess)

        games += 1
        choice = input("Do you want to play again?: ")
        if choice.lower().startswith('n'):
            gameOver = True

    # Find minimum number of guesses
    min_guesses = min(num_guesses)
 #   print(type(num_guesses))
    # Find the index of min_guesses from the list
    min_index = num_guesses.index(min_guesses)

    game_stats(games, total_guess, min_index)




# # Introduction to the Guess Game
# def game_intro():
#    print("This program allows you to play a guessing game.");
#    print("I will think of a number between 1 and");
#    print("100 and will allow you to guess until");
#    print("you get it.  For each guess, I will tell you");
#    print("whether the right answer is higher or lower");
#    print("than your guess.");

# # Plays one game of the Guessing game and returns the amount of guesses
# # the player took to win.
# def guessing_game():
#    answer = randrange(1, 100);  # randrange operates faster than randint
#    guess = int(input("Your guess? "));
#    guess_count = 1;
#    while guess != answer:
#       guess = int(input("Your guess? "));
#       guess_count += 1;
#    return guess_count;

# def main():
#    game_intro();
#    # Counters
#    total_games = 0;
#    total_guesses = 0;
#    best_game = 0;
#    least_guessed = 101;
#    continue_playing = "y";
#    while continue_playing.startswith("y", 0, len(continue_playing)):
#       guess_counter = guessing_game();
#       # end of game phase
#       total_games += 1;                   # increments total games
#       total_guesses += guess_counter;     # increments guesses per game
#       if guess_counter < least_guessed:   # checks for best game
#          least_guessed = guess_counter;
#          best_game = total_games;
#       continue_playing = input("Do you want to play again? ").lower();
#    guesses_per_game = float(total_guesses) / total_games;
#    # Display Information
#    print("Overall results:");
#    print("     total games   = %d" % total_games);
#    print("     total guesses = %d" % total_guesses);
#    print("     guesses/game  = %.1f" % guesses_per_game);
#    print("     best game     = %d" % best_game);

# if __name__ == "__main__":
#     main();
