from guess_game import play as play_guess_game
from memory_game import play as play_memory_game
from currency_roulette_game import play as play_currency_game
from utils import screen_cleaner
from score import add_score
def welcome():
    player_name = input("Please insert your name here: ")
    print(f'Hi {player_name} and welcome to the World of Games: The Epic Journey')
def start_play():
    game_list = ["Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.",
                 "Guess Game - guess a number and see if you chose like the computer.",
                 "Currency Roulette - try and guess the value of a random amount of USD in ILS."]
    is_number = True
    while is_number:
        print("Please choose a game to play:")
        for game in game_list:
            print(f'{game_list.index(game) + 1}. {game}')
        game_chosen = input("")
        if str.isdigit(game_chosen) and int(game_chosen) > 0 and int(game_chosen) <= len(game_list):
            is_number = False
            game_chosen = int(game_chosen)
        else:
            print("Please try again..")
    is_number = True
    is_winner = ""
    while is_number:
        difficulty_level = input("Please choose game difficulty between 1 and 5: ")
        if str.isdigit(difficulty_level) and int(difficulty_level) > 0 and int(difficulty_level) <= 5:
            is_number = False
            difficulty_level = int(difficulty_level)
        else:
            print("Please try again..")
    if game_chosen == 1:
        is_winner = play_memory_game(difficulty_level)
    elif game_chosen == 2:
        is_winner = play_guess_game(difficulty_level)
    elif game_chosen == 3:
        is_winner = play_currency_game(difficulty_level)

    print(f'did You win?? {is_winner}')
    if is_winner:
        add_score(difficulty_level)

    play_again = input("Do you want to play another game? yes/no: ")
    is_true = True
    while is_true:
        if play_again == "yes":
            is_true = False
            screen_cleaner()
            start_play()
        elif play_again == "no":
            is_true = False
            print("Thank you for playing!")
        else:
            play_again = input("Please choose 'yes' or 'no': ")





