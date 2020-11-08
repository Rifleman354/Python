import random

prompt = "Rock, paper, scissors! Choose R for rock, P for paper, and S for scissors (Q to Quit): \n"
#Prompts the user to input 3 letters
RPS = ['Rock', 'Paper', 'Scissors'] # A list containing the options for the random generator opponent
outcome = [" Lose!", " Tie!", " Win!"] # The outcome of the player
while True:
    opp_choose = random.choice(RPS) # The actual random generator
    user_input = input(prompt) # A variable that contains the player's input
    if user_input.upper() == "Q": # Allows the player to press "q" to quit the loop
        print("You have quit the game! \n")
        break
    elif user_input.upper() == "R":
        # The nested conditional statements that determines if the player wins or looses
        if opp_choose == 'Paper':
            V = 0
        if opp_choose == 'Scissors':
            V = 2
        if opp_choose == 'Rock':
            V = 1
    elif user_input.upper() == "P":
        if opp_choose == 'Paper':
            V = 1
        if opp_choose == 'Scissors':
            V = 0
        if opp_choose == 'Rock':
            V = 2
    elif user_input.upper() == "S":
        if opp_choose == 'Paper':
            V = 0
        if opp_choose == 'Scissors':
            V = 2
        if opp_choose == 'Rock':
            V = 1
    else:
        print("You need to choose a valid letter!")
        continue
        # If the player doesn't choose r, p, s, or q, this prompts the player and resets the program
    result = "You" + outcome[V]
    print(result) # Prompts the player the result