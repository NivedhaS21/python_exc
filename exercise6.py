'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare
them, print out a message of congratulations to the winner, and ask if the players want to start
a new game)
Remember the rules:
 Rock beats scissors
 Scissors beats paper
 Paper beats rock'''
while True:
    choice = input("Do wanna play a game of Rock-paper-scissor? Y/N\n")
    if choice == 'Y':
        player1=input("Player 1, Enter Your Choice:")
        player2 = input("Player 2, Enter Your Choice:")
        if player1 == player2:
            print("Its a tie!!!")
        elif player1 == "rock" and player2 == "scissor":
                print("player1 is winner")
        elif player1 == "rock" and player2 == "paper":
                print("player2 is winner")
        elif player1 == "scissor" and player2 == "rock":
                print("player2 is winner")
        elif player1 == "scissor" and player2 == "paper":
                print("player1 is winner")
        elif player1 == "paper" and player2 == "rock":
                print("player1 is winner")
        else:
                print("Run again to play")
                break;






