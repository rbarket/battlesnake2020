import random
import json
import optimalFood
from moveScore import scoreMove

def chooseDir(data):
	"""Returns up down left or right based on best choice of movements

	Parameters:
	data (str): json of data returned from the game

	Returns:
	str:move to be done

	"""
	bodyParts = data['you']['body'] # list of my own body parts
	head = [bodyParts[0]['x'],bodyParts[0]['y']] # head of snake
	width = data['board']['width']
	height = data['board']['height']
	hp = data['you']['health']
	foods = data['board']['food']
	snakes = data['board']['snakes']
	
	# Turning dictionaries into lists	

	occupiedList = [] # List of spaces currently occupied
	for snake in snakes:
		snakeBody = snake['body'] # snakeBody = list of body parts for one snake
		for piece in snakeBody: # iterate through each body piece of that snake
			part = [piece['x'], piece['y']]
			occupiedList.append(part)

	foodList = []
	for food in foods:
		item = (food['x'], food['y'])
		foodList.append(item)

	#

	legalMoves = possibleMoves(occupiedList, width, height, head) # only moves that are possible
	bestMove = scoreMove(legalMoves, snakes, width, height)
	if (hp < 75):
		print('getting food')
		res = optimalFood.getFood(legalMoves, occupiedList, foodList, head)
	else:
		print('best move of rando choice')
		res = random.choice(bestMove)
	return res

def possibleMoves(occupied, width, height, head):
	"""Returns list of moves that are physically possible to do

	Parameters:
	occupied (list): occupied positions
	width (int): width of board
	height (int): height of board 
	head (list): xy pos of head e.g. [3,5]

	Returns:
	list: possible moves
	
	"""
	
	moves = {}
	if not (([head[0]-1,head[1]] in occupied) or (head[0]-1 < 0)) : # left is occupied OR left is out of bounds
		item = {'left': [head[0]-1,head[1]] }
		moves.update(item)
	if not (([head[0]+1,head[1]] in occupied) or (head[0]+1 > width-1)) : # right
		item = {'right': [head[0]+1,head[1]] }
		moves.update(item) 

	if not (([head[0],head[1]-1] in occupied) or (head[1]-1 < 0)) : # up
		item = {'up': [head[0],head[1]-1] }
		moves.update(item)

	if not (([head[0],head[1]+1] in occupied) or (head[1]+1 > height-1)) : # down
		item = {'down': [head[0],head[1]+1] }
		moves.update(item)

	return moves

