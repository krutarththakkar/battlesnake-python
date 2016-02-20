class Snake():
	
    def __init__(self, snake):
        self.id = snake['id'] 
        self.age = snake['age']
        self.health = snake['health']
        self.status = snake['status']
        self.coordinates = snake['coords']
        self.head = self.coordinates[0]
        self.length = len(self.coordinates)    