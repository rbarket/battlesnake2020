def checkBubbleUpdate(point, occupied, width, height):
    """
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
	(boolean): True of the four directions are occupied
    """
    # Check if the position LEFT of the head is occupied OR out of bounds
    if not (([point[0]-1,point[1]] in occupied) or (point[0]-1 < 0)) :
    	return True
	# Check if the position RIGHT of the head is occupied OR out of bounds
	if not (([point[0]+1,point[1]] in occupied) or (point[0]+1 > width-1)) :
		return True
	# Check if the position UP of the head is occupied OR out of bounds
	if not (([point[0],point[1]-1] in occupied) or (point[1]-1 < 0)) :
		return True
	# Check if the position DOWN of the head is occupied OR out of bounds
	if not (([point[0],point[1]+1] in occupied) or (point[1]+1 > height-1)) :
		return True
