import json
import utility

def distanceToGold():
    '''
    get gold position
    get all snakes head postions
    Calculate closet to gold 
    are we closed to gold?
    if yes check and see if anything in the way. 

    '''
    with open('snake.json', 'r') as f:
        snakesinfo = json.load(f)
        # print snakesinfo
        # print json.dumps(snakes, indent=4)

        our_snakeid = '72ad0c75-244b-4e30-9169-4584cf4fee28'
        other_snakes = {}
        our_snake = {}
        for i in snakesinfo['snakes']:
            if i['id'] != our_snakeid:
                snake = i['id']
                # other_snakes[i]['id'] = {}
                other_snakes[snake] = {}
                other_snakes[snake]['coords'] = i['coords'][0]
                # other_snakes[i]['id'] = 'blah'
                # other_snakes[i] = []
            else:
                snake = i['id']
                our_snake[snake] = i['coords'][0]

        # for i in other_snakes:
        #     utility.distanceBetweenTwoPoints(snakesinfo[gold], i
        print json.dumps(other_snakes, indent=4)
        print json.dumps(our_snake, indent=4)

        # gold_position = snakeinfo['gold'] #can be cleaned up after by calling this directly in the next functions
        # our_distance = utility.distance()
        # our_distance = utility.distance()
        # our_distance = utility.distance()
        # our_distance = utility.distance()

distanceToGold()