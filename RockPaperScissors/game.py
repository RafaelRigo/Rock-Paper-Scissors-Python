import random
import sys

class Game:
	def __init__(self, rock="rock", paper="paper", scissors="scissors", exit="quit"):
		self.rock = rock
		self.paper = paper
		self.scissors = scissors
		self.exit = exit
		# self.win_move = win_move
		# self.defeat_move = defeat_move
		# self.special_moves_for_computer = special_moves_for_computer
		self.options = [self.rock, self.paper, self.scissors]

	def run(self, print_results=True, custom_input=None):
		def computer():
			# if self.special_moves_for_computer == False:
			# 	move = random.choice(self.options)
			# 	while move != self.win_move and move != self.defeat_move:
			# 		move = random.choice(self.options)
			# elif self.special_moves_for_computer == True:
			# 	if self.win_move == None or self.defeat_move == None:
			# 		move = random.choice(self.options)
			# 		while move != self.win_move and move != self.defeat_move:
			# 			move = random.choice(self.options)
			# 	else:
			# 		move = random.choice(self.options)
			move = random.choice(self.options)
			return move

		def player():
			if custom_input == None:
				move = input("What's your move? rock, paper or scissors: ")
			else:
				move = custom_input
			return move

		player_move = player()
		computer_move = computer()
		player_won = False
		computer_won = False
		tie = False
		error = False
		player_move = player_move.lower()

		if player_move == self.exit:
			sys.exit(0)

		elif player_move == computer_move:
			tie = True

		elif player_move == self.rock:
			if computer_move == self.scissors:
				player_won = True
			# elif computer_move == self.win_move:
			# 	computer_won = True
			# else:
			# 	computer_won = True

		elif player_move == self.paper:
			if computer_move == self.rock:
				player_won = True
			# elif computer_move == self.win_move:
			# 	computer_won = True
			# else:
			# 	computer_won = True

		elif player_move == self.scissors:
			if computer_move == self.paper:
				player_won = True
			# elif computer_move == self.win_move:
			# 	computer_won = True
			# else:
			# 	computer_won = True

		# elif player_move == self.win_move:
		# 	player_won = True

		# elif player_move == self.defeat_move:
		# 	computer_won = True

		else:
			error = True

		if print_results:
			if player_won:
				print(f"You chose {player_move} and the computer chose {computer_move}.")
				print("You won!")
				return "PW"
			elif computer_won:
				print(f"You chose {player_move} and the computer chose {computer_move}.")
				print("The computer won…")
				return "CW"
			elif tie:
				print(f"You chose {player_move} and the computer chose {computer_move}.")
				print("It's a tie!")
				return "T"
			elif error:
				print("\"{}\"? That isn't a valid move!".format(player_move))
				return "E"
		
		else:
			if player_won:
				return "PW"
			elif computer_won:
				return "CW"
			elif tie:
				return "T"
			elif error:
				return "E"
