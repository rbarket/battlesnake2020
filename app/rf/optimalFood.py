from math import sqrt
from utility import *
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

def getFood(moves, occupied, foodList, head):
	
	# Initialize Variables
	bestFood = {food: 0} #dictionairy
	for food in foodList:
