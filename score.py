from utils import SCORES_FILE_NAME
import os


def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5
    if not os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, "w") as file:
            file.write('0')

    if os.stat(SCORES_FILE_NAME).st_size == 0:
        with open(SCORES_FILE_NAME, "w") as file:
            file.write('0')

    with open(SCORES_FILE_NAME, "r") as file:
        current_score = file.read().strip()

    final_score = int(current_score) + POINTS_OF_WINNING
    with open(SCORES_FILE_NAME, "w") as file:
        file.write(str(final_score))
