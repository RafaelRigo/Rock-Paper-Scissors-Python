import rockpaperscissors as rps

game = rps.Game(rock="rock", paper="plastic", scissors="knife", exit="q", win_move="win", defeat_move="lose", computer_can_use_special_moves=True)
game.run(print_results=True, input_message="What's your move? ")
