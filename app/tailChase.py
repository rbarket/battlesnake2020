def action(moveList, occupiedList, head, tail, width, height):
    """
    _Purpose: To chase my own tail

    _Parameter:
    move(dict): List of moves that do not run into occupied space
    occupied(dict): List of occupied spaces (Positional coordinates of other snake/snakebodies)
    head(dict): Positional coordinates of my current head
    width(dict): Maximum board width 
    height(dict): Maximum board height 

    _Return:
    returnMove(string): Move needed in order to chase tail
    """
    # @TODO GET SNAKE TO ESCAPE IT'S OWN BODY WHEN IT ENCAPSULATE'S ITSELF
    
    # Initialize values

    moveToTail = 'up' # arbitrary value
    distance = abs(head[0] - tail[0]) + abs(head[1] - tail[1]) # calculate the distance between head and tail
    
    #Simply move towards the closest direction in order to follow the tail
    for direction in moveList.items():
        if (direction < distance):
            movetoTail = direction
    return movetoTail

