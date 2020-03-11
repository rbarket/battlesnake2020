#@TODO INCOMPLETE
def smallestDistanceItemTODO(itemA, itemB, returnType):
    """ @TODOIMCOMPLETE
    Method: smallestDistanceItem(itemA, itemB, returnType):

    Purpose:
    To calculate the smallest distance between itemA to itemB
    Returns the itemB or coordinates of itemB which is the closest to itemA

    Parameters:
	itemA (dict): The coordinates of itemA (original position)
    itemB (dict): The coordiantes of itemB (item in which we are comparing original position to)
    returnType (string): depending on what the algorithm asks we can return multiple things ["distance", "item", "list", "noList", or "all"]

    Returns:
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

    #Possible bug in for loop declaration (Look into it)
    for posB, itemB.item in itemB.items():
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
    """
    Method: checkBubbleScore(point, occupied, width, height)

    Purpose:
    To check the left, right, down, and up position, of the current position we are evaluating and
    add +1 to the score, if those positions are free

    Parameters:
	point(dict): Coordinates of the current position we are evaluating
    occupied(dict): List of coordinates that are currently occupied
    width(int): Maximum width of the game board
    height(int): Maximum height of the game board

    Returns:
	score(int): Initialized at 0, adds 1 to the score if none of the directions (Up, Left, Right, Down) are occupied, and has a maximum score of 4
    """
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
    
#@TODO INCOMPLETE FUNCTION
def checkBubbleTODO(point, occupied, width, height):
    """ INCOMPLETE FUNCTION @TODO
    _Method: checkBubbleScore(point, occupied, width, height)

    _Purpose:
    To check the left, right, down, and up position, of the current position we are evaluating and
    add +1 to the score, if those positions are free

    _Parameters:
	point(dict): Coordinates of the current position we are evaluating
    occupied(dict): List of coordinates that are currently occupied
    width(int): Maximum width of the game board
    height(int): Maximum height of the game board

    _Returns:
	score(int): Initialized at 0, adds 1 to the score if none of the directions (Up, Left, Right, Down) are occupied, and has a maximum score of 4
    """
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

def checkBubbleOutBound(point, checkFor, width, height):
    """
    Method: checkBubbleScore(point, checkFor, width, height)

    Purpose:
    To check the left, right, down, and up position, of the current position we are evaluating to see if
    they include unfavourable elements

    Parameters:
	point(dict): Coordinates of the current position we are evaluating
    checkFor(list): List of coordinates that we want to check for. We can check if they are occupied or food
    width(int): Maximum width of the game board
    height(int): Maximum height of the game board

    Returns:
	moves(list): A list of moves that do not have unfavourable elements
    """

    moves = {}

    # Check if each the list of directions we obtained includes unfavourable elements OR if it's out of bounds
    # We only add a list of directions from the list we obtained if they are not unfavourable
    
    # LEFT
    if not (( (point[0]-1, point[1]) in checkFor) or (point[0]-1 < 0)) :
	    item = {'left': (point[0]-1,point[1]) }
	    moves.update(item)
    # RIGHT
    if not (( (point[0]+1,point[1]) in checkFor) or (point[0]+1 > width-1)) :
		item = {'right': (point[0]+1,point[1]) }
		moves.update(item) 
    # UP
    if not (( (point[0],point[1]-1) in checkFor) or (point[1]-1 < 0)) :
		item = {'up': (point[0],point[1]-1) }
		moves.update(item)
    # DOWN
    if not (( (point[0],point[1]+1) in checkFor) or (point[1]+1 > height-1)) :
		item = {'down': (point[0],point[1]+1) }
		moves.update(item)

    return moves

def closestItem(point, itemList):
    """
    Method: closestItem(point, itemList, occupied, width, height)

    Purpose:
    To find the the closest item from position

    Parameters:
	point(dict): Current position we want to be evaluted from
    itemList(dict): List of items we want to find which are the closest

    Returns:
	closestItem(dict): Coordinates for the closest item from point
    """
    closestItem = {}
    # Arbitrary for initialization and will be replaced when a smaller distance is found
    smallestDistance = 10000 

    for item, itemCoord in itemList.items():
        # Get the distance (amount of spaces) between the point and item we are looking at
        # and replace current smallest distance if it's smaller
        evaluatedDistance = abs(itemCoord[0] - point[0]) + abs(itemCoord[1] - point[1])

        # test
        print('move: {}, coord: {}, xDist:{}, yDist:{}, hypotenuse:{}, food:{}'.format(move, coord, xDist, yDist, hyp, food))
        
        if (evaluatedDistance > smallestDistance):
            smallestDistance = evaluatedDistance
            closestItem = item

        #test
        print('best move is {}'.format(closestItem))

    return closestItem

def check(move, occupied, width, height, n=1):
    """
	Purpose:
	takes a move coord and returns a score based on how many free spaces are around the move of distance n

	Parameters:
	move (list): xy coord of the move
	occupied (list): xy coords all occupied spaces on board 
	width (int): width of board
	height (int): height of board
	n (int): how many spaces ahead to look (default 1)

	Returns:
	score (int): score of move
	"""
    if (n==0): # base case
		return 0	
    
    up = (move[0], move[1]-1)
    down = (move[0], move[1]+1)
    left = (move[0]-1, move[1])
    right = (move[0]+1, move[1])

    score = 0

	# for pos in coordMaker(move):


    if not (( left in occupied) or (left[0] < 0)): #left
		score += 1 + check(left, occupied, width, height, n-1)
    if not (( right in occupied) or (right[0] > width-1)): # right
		score += 1 + check(right, occupied, width, height, n-1)
    if not (( up in occupied) or (up[1] < 0)): # up
		score += 1 + check(up, occupied, width, height, n-1)
    if not (( down in occupied) or (down[1] > height-1)): #down
		score += 1 + check(down, occupied, width, height, n-1)
    return score





