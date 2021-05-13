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
    def __init__(self): #, filename
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

    
    # def memory(self, cell):
    #     self.memory = cell

    

p = Player() #init player
g = Game() #init game
victory_point = 0
moves_list = []
lines = g.read_lines_output("board_hard.txt") #reading lines convert into list of strings

start_coords = g.search_for_start(lines) #searching for start "X" to place player

current_coords = g.current_coords(start_coords[0],start_coords[1])

p.set_row(current_coords[0])
p.set_col(current_coords[1])


parse_output = g.parse_output(lines) #changing strings into cells
#print(parse_output)
memory=parse_output[start_coords[0]][start_coords[1]] #placing cell which player is on in memory
#print(memory)

parse_output[start_coords[0]][start_coords[1]] = p #replacing start cell with player

grid_output = g.grid_output(parse_output, p)
print(grid_output)

while True:
    parse_output[current_coords[0]][current_coords[1]] = memory

    # last_turn_coords = [current_coords[0], current_coords[1]]
    # print(last_turn_coords)

    user_movement = input("\nInput a move: ")

    moves_list.append(user_movement)
    movement = (p.move(user_movement))
    current_coords[0] += movement[0] #changing y
    current_coords[1] += movement[1] #changing x

    if user_movement == "q":
        print("\nBye!")
        exit()

    if user_movement == "e" and type(parse_output[current_coords[0]][current_coords[1]]) == Teleport:
        parse_output[current_coords[0]][current_coords[1]] = p
        for n, string in enumerate(parse_output):
                for i, cells in enumerate(string):
                    if cells.display == memory.display:
                        new_coords = [n, i]
                        
                        break
        parse_output[current_coords[0]][current_coords[1]] = memory
        current_coords = new_coords
        parse_output[current_coords[0]][current_coords[1]] = p

        grid_output = g.grid_output(parse_output, p)
        print(grid_output)
        print("\nWhoosh! The magical gates break Physics as we know it and opens a wormhole through space and time..")
        continue
    if user_movement == "e":
        continue
    #print(current_coords)
    #memory = parse_output[current_coords[0]][current_coords[1]]
    #print(memory)

    #print(type(parse_output[current_coords[0]][current_coords[1]]))


    if type(parse_output[current_coords[0]][current_coords[1]]) != Air:
        if type(parse_output[current_coords[0]][current_coords[1]]) == Wall:
            current_coords = parse_output[current_coords[0]][current_coords[1]].step_jank(current_coords, user_movement)
            memory = parse_output[current_coords[0]][current_coords[1]]
            parse_output[current_coords[0]][current_coords[1]] = p
            grid_output = g.grid_output(parse_output, p)
            print(grid_output)
            print("\nYou walked into a wall. Oof!")
        
        if type(parse_output[current_coords[0]][current_coords[1]]) == Start:
            current_coords = parse_output[current_coords[0]][current_coords[1]].step_jank(current_coords, user_movement)
            memory = parse_output[current_coords[0]][current_coords[1]]
            parse_output[current_coords[0]][current_coords[1]] = p
            grid_output = g.grid_output(parse_output, p)
            print(grid_output)
            print("\nYou walked into a wall. Oof!")

        if type(parse_output[current_coords[0]][current_coords[1]]) == Water:
            memory = Air()
            p.add_bucket()
            parse_output[current_coords[0]][current_coords[1]] = p
            grid_output = g.grid_output(parse_output, p)
            print(grid_output)
            print("\nThank the Honourable Furious Forest, you've found a bucket of water!")
#should outsource these functions to the cell.py 
        if type(parse_output[current_coords[0]][current_coords[1]]) == Fire:
            if p.num_water_buckets <= 0:
                parse_output[current_coords[0]][current_coords[1]] = p
                grid_output = g.grid_output(parse_output, p)
                print(grid_output)
                print("\nYou step into the fires and watch your dreams disappear :(")
                break
            if p.num_water_buckets > 0:
                p.remove_bucket()
                memory = Air()
                parse_output[current_coords[0]][current_coords[1]] = p
                grid_output = g.grid_output(parse_output, p)
                print(grid_output)
                print("\nWith your strong acorn arms, you throw a water bucket at the fire. You acorn roll your way through the extinguished flames!")

        
        if type(parse_output[current_coords[0]][current_coords[1]]) == Teleport:
            memory = parse_output[current_coords[0]][current_coords[1]]
            parse_output[current_coords[0]][current_coords[1]] = p
            
            for n, string in enumerate(parse_output):
                for i, cells in enumerate(string):
                    if cells.display == memory.display:
                        new_coords = [n, i]

            parse_output[current_coords[0]][current_coords[1]] = memory
            current_coords = new_coords
            parse_output[current_coords[0]][current_coords[1]] = p

            grid_output = g.grid_output(parse_output, p)
            print(grid_output)
            print("\nWhoosh! The magical gates break Physics as we know it and opens a wormhole through space and time..")


        

        if type(parse_output[current_coords[0]][current_coords[1]]) == End:
            parse_output[current_coords[0]][current_coords[1]] = p
            grid_output = g.grid_output(parse_output, p)
            print(grid_output)
            victory_point +=1
            print("\nYou conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable Furious Forest Throne, restoring your hometown back to its former glory of rainbow and sunshine! Peace reigns over the lands.")
            break

    else:
        memory = parse_output[current_coords[0]][current_coords[1]]
        parse_output[current_coords[0]][current_coords[1]] = p
        grid_output = g.grid_output(parse_output, p)
        print(grid_output)
    
    p.set_row(current_coords[0])
    p.set_col(current_coords[1])


if victory_point == 0:
    print("\nThe Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of ash and is scattered to the winds by the next storm... You have been roasted.")
    print("\nYour made {} moves.".format(len(moves_list)))
    joined_moves = ", ".join(moves_list)
    print("Your moves: {}".format(joined_moves))
    print("""
=====================
===== GAME OVER =====
=====================""")


if victory_point > 0:
    print("\nYour made {} moves.".format(len(moves_list)))
    joined_moves = ", ".join(moves_list)
    print("Your moves: {}".format(joined_moves))
    print("""
=====================
====== YOU WIN! =====
=====================""")

o = input()
if o == "":
    exit()
#create while loop, while player is alive, keep goin
#need to store in memory the cell which the player is sittin on