import RockPaperScissors.game as rps

game = rps.Game()


def my_input():
    move = input("Your move here: ")
    return move


results = game.run(print_results=False, custom_input=my_input())

if results == "PW":
    print(f"The player chose {results.player_move} and the computer chose {results.computer_move}.")
    print("Player won!")

if results == "CW":
    print(f"The player chose {results.player_move} and the computer chose {results.computer_move}.")
    print("Computer won!")

if results == "T":
    print(f"The player chose {results.player_move} and the computer chose {results.computer_move}.")
    print("Tie!")

if results == "E":
    print("Invalid move")
    