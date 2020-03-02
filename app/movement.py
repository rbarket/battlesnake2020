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
	
	occupiedList = [] # List of spaces currently occupied
	for bodyPart in bodyParts:
		part = [bodyPart['x'], bodyPart['y']]
		occupiedList.append(part)

	legalMoves = possibleMoves(occupiedList, width, height, head) # only moves that are possible
	print(legalMoves)
	res = random.choice(legalMoves)
	print(res)
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
	moves = ['up','down','left','right'] # left, right, down and up
	if ([head[0]-1,head[1]] in occupied) or (head[0]-1 < 0) : # left is occupied OR left is out of bounds
		moves.remove('left') # remove left from possible moves

	if ([head[0]+1,head[1]] in occupied) or (head[0]+1 > width) : # right
		moves.remove('right') 

	if ([head[0],head[1]-1] in occupied) or (head[1]-1 < 0) : # up
		moves.remove('up') 

	if ([head[0],head[1]+1] in occupied) or (head[1]-1 > height) : # down
		moves.remove('down') 

	return moves

