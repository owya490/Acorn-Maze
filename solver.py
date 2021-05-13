# You may need this if you really want to use a recursive solution!
# It raises the cap on how many recursions can happen. Use this at your own risk!


import sys
from game_parser import parse
from game_parser import read_lines
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
if len(sys.argv) < 2:
    print("Usage: python3 solver.py <filename> <mode>")
    exit()
sys.setrecursionlimit(100000)
filename_input = sys.argv[1]
mode_input = sys.argv[2]

class Player:
    def __init__(self):
        self.display = 'A'
        self.num_water_buckets = 0

    def add_bucket(self):
        self.num_water_buckets +=1
    
    def remove_bucket(self):
        self.num_water_buckets -= 1

up = [-1, 0]
down = [1, 0]
left = [0, -1]
right = [0, 1]


def search_for_start(read_lines_list):
        for y, string in enumerate(read_lines_list):
            for x, cells in enumerate(string):
                if cells == "X":
                    start_coords = [y,x]
                    return start_coords   

p = Player()

def solve(mode, filename):

    grid = parse(read_lines(filename))

    coords = search_for_start(read_lines(filename))

    memory = None
    ls = []
    while True:

        if memory != left:
            coords[1] += right[1]
            if type(grid[coords[0]][coords[1]]) == Air or type(grid[coords[0]][coords[1]]) == End or type(grid[coords[0]][coords[1]]) == Start: 
                memory = right
                ls.append("d")
                break
            if type(grid[coords[0]][coords[1]]) == Water:
                memory = right
                ls.append("d")
                air = Air()
                grid[coords[0]][coords[1]] = air
                p.add_bucket()
                break
            if type(grid[coords[0]][coords[1]]) == Fire and p.num_water_buckets > 0:
                memory = right
                ls.append("d")
                air = Air()
                grid[coords[0]][coords[1]] = air
                p.remove_bucket()
                break
            if type(grid[coords[0]][coords[1]]) == Teleport:
                memory = right
                ls.append("d")
                for n, string in enumerate(grid): #searches the list for the exact same teleport, updating the players location to the new teleport exit location
                    for i, cells in enumerate(string):
                        if cells.display == grid[coords[0]][coords[1]].display:
                            new_coords = [n, i]
                coords = new_coords
                break
            else:
                coords[1] -= right[1]

        if memory != up:
            coords[0] += down[0]
            if type(grid[coords[0]][coords[1]]) == Air or type(grid[coords[0]][coords[1]]) == End or type(grid[coords[0]][coords[1]]) == Start: 
                memory = down
                ls.append("s")
                break
            if type(grid[coords[0]][coords[1]]) == Teleport:
                print("im here")
                memory = down
                ls.append("s")
                for n, string in enumerate(grid): #searches the list for the exact same teleport, updating the players location to the new teleport exit location
                    for i, cells in enumerate(string):
                        if cells.display == grid[coords[0]][coords[1]].display:
                            new_coords = [n, i]
                coords = new_coords
                break
                
            else:
                coords[0] -= down[0]

        coords[1] += left[1]
        if type(grid[coords[0]][coords[1]]) == Air or type(grid[coords[0]][coords[1]]) == End or type(grid[coords[0]][coords[1]]) == Start: 
            memory = left
            ls.append("a")
            break
        else:
            coords[1] -= left[1]

        coords[0] += up[0]
        if type(grid[coords[0]][coords[1]]) == Air or type(grid[coords[0]][coords[1]]) == End or type(grid[coords[0]][coords[1]]) == Start: 
            memory = up
            ls.append("w")
            break
        else:
            coords[0] -= down[0]
    

    while True:

        if type(grid[coords[0]][coords[1]]) == End:
            break
        if type(grid[coords[0]][coords[1]]) == Start:
            i = 0
            while i < 100:
                ls.append("o")
                i +=1
            return ls
        



        if memory != left:

            coords[1] += right[1]

            if type(grid[coords[0]][coords[1]]) == Air or type(grid[coords[0]][coords[1]]) == End or type(grid[coords[0]][coords[1]]) == Start: 
                memory = right
                ls.append("d")
                continue
            if type(grid[coords[0]][coords[1]]) == Water:
                memory = right
                ls.append("d")
                air = Air()
                grid[coords[0]][coords[1]] = air
                p.add_bucket()
                continue
            if type(grid[coords[0]][coords[1]]) == Fire and p.num_water_buckets > 0:
                memory = right
                ls.append("d")
                air = Air()
                grid[coords[0]][coords[1]] = air
                p.remove_bucket()
                continue
            if type(grid[coords[0]][coords[1]]) == Teleport:
                memory = right
                ls.append("d")
                for n, string in enumerate(grid): #searches the list for the exact same teleport, updating the players location to the new teleport exit location
                    for i, cells in enumerate(string):
                        if cells.display == grid[coords[0]][coords[1]].display:
                            new_coords = [n, i]
                coords = new_coords
                continue
            else:
                coords[1] -= right[1]



        if memory != up:

            coords[0] += down[0]

            if type(grid[coords[0]][coords[1]]) == Air or type(grid[coords[0]][coords[1]]) == End or type(grid[coords[0]][coords[1]]) == Start: 
                memory = down
                ls.append("s")
                continue
            if type(grid[coords[0]][coords[1]]) == Teleport:
                memory = down
                ls.append("s")
                for n, string in enumerate(grid): #searches the list for the exact same teleport, updating the players location to the new teleport exit location
                    for i, cells in enumerate(string):
                        if cells.display == grid[coords[0]][coords[1]].display:
                            new_coords = [n, i]
                coords = new_coords
                continue
            else:
                coords[0] -= down[0]



        coords[1] += left[1]
        if type(grid[coords[0]][coords[1]]) == Air or type(grid[coords[0]][coords[1]]) == End or type(grid[coords[0]][coords[1]]) == Start: 
    
            memory = left
            ls.append("a")
            continue
        else:
            coords[1] -= left[1]


        coords[0] += up[0]
        if type(grid[coords[0]][coords[1]]) == Air or type(grid[coords[0]][coords[1]]) == End or type(grid[coords[0]][coords[1]]) == Start: 
            memory = up
            ls.append("w")
            continue
        else:
            coords[0] -= up[0]
        


        if type(grid[coords[0]][coords[1]]) == Teleport:

                cell_memory = grid[coords[0]][coords[1]]
                air = Air()
                grid[coords[0]][coords[1]] = air
                memory = "wait"
                ls.append("e")

                for n, string in enumerate(grid): #searches the list for the exact same teleport, updating the players location to the new teleport exit location
                    for i, cells in enumerate(string):
                        if cells.display == cell_memory.display:
                            new_coords = [n, i]
                grid[coords[0]][coords[1]] = cell_memory


                coords = new_coords


                continue

    return ls


ls = solve(mode_input, filename_input)     
if __name__ == "__main__":

    if len(ls) > 100:
        print("There is no possible path.")

    elif len(ls) > 0:
        print("Path has {} moves.".format(len(ls)))
        print("Path: {}".format(", ".join(ls)))



