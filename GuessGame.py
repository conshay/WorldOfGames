# This function will return a random number
def generate_number(difficulty):
    import random
    return random.randint(1,difficulty)

# This function will get and return guss from the user
def get_guess_from_user(difficulty):
    return input("please guess number from 1 to {} : " .format(difficulty))

# This function compares between the user number and the random number, and return True/False
def compare_results(difficulty, secret_number):
    if int(get_guess_from_user(int(difficulty))) == int((secret_number))  :
        return True
    else: return False

# This function run the GuessGame and return True for wining, or False for losing
def play(difficulty):
    difficulty=int(difficulty)
    if (compare_results(int(difficulty),generate_number(int(difficulty)))) == True :
        return True
    else:return False






