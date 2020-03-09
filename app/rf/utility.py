#Utility class

def smallestDistanceItem(itemA, itemB, returnType):
    """
    _Method: smallestDistanceItem(itemA, itemB, returnType):

    _Purpose:
    To calculate the smallest distance between itemA to itemB
    Returns the itemB or coordinates of itemB which is the closest to itemA

    _Parameters:
	itemA (dict): The coordinates of itemA (original position)
    itemB (dict): The coordiantes of itemB (item in which we are comparing original position to)
    returnType (string): depending on what the algorithm asks we can return multiple things ["distance", "item", "list", "noList", or "all"]

    _Returns:
	smallestVal (int) [distance]: Returns the distance (amount of spaces) between itemA and itemB
    closestItem (dict) [item]: Returns the coordinates of the item closest to itemA
    itemBList (dict) [list]: Returns a dictionary [Key: Distance, Value: Coordinates [x,y]]
    smallestVal, closestItem (int, dict) [noList]: Returns smallestVal and closestItem respectivally
    smallestVal, closesItem, itemBList (int, dict, dict) [all]: Returns all of the above, except noList, respectivelly
    """
    # Initializing variables
    smallestVal = 1000000 # An arbitrarily high number so that it may be replaced by a given set of smaller numbers
    closestItem = [0,0]  
    itemBList = {}

    for posB,  in itemB.items():
        distance = abs(itemA[0] - posB[0]) + abs(itemA[1] - posB[1])
        if (distance < smallestVal):
            smallestVal = distance
            closestItem = itemB
        itemBList[distance] = itemB    

    if (returnType == "distance"):
        return smallestVal
    elif (returnType == "item"):
        return closestItem
    elif (returnType == "list"):
        return itemBList
    elif (returnType == "noList"):
        return smallestVal, closestItem
    elif (returnType == "all"):
        return smallestVal, closestItem, itemBList

def checkBubbleScore(point, occupied, width, height):
    score = 0
    # Check if the position LEFT of the head is occupied OR out of bounds
    if not (([point[0]-1,point[1]] in occupied) or (point[0]-1 < 0)) :
    	score += 1
	# Check if the position RIGHT of the head is occupied OR out of bounds
	if not (([point[0]+1,point[1]] in occupied) or (point[0]+1 > width-1)) :
		score += 1
	# Check if the position UP of the head is occupied OR out of bounds
	if not (([point[0],point[1]-1] in occupied) or (point[1]-1 < 0)) :
		score += 1
	# Check if the position DOWN of the head is occupied OR out of bounds
	if not (([point[0],point[1]+1] in occupied) or (point[1]+1 > height-1)) :
		score += 1
    return score

def checkBubbleUpdate(point, occupied, width, height):
    score = 0
    # Check if the position LEFT of the head is occupied OR out of bounds
    if not (([point[0]-1,point[1]] in occupied) or (point[0]-1 < 0)) :
    	return 1
	# Check if the position RIGHT of the head is occupied OR out of bounds
	if not (([point[0]+1,point[1]] in occupied) or (point[0]+1 > width-1)) :
		return 1
	# Check if the position UP of the head is occupied OR out of bounds
	if not (([point[0],point[1]-1] in occupied) or (point[1]-1 < 0)) :
		return 1
	# Check if the position DOWN of the head is occupied OR out of bounds
	if not (([point[0],point[1]+1] in occupied) or (point[1]+1 > height-1)) :
		return 1

    











