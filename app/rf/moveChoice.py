import random
import json
import optimalFood


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
	hp = data['you']['health'] #My health
		
	# Game Board Data
	width = data['board']['width'] #Max width of game board
	height = data['board']['height'] #Max height of game board
	foodLoc = data['board']['food'] #Location of food on game board
	allSnakes = data['board']['data'] #Location of all snakes on the board (Enemy and I)
		
	# Test 
	print("Turn: {}".format(data['turn']))

	# Transforming dictionary into lists
	occupiedList = [] # List of coordinates currently occupied
	for myBody in bodyParts: #@TODOLETE MAY NOT NEED BECAUSE WE ARE LISTED INSIDE snakeList
		item = [myBody['x'], myBody['y']]
		occupiedList.append(item)
		
	foodList = [] # List of coordinates with food items
	for food in foodLoc:
		item = [food['x'], food['y']]
		foodList.append(item)

	snakeList = [] # List of all snakes on the board
	
	# DATA_CONSTRUCT @END


	# Create dictionary of lists of next moves that do not run into occupied space
	legalMoves = possibleMoves(occupiedList, width, height, head) # only moves that are possible
	# Create dictionary of lists of food the snake can go for
	foodMoves = optimalFood(legalMoves, foodList, head)	
	# Choose which stratergy to implement, given the information we have
	result = stratMoves(legalMoves, occupiedList, foodMoves, head, hp)

	#res = result
	#res = optimalFood.getFood(legalMoves, foodList, head)
	#return res
	return result

def possibleMoves(occupied, width, height, head):
	"""
	_Purpose:
	Returns list of moves that do not run into occupied space

	_Parameters:
	occupied (list): occupied positions
	width (int): width of board
	height (int): height of board 
	head (list): xy pos of head ex. [3,5]

	_Returns:
	moves (list): A list of strings with (x,y) coordinates containing moves that do not run into occupied space
	"""
	
	moves = {}
	# Check if the position left of the head is occupied OR out of bounds
	if not (([head[0]-1,head[1]] in occupied) or (head[0]-1 < 0)) :
		item = {'left': [head[0]-1,head[1]] }
		moves.update(item)
	# Check if the position right of the head is occupied OR out of bounds
	if not (([head[0]+1,head[1]] in occupied) or (head[0]+1 > width-1)) :
		item = {'right': [head[0]+1,head[1]] }
		moves.update(item) 
	# Check if the position up of the head is occupied OR out of bounds
	if not (([head[0],head[1]-1] in occupied) or (head[1]-1 < 0)) :
		item = {'up': [head[0],head[1]-1] }
		moves.update(item)
	# Check if the position down of the head is occupied OR out of bounds
	if not (([head[0],head[1]+1] in occupied) or (head[1]+1 > height-1)) :
		item = {'down': [head[0],head[1]+1] }
		moves.update(item)

	return moves

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