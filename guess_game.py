import random


def play(difficulty):
    secret_number = generate_numbers(difficulty)
    user_num = get_guess_from_user(difficulty)
    is_true = compare_results(secret_number, user_num)
    if is_true:
        print("You Won!! :)")
    else:
        print("You Lost :(")
    return is_true
    # return compare_results(secret_number, user_num)


def generate_numbers(difficulty):
    secret_number = random.randint(0, difficulty)
    # print(secret_number)
    return secret_number


def get_guess_from_user(difficulty):
    is_number = True
    while is_number:
        print("Please choose a number from the following options: ", end="")
        for num in range(difficulty):
            print(num, end=", ")
        user_random_number = input("- ")
        if str.isdigit(user_random_number) and 0 <= int(user_random_number) <= difficulty:
            return int(user_random_number)
        else:
            print("Please try again..")


def compare_results(generated_number, user_number):
    if generated_number == user_number:
        return True
    else:
        return False
