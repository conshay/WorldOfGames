# This function printing welcome message for the user
def welcome(name):
    return "Hello {} and welcome to the World of Games (WoG).Here you can find many cool games to play.".format(name)

# This function loading game
def load_game():
    import Utils
    import MemoryGame
    import GuessGame
    import Score
    print("Please choose a game to play: \n 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n 2. Guess Game - guess a number and see if you chose like the computer")
    choosegame = input()
    print("Please choose game difficulty from 1 to 5 :")
    if (choosegame > "2") or (choosegame < "1"):
        print(Utils.ERROR_MESSAGE), load_game()
    choosegame = int(choosegame)
    difficulty = input()
    if (difficulty > "5") or (difficulty < "1"):
        print(Utils.ERROR_MESSAGE), load_game()
    difficulty = int(difficulty)
    if  choosegame == 1  :
        if MemoryGame.play(difficulty) == True :
            Score.add_score(difficulty)
        else :
            load_game()
    elif choosegame == 2 :
        if  GuessGame.play(difficulty) == True :
            Score.add_score(difficulty)
        else :
            load_game()
