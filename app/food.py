def getFood(moves, foods, head):
	""" Decides closest food based on hypotenuse from head to food

	Parameters:
	moves (list): POSSIBLE moves
	foods (list): xy locations of food pieces e.g [3,5]
	head (list): xy location of head e.g [3,5]

	Returns:
	str: best move

	"""
	min = 100000 # smallest distance to food
	bestFood = [0,0] # best food to get
	for food in foods:
		xDist = abs(head[0] - food[0]) # x distance between head and food
		yDist = abs(head[1]- food[1]) # y distance between head and food
		hyp = sqrt(xdist^2 + ydist^2) #distance between head and food
		if (hyp < min):
			min = hyp 
			bestFood = food # current best food
	
	
	return None