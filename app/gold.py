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
        print snakesinfo
        # print snakesinfo
        # print json.dumps(snakes, indent=4)

        our_snakeid = '72ad0c75-244b-4e30-9169-4584cf4fee28'
        other_snakes = {}
        our_snake = {}
        dist = [] # Distance for other snakes
        for i in snakesinfo['snakes']:
            if i['id'] != our_snakeid:
                # print i['coords'][0]
                dist.append(utility.distanceBetweenTwoPoints(i['coords'][0], snakesinfo['gold']))

            else:
                our_dist = utility.distanceBetweenTwoPoints(i['coords'][0], snakesinfo['gold'])
                snake = i['id']
                our_snake[snake] = i['coords'][0]

        # for i in other_snakes:
            # utility.distanceBetweenTwoPoints(snakesinfo[gold], i)
        print dist
        print our_dist

        go_for_the_gold = True

        for i in dist:
            if our_dist < i: 
                print 'yay our distance is less go for the gold'
            else:
                print 'damn it don\'t go for the gold'
                go_for_the_gold = False


distanceToGold()