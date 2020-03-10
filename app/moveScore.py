import operator

def scoreMove(moves, snakes, width, height):

	snakeList = []
	for snake in snakes:
		snakeBody = snake['body'] # snakeBody = list of body parts for one snake
		for piece in snakeBody: # iterae through each body piece of that snake
			part = (piece['x'], piece['y'])
			snakeList.append(part)

	scoreDict = {}

	for move, coord in moves.items(): 
		if (move == 'down'):
			scoreDict.update({'down': check(coord, snakeList, width, height, n=2)})
		if (move == 'up'):
			scoreDict.update({'up': check(coord, snakeList, width, height, n=2)})
		if (move == 'right'):
			scoreDict.update({'right': check(coord, snakeList, width, height, n=2)})
		if (move == 'left'):
			scoreDict.update({'left': check(coord, snakeList, width, height, n=2)})

	max_val = max(scoreDict.values())
	bestMove = [k for k, v in scoreDict.items() if v == max_val] # Note: will return a list with only 1 item
	print('scoredict: {} and bestMove: {}'.format(scoreDict,bestMove))
	return bestMove


def check(move, occupied, width, height, n=1):
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


	if (n==0): # base case
		return 0	

	up = (move[0], move[1]-1)
	down = (move[0], move[1]+1)
	left = (move[0]-1, move[1])
	right = (move[0]+1, move[1])

	score = 0

	# for pos in coordMaker(move):


	if not (( left in occupied) or (left[0] < 0)): #left
		score += 1 + check(left, occupied, width, height, n-1)
	if not (( right in occupied) or (right[0] > width-1)): # right
		score += 1 + check(right, occupied, width, height, n-1)
	if not (( up in occupied) or (up[1] < 0)): # up
		score += 1 + check(up, occupied, width, height, n-1)
	if not (( down in occupied) or (down[1] > height-1)): #down
		score += 1 + check(down, occupied, width, height, n-1)
	return score


