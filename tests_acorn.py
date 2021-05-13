from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

from player import Player

# p = Player()
# p.add_bucket()
# print(p.num_water_buckets)

def read_lines(filename):
    """Read in a file and return the contents as a list of strings."""
    file = open(filename, "r")
    read_lines_list = []
    while True:
        line = file.readline()
        if line == "":
            break

        # line = line.strip("\n")
        read_lines_list.append(line)
    file.close()

    # read_lines_list_final = []
    # for strings in read_lines_list:
    #     read_lines_list_final.append(strings[0:15])


    return read_lines_list#_final
    pass
read_lines_list = read_lines("board_test.txt")
print(read_lines_list)

def parse(lines):
    """Transform the input into a grid.

    Arguments:
        lines -- list of strings representing the grid

    Returns:
        list -- contains list of lists of Cells
    """
    i = 0
    while i < len(lines):
        holder = lines[i].strip("\n")
        lines[i] = holder
        i +=1

    print(lines)

    result_x = 0
    result_y = 0
    result_1 = 0
    result_2 = 0
    result_3 = 0
    result_4 = 0
    result_5 = 0
    result_6 = 0
    result_7 = 0
    result_8 = 0
    result_9 = 0

    for strings in lines:
        for objects in strings:
            if objects != "*" and objects != " " and objects != "X" and objects != "Y" and objects != "F" and objects != "W" and objects != "1" and objects != "2" and objects != "3" and objects != "4" and objects != "5" and objects != "6" and objects != "7" and objects != "8" and objects != "9":
                raise ValueError ("Bad letter configuration file: {}".format(objects))
            if objects == "X":
                result_x += 1
            if objects == "Y":
                result_y += 1
            if objects == "1":
                result_1 += 1
            if objects == "2":
                result_2 += 1
            if objects == "3":
                result_3 += 1
            if objects == "4":
                result_4 += 1
            if objects == "5":
                result_5 += 1
            if objects == "6":
                result_6 += 1
            if objects == "7":
                result_7 += 1
            if objects == "8":
                result_8 += 1
            if objects == "9":
                result_9 += 1

    if result_x != 1:
        raise ValueError ("Expected 1 starting position, got {}".format(result_x))
    if result_y != 1:
        raise ValueError ("Expected 1 ending position, got {}".format(result_y))
    if result_1 == 1 or result_1 > 2:
        raise ValueError ("1 does not have an exclusively matching pad")
    if result_2 == 1 or result_2 > 2:
        raise ValueError ("2 does not have an exclusively matching pad")
    if result_3 == 1 or result_3 > 2:
        raise ValueError ("3 does not have an exclusively matching pad")
    if result_4 == 1 or result_4 > 2:
        raise ValueError ("4 does not have an exclusively matching pad")
    if result_5 == 1 or result_5 > 2:
        raise ValueError ("5 does not have an exclusively matching pad")
    if result_6 == 1 or result_6 > 2:
        raise ValueError ("6 does not have an exclusively matching pad")
    if result_7 == 1 or result_7 > 2:
        raise ValueError ("7 does not have an exclusively matching pad")
    if result_8 == 1 or result_8 > 2:
        raise ValueError ("8 does not have an exclusively matching pad")
    if result_9 == 1 or result_9 > 2:
        raise ValueError ("9 does not have an exclusively matching pad")

    list_of_cells = []
    list_of_lists_of_cells = []
    for strings in lines:
        for objects in strings:
            if objects == "*":
                wall = Wall()
                list_of_cells.append(wall)
            if objects == " ":
                air = Air()
                list_of_cells.append(air)
            if objects == "X":
                start = Start()
                list_of_cells.append(start)
            if objects == "Y":
                end = End()
                list_of_cells.append(end)
            if objects == "F":
                fire = Fire()
                list_of_cells.append(fire)
            if objects == "W":
                water = Water()
                list_of_cells.append(water)
            if objects == "1":
                teleport1 = Teleport(1)
                list_of_cells.append(teleport1)
            if objects == "2":
                teleport2 = Teleport(2)
                list_of_cells.append(teleport2)
            if objects == "3":
                teleport3 = Teleport(3)
                list_of_cells.append(teleport3)
            if objects == "4":
                teleport4 = Teleport(4)
                list_of_cells.append(teleport4)
            if objects == "5":
                teleport5 = Teleport(5)
                list_of_cells.append(teleport5)
            if objects == "6":
                teleport6 = Teleport(6)
                list_of_cells.append(teleport6)
            if objects == "7":
                teleport7 = Teleport(7)
                list_of_cells.append(teleport7)
            if objects == "8":
                teleport8 = Teleport(8)
                list_of_cells.append(teleport8)
            if objects == "9":
                teleport9 = Teleport(9)
                list_of_cells.append(teleport9)

            #Do teleporter, figure it out u monkey
        list_of_lists_of_cells.append(list_of_cells)
        list_of_cells = []
    return list_of_lists_of_cells

