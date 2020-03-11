import random
import json
# <<<<<<<<< HEAD
import rF.optimalFood as bestFood
import rF.utility as util
from rF.moveScore import scoreMove
# >>>>>>>>> 17df5e2ef968ac0064231ff335d4628d00c1a883

def action(data):
	"""
	_Purpose:
	Return UP, DOWN, LEFT, or RIGHT based on which move is the best.
	Will navigate to food when hungry and avoid occupied space

	_Parameters:
	data (str): json format of data returned from the game server

	_Returns:
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
	foodLoc = data['board']['food'] #Location of food on game board
	allSnakes = data['board']['data'] #Location of all snakes on the board (Enemy and I)
		
	# Test 
	print("Turn: {}".format(data['turn']))

	# Transforming dictionary into lists

	###CREATE LIST OF FOOD###
	# List of coordinates currently ocuppied by food
	foodList = []
	# Add and iterate through list of food on the game board
	for food in foodLoc:
		item = [food['x'], food['y']]
		foodList.append(item)
	######
	
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
	######

	# DATA_CONSTRUCT @END


	# Create dictionary of lists of next moves that do not run into occupied space
	legalMoves = util.checkBubbleOutBound(head, occupiedList, width, height)
	# Create dictionary of lists of food the snake can go for
	foodMoves = optimalFood(legalMoves, foodList, head)	
	# Choose which stratergy to implement, given the information we have
	result = stratMoves(legalMoves, occupiedList, foodMoves, head, hp)

	#res = result
	#res = optimalFood.getFood(legalMoves, foodList, head)
	#return res
	return result

def stratMoves(legalMoves, occupiedList, foodList, head, hp):
	# Will get food if hp is less than 75
	if (hp < 75):
    		print('getting food')
		res = optimalFood.getFood(legalMoves, occupiedList, foodList, head)
	# Will chase its own tail if not hungry
	else:
		print('chasing tail')
		res = tailChase()
	return res