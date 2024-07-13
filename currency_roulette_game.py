import requests
import random

def play(difficulty):
    random_dollar, interval_arr = get_money_interval(difficulty)
    user_guess = get_guess_from_user(random_dollar)
    is_true = compare_results(user_guess, interval_arr)
    if is_true:
        print("You won! :)")
        return is_true
    else:
        print("You lost :(")
        return is_true

def get_money_interval(difficulty):
    random_dollar = random.randint(1, 100)
    base = 10
    interval = base - difficulty

    url = "https://openexchangerates.org/api/latest.json?app_id="
    api_key = "854fb793dd8f41ab993366ef1ded8390"
    full_url = url + api_key
    resp = requests.get(full_url)
    if resp.ok:
        data = resp.json()
        rate = data["rates"]["ILS"]
        interval_arr = [round((random_dollar * rate) - interval, 2), round((random_dollar * rate) + interval, 2)]
        return random_dollar, interval_arr
    else:
        interval_arr = [round((random_dollar * 3.72) - interval, 2), round((random_dollar * 3.72) + interval, 2)]
        return random_dollar, interval_arr


def get_guess_from_user(random_dollar):
    is_number = True
    while is_number:
        user_guess = input(f'Please guess how much money in ₪ is {random_dollar}$: ')
        if str.isdigit(user_guess) and int(user_guess) != 0:
            return int(user_guess)
        else:
            print("Please try again..")

def compare_results(user_guess, interval_arr):
    if interval_arr[0] <= user_guess <= interval_arr[1]:
        return True
    else:
        return False