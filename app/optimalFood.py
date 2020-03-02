from math import sqrt
def getFood(moves, foods, head):
	""" Decides closest food based on hypotenuse from head to food

	Parameters:
	moves (dict): POSSIBLE moves e.g {left: [3,5], up: [4,6]}
	foods (list): xy locations of food pieces e.g [3,5]
	head (list): xy location of head e.g [3,5]

	Returns:
	str: best move

	"""
	minimum = 100000 # smallest distance from head to food
	bestFood = [0,0] # best food to get
	for food in foods:
		xDist = abs(head[0] - food[0]) # x distance between head and food
		yDist = abs(head[1]- food[1]) # y distance between head and food
		hyp = sqrt(xDist**2 + yDist**2) #distance between head and food
		if (hyp < minimum):
			minimum = hyp 
			bestFood = food # current best food


	mini = 100000 # smallest distance from move to food
	bestMove ='up' # arbitrary for initialization
	for move, coord in moves.items(): # e.g move: 'left' and coord: [3,5]
		xDist = abs(coord[0] - bestFood[0]) # x distance between move and food
		yDist = abs(coord[1]- bestFood[1]) # y distance between move and food
		hyp = sqrt(xDist**2 + yDist**2) #distance between move and food

		# print('move: {}, coord: {}, xDist:{}, yDist:{}, hypotenuse:{}, food:{}'.format(move, coord, xDist, yDist, hyp, food))
		if (hyp < mini):
			mini = hyp
			bestMove = move

	return bestMove