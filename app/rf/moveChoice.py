import random
import json
# <<<<<<<<< HEAD
import rf.optimalFood as bestFood
import rf.utility as util
import rf.tailChase as personality
from rf.moveScore import scoreMove
# >>>>>>>>> 17df5e2ef968ac0064231ff335d4628d00c1a883

def action(data):
	"""
	Purpose:
	Return UP, DOWN, LEFT, or RIGHT based on which move is the best.
	Will navigate to food when hungry and avoid occupied space

	Parameters:
	data (str): json format of data returned from the game server

	Returns:
	str:"UP" or "LEFT" or "RIGHT" or "DOWN", a move the snake will do

	"""

	# DATA_CONSTRUCT @BEGIN - Defining and Importing Data for class use

	# My Body data
	bodyParts = data['you']['body'] #List of my own body parts (May not need because we are inside of JSON[snakes] when avoiding collision)
	head = [bodyParts[0]['x'],bodyParts[0]['y']] #My head
	tail = bodyParts[-1]['x'], bodyParts[-1]['y'] #My tail
	hp = data['you']['health'] #My health
		
	# Game Board Data
	width = data['board']['width'] #Max width of game board
	height = data['board']['height'] #Max height of game board
	allFood = data['board']['food'] #Location of food on game board
	allSnakes = data['board']['data'] #Location of all snakes on the board (Enemy and I)
		
	# Test 
	print("Turn: {}".format(data['turn']))

	# Transforming dictionary into lists

	###CREATE LIST OF FOOD###
	# List of coordinates currently ocuppied by food
	foodList = []
	# Add and iterate through list of food on the game board
	for food in allFood:
		item = [food['x'], food['y']]
		foodList.append(item)
	
	###CREATE LIST OF OCCUPIED SPACES###
	# List of coordinates currently occupied by all snakes on the board
	occupiedList = []
	# Add each parts of the snake into the occupied list
	# Iterate through list of snakes
	for snake in allSnakes:
    	# Add and iterate through list of bodyparts on snake
		for piece in snake['body']:
			part = (piece['x'], piece['y'])
			occupiedList.append(part)

	# DATA_CONSTRUCT @END


	# Create dictionary of lists of next moves that do not run into occupied space
	legalMoves = util.checkBubbleOutBound(head, occupiedList, width, height)
	# Get the coordinates of the most optimal food to go for
	myFood = optimalFood.getFood(occupiedList, foodList, head, width, height)	
	# Choose which stratergy to implement, given the information we have
	result = stratMoves(legalMoves, occupiedList, myFood, head, hp)

	#res = result
	#res = optimalFood.getFood(legalMoves, foodList, head)
	#return res
	return result

def stratMoves(legalMoves, occupiedList, foodMove, head, tail, hp):
	# Will get food if hp is less than 75
	if (hp < 75):
    		print('getting food')
		res = foodMove
	# Will chase its own tail if not hungry
	else:
		print('chasing tail')
		# Currently has a defensive/non-agressive personality
		# Where we will always chase our tail by default
		res = personality.myChase(head, tail, legalMoves)
	return res