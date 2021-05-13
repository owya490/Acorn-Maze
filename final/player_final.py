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

    def move(self, move):
        if move == "s":
            #take current position and add 1 to list counter in list of lists
            return [1, 0]
        if move == "w":
            #take current position and add 1 to list counter in list of lists
            return [-1, 0]            
        if move == "a":
            #take current position and add 1 to list counter in list of lists
            return [0, -1]
        if move == "d":
            #take current position and add 1 to list counter in list of lists
            return [0, 1]
        if move == "q":
            #take current position and add 1 to list counter in list of lists
            return [0, 0]
        if move == "e":
            #take current position and add 1 to list counter in list of lists
            return [0, 0]
        pass
