def action(moveList, enemyBodyList, head, tail, width, height, hp):
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
    randMethod = {enemyChase(head, tail, moveList), myChase(head, enemyBodyList, enemyBodyList)}
    return random.randMethod

def myChase(moveDict, tail):
    import random
    
    # Initialize Values

    moveToTail = 'up' # arbitrary value
     # calculate the distance between head and tail
    minimum = 10000
    #Simply move towards the closest direction in order to follow the tail
    for move, coord in moveDict.items():
        distance = abs(coord[0] - tail[0]) + abs(coord[1] - tail[1])
        print("move: {}, coord: {}, distance: {}".format(move, coord, distance))
        if (distance < minimum):
            movetoTail = move
        elif (distance == minimum):
            movetoTail = random.choice([move, movetoTail])
    print("movelist: {}, bestMove: {}".format(list(moveDict.keys()), movetoTail)) 
    return movetoTail

def enemyChase(head, moveList, enemyBodyList):
    
    # Initialize values

    moveToEnemy = 'up' # arbitrary value
    distance = abs(head[0] - tail[0]) + abs(head[1] - tail[1]) # calculate the distance between head and enemy's tail
    return None

def closestEnemy(enemyBodyList):
    #@DO SOMETHING
    return None