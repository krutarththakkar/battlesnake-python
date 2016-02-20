import json
import utility
our_snakeid = '72ad0c75-244b-4e30-9169-4584cf4fee28'

def distanceToGold(snakesinfo):
    directions = {'north': 0,
                    'east': 0,
                    'south': 0,
                    'west': 0
                }

    dist = [] # Distance for other snakes
    for i in snakesinfo['snakes']:
        if i['id'] != our_snakeid:
            dist.append(utility.distanceBetweenTwoPoints(i['coords'][0], snakesinfo['gold']))

        else:
            our_dist = utility.distanceBetweenTwoPoints(i['coords'][0], snakesinfo['gold'])
            our_coords = i['coords'][0]
    print dist
    print our_dist

    go_for_the_gold = True

    for i in dist:
        if our_dist < i: 
            print 'yay our distance is less go for the gold'
            print snakesinfo['gold'][0]
            print our_coords[0]
            east_west = our_coords[0] - snakesinfo['gold'][0]
            north_south = our_coords[1] - snakesinfo['gold'][1] 
            print 'east_west %s north_south%s' % (east_west, north_south)
            if east_west > 0 and directions['west'] < 100:
                directions['west'] += 100
            elif east_west < 0 and directions['east'] < 100:
                directions['east'] += 100 

            if north_south > 0  and directions['north'] < 100:
                directions['north'] += 100
            elif north_south < 0  and directions['south'] < 100:
                directions['south'] += 100 
        else:
            print 'damn it don\'t go for the gold'
            return {0,0,0,0}
        if go_for_the_gold is True:
            return{directions['north'], directions['east'], directions['south'], directions['west']}