import json
from main import boardTypes

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


