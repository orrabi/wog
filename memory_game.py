import random
from time import sleep
from utils import screen_cleaner

def play(difficulty):
    generated_arr = generate_sequence(difficulty)
    user_arr = get_list_from_user(difficulty)
    is_true = is_list_equal(generated_arr, user_arr)
    if is_true:
        print("You won!! :)")
    else:
        print("You lost :(")
    return is_true

def generate_sequence(difficulty):
    arr = []
    for value in range(difficulty):
        arr.append(random.randint(1, 100))
    print(arr, flush=True)
    sleep(0.7)
    screen_cleaner()
    return arr
def get_list_from_user(difficulty):
    arr = []
    print(f'Please insert the {difficulty} numbers you saw between 1-100')
    for value in range(difficulty):
        is_number = True
        while is_number:
            user_input = input()
            if str.isdigit(user_input) and 0 < int(user_input) <= 100:
                arr.append(int(user_input))
                is_number = False
            else:
                print(f'You have entered an invalid value.. please insert {difficulty} numbers between 1-100 ')
    return arr


def is_list_equal(generated_arr, user_arr):
    for value in user_arr:
        if value not in generated_arr:
            return False
    return True


