import json
import math
import random
from main import boardTypes

def distanceBetweenTwoPoints(point1, point2):
	return  (abs((point2[0] - point1[0])) + abs((point2[1] - point1[1])))


def createBoardObject(data):
    global boardTypes
    Board = [[0 for x in range(data["height"])] for x in range(data["width"])]

    # Start off as empty
    for i in range(data["height"] - 1):
        for j in range(data["width"] - 1):
            Board[i][j] = boardTypes['Empty']

    # Find Snakes
    for snake in data["snakes"]:
        for index, point in enumerate(snake["coords"], start=0):
            if index == 0:
                Board[point[0]][point[1]] = boardTypes['Snake_Head']
            else:
                if Board[point[0]][point[1]] != boardTypes['Snake_Head']:
                    Board[point[0]][point[1]] = boardTypes['Snake_Body']
    # Find Food
    for apple in data["food"]:
        print apple
        Board[apple[0]][apple[1]] = boardTypes['Food']

    # Find Walls
    if "walls" in data:
        for wall in data["walls"]:
            print wall
            Board[wall[0]][wall[1]] = boardTypes['Wall']
    else:
        print "No Walls object, must be a classic games"

    return Board

def getTaunt():
    bieberqoutes = ['I make mistakes growing up. I\'m not perfect; I\'m not a robot. -Justin Bieber', 'I\'m crazy, I\'m nuts. Just the way my brain works. I\'m not normal. I think differently. -Justin Bieber', 'Friends are the best to turn to when you\'re having a rough day. -Justin Bieber', 'I leave the hip thrusts to Michael Jackson. -Justin Bieber', 'It\'s cool when fans spend so much time making things for me. It means a lot. -Justin Bieber', 'No one can stop me. -Justin Bieber']
    
    return random.choice(bieberqoutes)

def whichSnake(point, data):
    for snake in data["snakes"]:
        for snakePoint in data["coords"]:
            if point == snakePoint:
                return snake["id"]



def getSelf(snakes):
    snakeId = "72ad0c75-244b-4e30-9169-4584cf4fee28"

    for snake in snakes:
        if snake['id'] == snakeId:
            return snake

    return False