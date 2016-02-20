import json

class Foods():
	def __init__(self, foods):
		print foods
		self.foods = foods

	def distanceToFood(self, snake):
		foods = []
		head = snake["coords"][0]
		for food in self.foods:
			x =  head[0] - food[0]
			y =  head[1] - food[1]
			foods.append(abs(x) + abs(y))
		return foods


	def amClosest(self, snakes, mySnake):
		myDistance = self.distanceToFood(mySnake)
		for snake in snakes:
			snakeDistance = self.distanceToFood(snake)

			for x in xrange(0,len(snakeDistance)):
				if myDistance[x] > snakeDistance[x]:
					myDistance[x] = 100

				if myDistance[x] == snakeDistance[x]:
					if len(snake['coords']) > len(mySnake['coords']):
						myDistance[x] = 100

		closest = []
		for distance in myDistance:
			if distance < 100:
				closest.append(distance)
			else:
				closest.append(-1)

		return closest

	def goTowards(self, closest, direction, mySnake):
		head = mySnake["coords"][0]
		for x in xrange(0, len(self.foods)):
			if closest[x]:
				print "i am closest to " + str(closest[x])
				food = self.foods[x]

				if food[0] < head[0]:
					direction.north *= 1.5
				elif food[0] > head[0]:
					direction.south *= 1.5

				if food[1] < head[1]:
					direction.east *= 1.5
				elif food[1] > head[1]:
					direction.west *= 1.5
		return direction













