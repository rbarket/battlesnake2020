from math import sqrt
import rf.utility as util

def getFoodList(moves, foodList, head):
	""" 
	@TODO FUNCTION UNCONSTRUCTED - At this stage a list of food is uneeded
	_Purpose: Create a list of the best choice for food

	_Parameters:
	moves (dict): POSSIBLE moves e.g {left: [3,5], up: [4,6]}
	foods (list): xy locations of food pieces e.g [3,5]
	head (list): xy location of head e.g [3,5]

	_Returns:
	dict: List of foods - With the first index to last is the best to worst
		  Score: [xLocation][yLocation] 
	"""
	#Initialize variables
	optimalList = {}
	nearestFood = smallestDistanceItem(head, foodList, "closestItem") 
	

	return optimalList

def getFood(occupied, foodList, head, width, height):
	""" 
	Purpose:To get the coordinate of the most optimal food to go for

	Parameters:
	occupied(list): List off all occupied spaces
	foodList(dict): List off the current food on the board
	head(dict): Coordinates of my head
	width(int): Maximum width of the game board
    height(int): Maximum height of the game board

	Returns:
	bestFood(dict): Coordinates of the best and/or most optimal food on the board
	"""
	# Initializing variables with arbitrary values
	foodPos = (-1, -1)
	foodScoredList = {foodPos: 0}
	
	# Insert foodList into foodScoredList with a score of 0
	for food in foodList:
    		foodScoredList.update({food: 0})

	#SCORE_FOOD @BEGIN

	# +1 for the closest food from our head
	foodScoredList.update({util.closestItem(head, foodList): 1})

	# +1 for each free space beside the food (excluding diagonal spaces)
	for food in foodScoredList.items():
		foodScoredList.update({food: util.checkBubbleScore(food, occupied, width, height)})
	
	
	"""
	# -1 if enemy head within 2 spaces of food
	# -2 if enemy head directly beside food
	@TODO NEED TAILCHASE FUNCTION TO COMPLETE
	"""

	"""
	Possible bug in this function because bestFood may only be coordinates
	return needs to be a string to currently compile well
	"""
	# Retreieving best food in list with the highest score
	# and return it because it's the most optimal food
	bestScore = -1
	bestFood = {}
	for food, score in foodScoredList.items([1]):
		if (foodScoredList.items([1]) > bestScore):
			bestScore = foodScoredList.items([1])
	return bestFood