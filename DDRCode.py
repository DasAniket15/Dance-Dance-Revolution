from dance_dance_revolution import DanceDanceRevolution

GAME = DanceDanceRevolution()


def get_game_parameters():
    """
    Takes input of amount of steps user has to memorize, and also
    take input of speed at which the steps that the usesr will have
    memorize will appear on screen.
    """

    #Defining list to convert into tuple later
    game_parameters = []

    #Defining variables for infinite while loops
    i = j = 0

    #Taking input for steps
    while i < 1:
        amt_steps = int(input("How many steps would you like to memorize? (positive non-zero integers only) "))

        if amt_steps <= 0:
            print ("WARNING: Please enter a positive no-zero integer value.")

        else:
            game_parameters.append(amt_steps)
            i = 1

    #Taking input for speed of game
    while j < 1:
        speed_steps = float(input("How fast would you like the game to run? (positive non-zero numerical values only) "))

        if speed_steps <= 0:
            print ("WARNING Pleaes enter a positive non-zero numerical value.")

        else:
            game_parameters.append(speed_steps)
            j = 1

    #Converting list into tuple
    game_parameters = tuple(game_parameters)

    return game_parameters


def get_user_answers():
    """
    Prompts user to enter U, D, L, R and continue until user enters DONE
    and store all the controls in a list.
    """

    #Defining list of inputs
    list_ctrl_inputs = []

    #Defining variables for infinite while loop
    i = 0

    #Taking inputs of directions from user
    while i < 1:
        ctrl_inputs = input("Enter a direction (U/D/L/R) or 'DONE' to finish: ")

        if ctrl_inputs == "DONE" and len(list_ctrl_inputs) == 0:
            print ("Please enter at least one answer before selecting 'DONE'.")

        elif ctrl_inputs == "DONE" and len(list_ctrl_inputs) > 0:
            i = 1

        else:
            list_ctrl_inputs.append(ctrl_inputs)

    return list_ctrl_inputs


def run_game():
    """
    Runs the game.
    """
    
    #Storing returned value of game parameters function in a variable
    game_parameters = get_game_parameters()

    #Storing values in GAME methods to set amount of steps and speed of the game
    GAME.set_amount(game_parameters[0])
    GAME.set_speed(game_parameters[1])

    #Play sequence according to the values assigned by game parameters
    GAME.play_sequence()

    #Store returned value of user answers function in a variable
    user_answers = get_user_answers()

    #Checking if user's answers match the game and returns statements accordingly
    check_answer = GAME.check_answers(user_answers)
    if check_answer == True:
        return ("Congratulations! You've guessed correctly!")

    else:
        return ("Sorry, but you seem to be wrong!")


def main():
    game = run_game()

    print (game)


main()