from game_parser import read_lines
from game_parser import parse
from grid import grid_to_string
from player import Player
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)



class Game:
    def __init__(self):
        pass


    def search_for_start(self,read_lines_list):
        for y, string in enumerate(read_lines_list):
            for x, cells in enumerate(string):
                if cells == "X":
                    start_coords = [y,x]
                    return start_coords   

    def current_coords(self, y, x):
        self.x = x
        self.y = y
        return [self.y, self.x]

    def gameMove(self, move):
        pass
    
    def read_lines_output(self, filename):
        return read_lines(filename)
    
    def parse_output(self, lines):
        return parse(lines)


    def grid_output(self, end_lines, player):
        return grid_to_string(end_lines, player)

    
