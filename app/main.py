import bottle
from walls import *

snakeId = "72ad0c75-244b-4e30-9169-4584cf4fee28"

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    head_url = '%s://%s/static/rbm-head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    return {
        'color': '#00ff00',
        'head': head_url
    }


@bottle.post('/start')
def start():
    data = bottle.request.json
    print data
    # TODO: Do things with data

    return {
        'taunt': 'RBM is gong to win ' + str(data['game'])
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
    print data
    # TODO: Do things with data

    # Check for wall collision
    walls = Walls()
    collision_results = walls.wallCollision(data)
    print collision_results

    return {
        'move': 'north',
        'taunt': 'battlesnake-python!'
    }


@bottle.post('/end')
def end():
    data = bottle.request.json
    print data
    # TODO: Do things with data

    return {
        'taunt': 'battlesnake-python!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host='127.0.0.1', port=8080)
