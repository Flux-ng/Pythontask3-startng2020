import random
##Easy guess, user guess the ultimate number randomly from numbers between 1 - 10
play = True
while play:
    easy = random.randint(1, 10)
    ultimate_number = 7
    guess_limit = 6
    guess_count = 0
    ## Get to know user for flow of interaction between the computer and the player
    user_name = input(" Hello dear, what is your name: ")
    ## Is able to choose/select different level of game to play here
    game_level = input(user_name + "," " please set your game level. Enter 'E' for Easy; 'M' for Medium; 'H' for Hard: ").upper()
    ## Easy game level
    if game_level == "E":
        print("Guess for a number between 1 - 10")
        print("You are to make the right guess within: " + str(guess_limit) + " guesses ")
        guess_left = guess_limit
        while guess_count < guess_limit:
            try:
                ## Guess panel to accept input from user
                guess = int(input(" Make a Guess: "))
                guess_count += 1
                if guess != ultimate_number:
                    print('"That was wrong!"')
                    ## Guess left after every succesive guess(es)
                    guess_left -= 1
                    print("You have: " + str(guess_left) + " Guess(s) " + " left ")
                elif guess == ultimate_number:
                    print('"You got it right!"')
                    break
            ## Except Prompt
            except ValueError:
                print("Invalid input")
                print("Try again")
                continue
        else:
            print("Game Over!!!")

    medium = random.randint(1, 20)
    ultimate_number = 15
    guess_limit = 4
    guess_count = 0
    ##Medium game level
    if game_level == "M":
        guess_left = guess_limit
        print(user_name + "," " guess for a number between 1 - 20")
        ## Number of Guess (es) allow per session
        print("You are to make the right guess within " + str(guess_limit) + " guesses ")
        while guess_count < guess_limit:
            try:
                ## Guess input panel
                guess = int(input("Make a Guess: "))
                guess_count += 1
                if guess != ultimate_number:
                    print('"That was wrong')
                    ## Guess left after every successive gues
                    guess_left -= 1
                    print("You have: " + str(guess_left) + " Guess(s) " + " left ")
                elif guess == ultimate_number:
                    print('"You got it right"')
                    break
            ## Except prompt
            except ValueError:
                print("Invalid input")
                print("Try again")
                continue
        else:
            print("Game Over!!!")


    hard = random.randint(1, 50)
    ultimate_number = 35
    guess_limit = 3
    guess_count = 0
## Hard game level
    if game_level == "H":
        print(user_name + "," " guess for a number between 1 - 50")
        print("You are to make the right guess within: " + str(guess_limit) + " guesses ")
        guess_left = guess_limit
        while guess_count < guess_limit:
            try:
                guess = int(input("Make a Guess: "))
                guess_count += 1
                if guess != ultimate_number:
                    print('"That was wrong')
## Guess left after every successive guess
                    guess_left -= 1
                    print("You have: " + str(guess_left) + " Guess(s) " + " left ")
                elif guess == ultimate_number:
                    print('"You got it right"')
                    break
## Except prompt
            except ValueError:
                print("Invalid input")
                print("Try again")
                continue
        else:
            print("Game Over!!!")
## Replay prompt
    play_again = (input("Do you to play again? Enter Yes/No ")).lower()
    if play_again == "no":
        play = False
    else:
        continue