parse_output = parse(read_lines_list)
print(parse(read_lines_list))



# def grid_to_string(grid, player):
#     """Turns a grid and player into a string

#     Arguments:
#         grid -- list of list of Cells
#         player -- a Player with water buckets

#     Returns:
#         string: A string representation of the grid and player.
#     """
#     string = []
#     for lists in grid:
#         for objects in lists:
#             string.append(objects.display)
#         string.append("\n")

#     string.append("\nYou have {} water buckets.".format(player.num_water_buckets))
#     string_joined = "".join(string)
#     return string_joined

#     pass

# print(grid_to_string(parse_output,p))
# print("checkpoint")
# print(read_lines_list)

# def search_for_start(read_lines_list):
#     for y, string in enumerate(parse_output):
#         for x, cells in enumerate(string):
#             if cells.display == "X":
#                 start_coords = [y,x]
#                 return start_coords


# start_coords= search_for_start(read_lines_list)
# print(start_coords)
# parse_output[start_coords[0]][start_coords[1]] = p

# print(parse_output[start_coords[0]][start_coords[1]])
# print(parse_output)

# print(grid_to_string(parse_output,p))



# import os
# import sys
# from game_parser import read_lines
# from game_parser import parse
# from grid import grid_to_string
# from player import Player
# from cells import (
#     Start,
#     End,
#     Air,
#     Wall,
#     Fire,
#     Water,
#     Teleport
# )



# class Game:
#     def __init__(self): #, filename
#         pass


#     def search_for_start(self, read_lines_list):
#         y = 0
#         x = 0
#         while y < len(read_lines_list):
#             while x < len(read_lines_list[y]):
#                 if read_lines_list[y][x] == "X":
#                     start_coords = [y, x]
#                     return start_coords
#                 x +=1
#             y +=1

#     def current_coords(self, y, x):
#         self.x = x
#         self.y = y
#         return [self.y, self.x]

#     def gameMove(self, move):
#         pass

#     def read_lines_output(self, filename):
#         return read_lines(filename)

#     def parse_output(self, lines):
#         return parse(lines)

#     def search_for_start(self, read_lines_list):
#         y = 0
#         x = 0
#         while y < len(read_lines_list):
#             while x < len(read_lines_list[y]):
#                 if read_lines_list[y][x] == "X":
#                     start_coords = [y, x]
#                     return start_coords
#                 x +=1
#             y +=1

#     def grid_output(self, end_lines, player):
#         return grid_to_string(end_lines, player)


#     # def memory(self, cell):
#     #     self.memory = cell


# os.system("clear")
# p = Player() #init player
# g = Game() #init game
# victory_point = 0
# moves_list = []
# lines = g.read_lines_output("board_hard.txt") #reading lines convert into list of strings

# start_coords = g.search_for_start(lines) #searching for start "X" to place player
# current_coords = g.current_coords(start_coords[0],start_coords[1])
# #print(current_coords)


# parse_output = g.parse_output(lines) #changing strings into cells
# #print(parse_output)
# memory=parse_output[start_coords[0]][start_coords[1]] #placing cell which player is on in memory
# #print(memory)

# parse_output[start_coords[0]][start_coords[1]] = p #replacing start cell with player

# grid_output = g.grid_output(parse_output, p)
# print(grid_output)

# while True:
#     parse_output[current_coords[0]][current_coords[1]] = memory

#     # last_turn_coords = [current_coords[0], current_coords[1]]
#     # print(last_turn_coords)

#     user_movement = input("\nInput a move: ")
#     os.system("clear")
#     moves_list.append(user_movement)
#     movement = (p.move(user_movement))
#     current_coords[0] += movement[0] #changing y
#     current_coords[1] += movement[1] #changing x
#     if user_movement == "q":
#         print("\nBye!")
#         exit()

#     if user_movement == "e" and type(parse_output[current_coords[0]][current_coords[1]]) == Teleport:
#         parse_output[current_coords[0]][current_coords[1]] = p
#         for n, string in enumerate(parse_output):
#                 for i, cells in enumerate(string):
#                     if cells.display == memory.display:
#                         new_coords = [n, i]

#                         break
#         parse_output[current_coords[0]][current_coords[1]] = memory
#         current_coords = new_coords
#         parse_output[current_coords[0]][current_coords[1]] = p

