class Player:
    def __init__(self):
        self.display = 'A'
        self.num_water_buckets = 0
        self.row = 0
        self.col = 0
    
    def set_row(self, row):
        self.row = row

    def set_col(self, col):
        self.col = col

    def add_bucket(self):
        self.num_water_buckets +=1
    
    def remove_bucket(self):
        self.num_water_buckets -= 1

    def __str__(self):
        return "Player"
    def __repr__(self):
        return self.__str__()

    def move(self, move): #for player movement, respective keys provide respective update to coordinates
        if move == "s":
            return [1, 0]
        if move == "w":
            return [-1, 0]            
        if move == "a":
            return [0, -1]
        if move == "d":
            return [0, 1]
        if move == "q":
            return [0, 0]
        if move == "e":
            return [0, 0]
        if move == "S":
            return [1, 0]
        if move == "W":
            return [-1, 0]            
        if move == "A":
            return [0, -1]
        if move == "D":
            return [0, 1]
        if move == "Q":
            return [0, 0]
        if move == "E":
            return [0, 0]
