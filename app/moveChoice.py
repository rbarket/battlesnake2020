import random
import json
# <<<<<<< HEAD
import app.optimalFood
from app.moveScore import scoreMove
# =======
# import optimalFood
# import tailChase
# from moveScore import scoreMove
# >>>>>>> 17df5e2ef968ac0064231ff335d4628d00c1a883

def chooseDir(data):
	"""Returns up down left or right based on best choice of movements

	Parameters:
	data (str): json of data returned from the game

	Returns:
	str:move to be done

	"""
	bodyParts = data['you']['body'] # list of my own body parts
	head = (bodyParts[0]['x'],bodyParts[0]['y']) # head of snake
	tail = (bodyParts[-1]['x'], bodyParts[-1]['y'])
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
			part = (piece['x'], piece['y'])
			occupiedList.append(part)

	foodList = []
	for food in foods:
		item = (food['x'], food['y'])
		foodList.append(item)

	#

	legalMoves = possibleMoves(occupiedList, width, height, head) # only moves that are possible
	bestMove = scoreMove(legalMoves, snakes, width, height)
	if (hp < 50):
		print('getting food')
		res = optimalFood.getFood(legalMoves, occupiedList, foodList, head, width, height)
	else:
# <<<<<<< HEAD
		print('best move of random choice')
		res = random.choice(bestMove)
# =======
# 		print('chasing tail')
# 		res = tailChase.action(legalMoves, occupiedList, head, tail, width, height, hp)
# >>>>>>> 17df5e2ef968ac0064231ff335d4628d00c1a883
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
	if not (( (head[0]-1,head[1]) in occupied) or (head[0]-1 < 0)) : # left is occupied OR left is out of bounds
		item = {'left': [head[0]-1,head[1]] }
		moves.update(item)
	if not (( (head[0]+1,head[1]) in occupied) or (head[0]+1 > width-1)) : # right
		item = {'right': [head[0]+1,head[1]] }
		moves.update(item) 

	if not (( (head[0],head[1]-1) in occupied) or (head[1]-1 < 0)) : # up
		item = {'up': [head[0],head[1]-1] }
		moves.update(item)

	if not (( (head[0],head[1]+1) in occupied) or (head[1]+1 > height-1)) : # down
		item = {'down': [head[0],head[1]+1] }
		moves.update(item)

	return moves

