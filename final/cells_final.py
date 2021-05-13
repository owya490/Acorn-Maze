class Start:
    def __init__(self):
        self.display = 'X'
    
    def __str__(self):
        return "Start"
    def __repr__(self):
        return self.__str__()

    def step(self, game):
        pass
    
    def step_jank(self, current_coords, user_movement):
        if user_movement == "s":
            current_coords[0] += -1
            return current_coords
        if user_movement == "w":
            current_coords[0] += 1
            return current_coords
        if user_movement == "a":
            current_coords[1] += 1
            return current_coords
        if user_movement == "d":
            current_coords[1] += -1
            return current_coords


class End:
    def __init__(self):
        self.display = 'Y'

    def __str__(self):
        return "End"
    def __repr__(self):
        return self.__str__()
    
    def step(self, game):
        pass


class Air:
    def __init__(self):
        self.display = ' '

    def __str__(self):
        return "Air"
    def __repr__(self):
        return self.__str__()

    def step(self, game):
        pass


class Wall:
    def __init__(self):
        self.display = '*'

    def __str__(self):
        return "Wall"
    def __repr__(self):
        return self.__str__()
    
    def step(self, game):
        current_coords = last_turn_coords
        pass
    def step_jank(self, current_coords, user_movement):
        if user_movement == "s":
            #take current position and add 1 to list counter in list of lists
            current_coords[0] += -1
            return current_coords
        if user_movement == "w":
            #take current position and add 1 to list counter in list of lists
            current_coords[0] += 1
            return current_coords
        if user_movement == "a":
            #take current position and add 1 to list counter in list of lists
            current_coords[1] += 1
            return current_coords
        if user_movement == "d":
            #take current position and add 1 to list counter in list of lists
            current_coords[1] += -1
            return current_coords

        
    


class Fire:
    def __init__(self):
        self.display = 'F'

    def __str__(self):
        return "Fire"
    def __repr__(self):
        return self.__str__()

    def step(self, game):
        pass


class Water:
    def __init__(self):
        self.display = 'W'

    def __str__(self):
        return "Water"
    def __repr__(self):
        return self.__str__()

    def step(self, game):
        pass

    def step_jank(self):
        pass



class Teleport:
    def __init__(self, display):
        self.display = str(display)  # You'll need to change this!
    
    def __str__(self):
        return "Teleport{}".format(self.display)
    def __repr__(self):
        return self.__str__()

    def step(self, game):
        pass
