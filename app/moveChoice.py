import random
import json

import app.optimalFood as foodCode

import app.utility as util

def action(data):
	"""Returns up down left or right based on best choice of movements

	Parameters:
	data (str): json of data returned from the game

	Returns:
	str:move to be done

	"""
	bodyParts = data['you']['body'] # list of my own body parts
	head = (bodyParts[0]['x'],bodyParts[0]['y']) # head of snake
	tail = (bodyParts[-1]['x'], bodyParts[-1]['y'])
	hp = data['you']['health']

	width = data['board']['width']
	height = data['board']['height']
	allFood = data['board']['food']
	allSnakes = data['board']['snakes']
	
	print("\n Turn number {}".format(data['turn']))

	# Turning dictionaries into lists	

	foodList = []
	for food in allFood:
		item = (food['x'], food['y'])
		foodList.append(item)


	occupiedList = [] # List of spaces currently occupied
	for snake in allSnakes:
		snakeBody = snake['body'] # snakeBody = list of body parts for one snake
		for piece in snakeBody: # iterate through each body piece of that snake
			part = (piece['x'], piece['y'])
			occupiedList.append(part)


	
	legalMoves = util.checkBubbleOutBound(head, occupiedList, width, height) # only moves that are possible
	
	if (hp < 101):
		print('getting food')
		res = foodCode.getFood(legalMoves, occupiedList, foodList, head, width, height)
		
	else:
		print('best move of random choice')
		bestMove = scoreMove(legalMoves, snakes, width, height)
		res = random.choice(bestMove)
	return res

# def possibleMoves(occupied, width, height, head):
# 	"""Returns list of moves that are physically possible to do

# 	Parameters:
# 	occupied (list): occupied positions
# 	width (int): width of board
# 	height (int): height of board 
# 	head (list): xy pos of head e.g. [3,5]

# 	Returns:
# 	list: possible moves
	
# 	"""
	
# 	moves = {}
# 	if not (( (head[0]-1,head[1]) in occupied) or (head[0]-1 < 0)) : # left is occupied OR left is out of bounds
# 		item = {'left': (head[0]-1,head[1]) }
# 		moves.update(item)
# 	if not (( (head[0]+1,head[1]) in occupied) or (head[0]+1 > width-1)) : # right
# 		item = {'right': (head[0]+1,head[1]) }
# 		moves.update(item) 

# 	if not (( (head[0],head[1]-1) in occupied) or (head[1]-1 < 0)) : # up
# 		item = {'up': (head[0],head[1]-1) }
# 		moves.update(item)

# 	if not (( (head[0],head[1]+1) in occupied) or (head[1]+1 > height-1)) : # down
# 		item = {'down': (head[0],head[1]+1) }
# 		moves.update(item)

# 	return moves
# def stratMoves(legalMoves, occupiedList, foodMove, head, tail, hp):
# 	# Will get food if hp is less than 75
# 	if (hp < 75):
#     	print('getting food')
# 		res = foodMove
# 	# Will chase its own tail if not hungry
# 	else:
# 		print('chasing tail')
# 		# Currently has a defensive/non-agressive personality
# 		# Where we will always chase our tail by default
# 		res = personality.myChase(head, tail, legalMoves)
# 	return res
