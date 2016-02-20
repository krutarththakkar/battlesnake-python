import json
import math
import random

def distanceBetweenTwoPoints(point1, point2):
	return math.sqrt( (point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 )

def createBoardObject(data):
    print data
    #Matrix = [[0 for x in range(data.height)] for x in range(data.width)]

def getTaunt():
    bieberqoutes = ['I make mistakes growing up. I\'m not perfect; I\'m not a robot. -Justin Bieber', 'I\'m crazy, I\'m nuts. Just the way my brain works. I\'m not normal. I think differently. -Justin Bieber', 'Friends are the best to turn to when you\'re having a rough day. -Justin Bieber', 'I leave the hip thrusts to Michael Jackson. -Justin Bieber', 'It\'s cool when fans spend so much time making things for me. It means a lot. -Justin Bieber', 'No one can stop me. -Justin Bieber']
    
    return random.choice(bieberqoutes)

def getSelf(snakes):
    snakeId = "72ad0c75-244b-4e30-9169-4584cf4fee28"

    for snake in snakes:
        if snake['id'] == snakeId:
            return snake

    return False

