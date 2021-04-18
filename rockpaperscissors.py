import random

class Game:
	def __init__(self, rock="rock", paper="paper", scissors="scissors", exit="quit", win_move=None, defeat_move=None, computer_can_use_special_moves=False):
		self.rock = rock
		self.paper = paper
		self.scissors = scissors
		self.win_move = win_move
		self.defeat_move = defeat_move
		self.computer_can_use_special_moves = computer_can_use_special_moves
		self.options = [self.rock, self.paper, self.scissors, self.win_move, self.defeat_move]

	def run(self, print_results=True, print_error=True, input_message="What's your move? rock, paper or scissors: ", custom_input=None):
		def computer():
			if self.computer_can_use_special_moves == False:
				move = random.choice(self.options)
				while move != self.win_move and move != self.deafeat_move:
					move = random.choice(self.options)
			elif self.computer_can_use_special_moves == True:
				if self.win_move == None or self.defeat_move == None:
					move = random.choice(self.options)
					while move != self.win_move and move != self.defeat_move:
						move = random.choice(self.options)
				else:
					move = random.choice(self.options)
			return move

		def player():
			if custom_input == None:
				move = input(input_message)
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

		if player_move == computer_move:
			tie = True

		elif player_move == self.rock:
			if computer_move == self.scissors:
				player_won = True
			elif computer_move == self.win_move:
				computer_won = True
			else:
				computer_won = True

		elif player_move == self.paper:
			if computer_move == self.rock:
				player_won = True
			elif computer_move == self.win_move:
				computer_won = True
			else:
				computer_won = True

		elif player_move == self.scissors:
			if computer_move == self.paper:
				player_won = True
			elif computer_move == self.win_move:
				computer_won = True
			else:
				computer_won = True

		elif player_move == self.win_move:
			player_won = True

		elif player_move == self.defeat_move:
			computer_won = True

		else:
			error = True

		if print_results == True and player_won = True:
			print()
