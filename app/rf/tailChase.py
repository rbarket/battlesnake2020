#@TODO INCOMPLETE
def actionTODO(moveList, enemyBodyList, head, tail, width, height, hp):
    """
    Purpose: To decide whether to chase my tail or to attack.
             This function can be deleted if we implement StratMoves method under moveChoice.py 

    Parameter:
    moveList(list):
    enemyBodyList(list):
    head(dict):
    tail(dict):
    width(int):
    height(int):
    hp(int):
    
    Return:
    returnMove(string): Move needed in order to chase tail
    """
    # @TODO GET SNAKE TO ESCAPE IT'S OWN BODY WHEN IT ENCAPSULATE'S ITSELF
    randMethod = {enemyChase(head, tail, moveList), myChase(head, enemyBodyList, enemyBodyList)}
    return random.randMethod

def myChase(head, tail, moveList):
    """
    Purpose: To chase my own tail

    Parameter:
    head(dict): Positional coordinates of my head
    tail(dict): Positional coordinates of my tail
    moveList(list): list of moves I can execute

    Return:
    returnMove(string): Move needed in order to chase tail
    """
    
    # Initialize Values
    #Arbitrary Value
    moveToTail = 'up' 
    # Calculate the distance between head and tail
    distance = abs(head[0] - tail[0]) + abs(head[1] - tail[1])
    
    #Simply move towards the closest direction in order to follow the tail
    for direction in moveList.items():
        if (direction < distance):
            movetoTail = direction
    return movetoTail

# @TODO INCOMPLETE FUNCTION
def enemyChaseTODO(head, moveList, enemyBodyList):
    
    # Initialize values

    moveToEnemy = 'up' # arbitrary value
    distance = abs(head[0] - tail[0]) + abs(head[1] - tail[1]) # calculate the distance between head and enemy's tail

# @TODO INCOMPLETE FUNCTION
def closestEnemy(enemyBodyList):
    #@DO SOMETHING