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
    total_guess = 0
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
        total_guess += num_guess
        if guess == answer:
            print("You got it right in ", num_guess, "guesses")
            game_over = True
        elif guess > answer:
            print("It's lower")
        else:
            print("It's higher")

    return num_guess


#the number of total games, total guesses, and best game, which had the fewest number of guess in trial
def game_stats(total_games):
    print("Overall results:")
    print("    total games   =", total_games)
#    print("    total guesses =", total_guess)



if __name__ == "__main__":
    gameOver = False
    games = 0
#    guess = 0
    while gameOver == False:
        play_games()
        games += 1
        choice = input("Do you want to play again?: ")
        if choice.lower().startswith('n'):
            gameOver = True

    game_stats(games)




# this is the first code I wrote
# def play():
#     MAX = randint(2,100)
#     num_guess = 1
#     total_num_game = 0
#  #   game_playing = True

#     print("I'm thinking of a number between 1 and", MAX ," ....")
#     answer = randint(1,MAX)
#     print(answer)
#     guess = int(input("Your guess? "))
#     while answer != guess:
#         num_guess += 1
#         if guess < answer:
#             print("It's higher")
#             guess = int(input("Your guess? "))
#         else:
#             print("It's lower")
#             guess = int(input("Your guess? "))
#     print("You got it right in", num_guess, "times.")

# def repeat():
#     total_num_game = 1
#     again = input("Do you want to play again? ")
#     if again.lower().startswith("y"):
#         print()
#         play()
#         repeat()
#         total_num_game += 1
#         print(total_num_game)
#     elif again.lower().startswith("n"):
#         print("Overall Results: \n total games = ", total_num_game)
#     else:
#         print("Don't understand")