# This function will return a random number
def generate_sequence(difficulty):
    import random
    list_a = []
    for x in range(difficulty) :
        list_a.append(random.randint(1,101))
    print(*list_a, sep=" ")
    import time
    time.sleep(0.7)
    from Utils import screen_cleaner
    screen_cleaner()
    return list_a

# This function will return numbers list from the user
def get_list_from_user(difficulty) :
    print ("After seeing the numbers enter the numbers you saw, each one separated with Enter.")
    list_b=[]
    for i in range(difficulty) :
        list_b.append(int(input(" : ")))
    return list_b

# This function compares between two lists and return ture or false
def is_list_equal(list_a, list_b):
    if list_a == list_b:
        return True
    else: return False

# This function run the MemoryGame and return True for wining and False for losing
def play(difficulty):
    if (is_list_equal(generate_sequence(difficulty), get_list_from_user(difficulty))) == True:
        return True
    else: return False





