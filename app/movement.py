import random
import json

def choose_dir(data):
	"""

	"""

	bodyParts = data['you']['body'] # list of my own body parts
	head = [bodyParts[0]['x'],bodyParts[0]['y']] # head of snake
	neck = bodyParts[1] # piece directly after head
	
	occupiedList = [] # List of spaces currently occupied
	for bodyPart in bodyParts:
		part = [bodyPart['x'], bodyPart['y']]
		occupiedList.append(part)
		print(occupiedList)

	directions = ["up", "down", "left", "right"]
	return 'down'


