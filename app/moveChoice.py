import random
import json

import app.optimalFood as foodCode
from app.moveScore import scoreMove
import app.utility as util
import app.tailChase as tailChase

def action(data):
	"""Returns up down left or right based on best choice of movements

	Parameters:
	data (str): json of data returned from the game

	Returns:
	str:move to be done

	"""
	bodyParts = data['you']['body'] # list of my own body parts
	head = (bodyParts[0]['x'], bodyParts[0]['y']) # head of snake
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
	
	if (hp < 30):
		print('getting food')
		res = foodCode.getFood(legalMoves, occupiedList, foodList, head, width, height)
		
	else:
		# print('chasing tail')
		# # Currently has a defensive/non-agressive personality where we will always chase our tail by default
		# res = tailChase.myChase(legalMoves, tail)
		print('best move of random choice')
		bestMove = scoreMove(legalMoves, occupiedList, width, height)
		res = random.choice(bestMove)
	return res

