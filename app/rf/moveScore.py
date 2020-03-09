import operator
from utility import *

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
			scoreDict.update({'down': checkBubbleScore(coord, snakeList, width, height)})
		if (move == 'up'):
			scoreDict.update({'up': checkBubbleScore(coord, snakeList, width, height)})
		if (move == 'right'):
			scoreDict.update({'right': checkBubbleScore(coord, snakeList, width, height)})
		if (move == 'left'):
			scoreDict.update({'left': checkBubbleScore(coord, snakeList, width, height)})
	
	max_val = max(scoreDict.values())
	#WTF IS THE FUNCTION BELOW DOING LOL?
	bestMove = [k for k, v in scoreDict.items() if v == max_val] # Note: will return a list with only 1 item
	print('scoredict: {} and bestMove: {}'.format(scoreDict,bestMove))
	return bestMove


