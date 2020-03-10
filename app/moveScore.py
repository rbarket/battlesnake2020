import operator

def scoreMove(moves, snakes, width, height):

	snakeList = []
	for snake in snakes:
		snakeBody = snake['body'] # snakeBody = list of body parts for one snake
		for piece in snakeBody: # iterae through each body piece of that snake
			part = [piece['x'], piece['y']]
			snakeList.append(part)

	scoreDict = {}

	for move, coord in moves.items(): 
		if (move == 'down'):
			scoreDict.update({'down': check(coord, snakeList, width, height)})
		if (move == 'up'):
			scoreDict.update({'up': check(coord, snakeList, width, height)})
		if (move == 'right'):
			scoreDict.update({'right': check(coord, snakeList, width, height)})
		if (move == 'left'):
			scoreDict.update({'left': check(coord, snakeList, width, height)})

	max_val = max(scoreDict.values())
	bestMove = [k for k, v in scoreDict.items() if v == max_val] # Note: will return a list with only 1 item
	print('scoredict: {} and bestMove: {}'.format(scoreDict,bestMove))
	return bestMove


def check(move, occupied, width, height):
	"""
	_Purpose:
	takes a move coord and returns a score (max 4) based on how many free spaces are directly around the move

	_Parameters:
	move (list): xy coord of the move
	occupied (list): xy coords all occupied spaces on board 
	width (int): width of board
	height (int): height of board

	_Returns:
	score (int): score of move
	"""

	def coordMaker(coord):
		"""
		_Purpose:
		makes up down left right coordinates of the current coordinated passed to it
		"""

		up = (coord[0], coord[1]-1)
		down = (coord[0], coord[1]+1)
		left = (coord[0]-1, coord[1])
		right = (coord[0]-1, coord[1])
		spots = [coord, up, down, left, right]
		return spots

	score = 0
	for pos in coordMaker(move):		
		if not (([pos[0]-1,pos[1]] in occupied) or (pos[0]-1 < 0)): #left
			score += 1
		if not (([pos[0]+1,pos[1]] in occupied) or (pos[0]+1 > width-1)): # right
			score += 1
		if not (([pos[0],pos[1]-1] in occupied) or (pos[1]-1 < 0)): # up
			score += 1
		if not (([pos[0],pos[1]+1] in occupied) or (pos[1]+1 > height-1)): #down
			score += 1
	return score


