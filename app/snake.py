from utility import *

class Snake():
	
    def __init__(self, snake):
        self.id = snake['id'] 
        self.age = snake['age']
        self.health = snake['health']
        self.status = snake['status']
        self.coordinates = snake['coords']
        self.head = self.coordinates[0]
        self.length = len(self.coordinates)
        
    def shouldAttack(self, enemySnake):
	    if self.lenth < enemySnake.length
	        return False
	    
	    if distanceBetweenTwoPoints(self.head, enemySnake.head) < 3
	        return True
	        
	def attackDirection():
	
	def attack(directions, snakes):
		for snake in snakes
            if snake.id == self.id
               continue
            if shouldAttack(snake)
                direction = attackDirection()
		if shouldAttack()
		    direction = attackDirection()
		else
		    