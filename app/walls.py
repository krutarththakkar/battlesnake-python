import json
from utility import *
class Walls():
	#def __init__(self):
    #def distanceToWalls:
    def wallCollision(self, game_json, direction, mySnake, snakes):
    	#if game_json == "":
    	#	game_json = "{u'height': 10, u'snakes': [{u'age': 0, u'name': u'', u'health': 100, u'message': u'', u'status': u'alive', u'id': u'72ad0c75-244b-4e30-9169-4584cf4fee28', u'taunt': u'', u'coords': [[2, 2], [2, 2], [2, 2]], u'kills': 0}], u'width': 10, u'turn': 0, u'game': 1, u'food': [], u'mode': u'classic'}";
    	
    	#print "json: " + str(game_json)

    	#our_snake = getSelf(snakes)
    	#print "our snake " + str(our_snake)
    	#snake_head = our_snake["coords"][0]
    	#print "head " + str(snake_head)
    	snake_head = mySnake.head

    	width = game_json["width"]
    	height = game_json["height"]
    	#print " width " + str(width) + " height " + str(height)

    	north_result = 100
    	east_result = 100
    	west_result = 100
    	south_result = 100 

    	if snake_head[0] == 0: # head on left side, don't go west
    		west_result = 0
    		direction.west = 0

    	if snake_head[0] == width - 1: # head on right side, don't go east
    		east_result = 0
    		direction.east = 0

    	if snake_head[1] == 0: # head on top side, don't go north
    		north_result = 0
    		direction.north = 0		

    	if snake_head[1] == height - 1: # head on bottom, dont go south
    		south_result = 0	
    		direction.south = 0

    	result_json = {"north":north_result, "east":east_result, "west":west_result, "south":south_result}
    	#print "result_json: " + str(result_json)
    	#return result_json 
    	return direction



    def snakeCollision(self, game_json, direction, mySnake, snakes):
    	#snakes = []
    	#for snake in data["snakes"]:
        #	snakes.append(Snake(snake))

        #snakes = game_json["snakes"]
        #print "len " + str(len(snakes))
        for s in xrange(0, len(snakes)): # for each snake in game
			#print " snake " + " " + str(s)
			snake = snakes[s]
			point_coords = snake.coordinates
			#print " s " + str(point_coords)

			for c in xrange(0, len(point_coords)):	# fore each point in snake
				point_coord = snake.coordinates[c]
				#print " point " + str(point_coord[0]) +" " + str(point_coord[1])

				if mySnake.head[0] - 1 == point_coord[0] and mySnake.head[1] == point_coord[1]: # snake on left
					direction.west = 0
		    		print "Snake on left"

		    	if mySnake.head[0] + 1 == point_coord[0] and mySnake.head[1] == point_coord[1]: # snake on right
		    		direction.east = 0
		    		print "Snake on right"

		    	if mySnake.head[0] == point_coord[0] and mySnake.head[1] - 1 == point_coord[1]: # snake on top
					direction.north = 0	
					print "Snake above"	

		    	if mySnake.head[0] == point_coord[0] and mySnake.head[1] + 1 == point_coord[1]: # head on bottom side, don't go north	
					direction.south = 0
					print "Snake below"

    	return direction



