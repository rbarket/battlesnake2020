import random
import json

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
	
	
	# Turning dictionaries into lists	

	occupiedList = [] # List of spaces currently occupied
	for bodyPart in bodyParts:
		item = [bodyPart['x'], bodyPart['y']]
		occupiedList.append(item)

	foodList = []
	for food in foods:
		item = [food['x'], food['y']]
		foodList.append(item)

	#

	legalMoves = possibleMoves(occupiedList, width, height, head) # only moves that are possible
	
	# if hp < 50:
	# 	getFood(legalMoves, foodList, head)
	print(width)
	print(height)
	print(legalMoves)
	res = random.choice(list(legalMoves.keys()))
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