#         grid_output = g.grid_output(parse_output, p)
#         print(grid_output)
#         print("\nWhoosh! The magical gates break Physics as we know it and opens a wormhole through space and time..")
#         continue
#     if user_movement == "e":
#         continue
#     #print(current_coords)
#     #memory = parse_output[current_coords[0]][current_coords[1]]
#     #print(memory)

#     #print(type(parse_output[current_coords[0]][current_coords[1]]))


#     if type(parse_output[current_coords[0]][current_coords[1]]) != Air:
#         if type(parse_output[current_coords[0]][current_coords[1]]) == Wall:
#             current_coords = parse_output[current_coords[0]][current_coords[1]].step_jank(current_coords, user_movement)
#             memory = parse_output[current_coords[0]][current_coords[1]]
#             parse_output[current_coords[0]][current_coords[1]] = p
#             grid_output = g.grid_output(parse_output, p)
#             print(grid_output)
#             print("\nYou walked into a wall. Oof!")

#         if type(parse_output[current_coords[0]][current_coords[1]]) == Start:
#             current_coords = parse_output[current_coords[0]][current_coords[1]].step_jank(current_coords, user_movement)
#             memory = parse_output[current_coords[0]][current_coords[1]]
#             parse_output[current_coords[0]][current_coords[1]] = p
#             grid_output = g.grid_output(parse_output, p)
#             print(grid_output)
#             print("\nYou walked into a wall. Oof!")

#         if type(parse_output[current_coords[0]][current_coords[1]]) == Water:
#             memory = Air()
#             p.add_bucket()
#             parse_output[current_coords[0]][current_coords[1]] = p
#             grid_output = g.grid_output(parse_output, p)
#             print(grid_output)
#             print("\nThank the Honourable Furious Forest, you've found a bucket of water!")
# #should outsource these functions to the cell.py
#         if type(parse_output[current_coords[0]][current_coords[1]]) == Fire:
#             if p.num_water_buckets <= 0:
#                 parse_output[current_coords[0]][current_coords[1]] = p
#                 grid_output = g.grid_output(parse_output, p)
#                 print(grid_output)
#                 print("\nYou step into the fires and watch your dreams disappear :(")
#                 break
#             if p.num_water_buckets > 0:
#                 p.remove_bucket()
#                 memory = Air()
#                 parse_output[current_coords[0]][current_coords[1]] = p
#                 grid_output = g.grid_output(parse_output, p)
#                 print(grid_output)
#                 print("\nWith your strong acorn arms, you throw a water bucket at the fire. You acorn roll your way through the extinguished flames!")


#         if type(parse_output[current_coords[0]][current_coords[1]]) == Teleport:
#             memory = parse_output[current_coords[0]][current_coords[1]]
#             parse_output[current_coords[0]][current_coords[1]] = p

#             for n, string in enumerate(parse_output):
#                 for i, cells in enumerate(string):
#                     if cells.display == memory.display:
#                         new_coords = [n, i]

#             parse_output[current_coords[0]][current_coords[1]] = memory
#             current_coords = new_coords
#             parse_output[current_coords[0]][current_coords[1]] = p

#             grid_output = g.grid_output(parse_output, p)
#             print(grid_output)
#             print("\nWhoosh! The magical gates break Physics as we know it and opens a wormhole through space and time..")




#         if type(parse_output[current_coords[0]][current_coords[1]]) == End:
#             parse_output[current_coords[0]][current_coords[1]] = p
#             grid_output = g.grid_output(parse_output, p)
#             print(grid_output)
#             victory_point +=1
#             print("\nYou conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable Furious Forest Throne, restoring your hometown back to its former glory of rainbow and sunshine! Peace reigns over the lands.")
#             break

#     else:
#         memory = parse_output[current_coords[0]][current_coords[1]]
#         parse_output[current_coords[0]][current_coords[1]] = p
#         grid_output = g.grid_output(parse_output, p)
#         print(grid_output)

# if victory_point == 0:
#     print("\nThe Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of ash and is scattered to the winds by the next storm... You have been roasted.")
#     print("\nYour made {} moves.".format(len(moves_list)))
#     joined_moves = ", ".join(moves_list)
#     print("Your moves: {}".format(joined_moves))
#     print("""
# =====================
# ===== GAME OVER =====
# =====================""")


# if victory_point > 0:
#     print("\nYour made {} moves.".format(len(moves_list)))
#     joined_moves = ", ".join(moves_list)
#     print("Your moves: {}".format(joined_moves))
#     print("""
# =====================
# ====== YOU WIN! =====
# =====================""")

# o = input()
# if o == "":
#     exit()
# #create while loop, while player is alive, keep goin
# #need to store in memory the cell which the player is sittin on