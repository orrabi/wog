import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 400
def screen_cleaner():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

