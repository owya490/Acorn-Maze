from game import Game
import os
import sys

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

if len(sys.argv) < 2: #checking if there there is a sys.argv input
    print("Usage: python3 run.py <filename> [play]")
    exit()
filename = sys.argv[1]

p = Player() #init player
g = Game() #init game
victory_point = 0
moves_list = []

try:
    f = open(filename, 'r')
except FileNotFoundError:
    print("{} does not exist!".format(filename))
    exit()
    
lines = g.read_lines_output(filename) #reading lines convert into list of strings

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
    parse_output[current_coords[0]][current_coords[1]] = memory #storing the current cell in memory to place it back in after player moves off it


    user_movement = input("\nInput a move: ") #requesting a movement command from user
    if user_movement != "q" and user_movement != "e" and user_movement != "w" and user_movement != "a" and user_movement != "s" and user_movement != "d" and user_movement != "Q" and user_movement != "E" and user_movement != "W" and user_movement != "A" and user_movement != "S" and user_movement != "D":
        print(grid_output)
        print("\nPlease enter a valid move (w, a, s, d, e, q).")
        continue
    movement = (p.move(user_movement))
    current_coords[0] += movement[0] #changing y
    current_coords[1] += movement[1] #changing x


    if user_movement == "q": #for quitting
        print("\nBye!")
        exit()

    if user_movement == "e" and type(parse_output[current_coords[0]][current_coords[1]]) == Teleport: #implementing function that teleports player if they skip turn on teleport pad.
        moves_list.append(user_movement) #appending movement 

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
    if user_movement == "e": #implmenting the rest movement, where a turn is taken with no movement
        moves_list.append(user_movement) #appending movement 
        print(grid_output)
        continue



    if type(parse_output[current_coords[0]][current_coords[1]]) != Air:
        if type(parse_output[current_coords[0]][current_coords[1]]) == Wall: #implement wall interaction
            current_coords = parse_output[current_coords[0]][current_coords[1]].step_jank(current_coords, user_movement)
            memory = parse_output[current_coords[0]][current_coords[1]]
            parse_output[current_coords[0]][current_coords[1]] = p
            grid_output = g.grid_output(parse_output, p)
            print(grid_output)
            print("\nYou walked into a wall. Oof!")
        
        if type(parse_output[current_coords[0]][current_coords[1]]) == Start: #implement start cell interaction
            moves_list.append(user_movement) #appending movement 
            memory = parse_output[current_coords[0]][current_coords[1]]
            parse_output[current_coords[0]][current_coords[1]] = p
            grid_output = g.grid_output(parse_output, p)
            print(grid_output)


        if type(parse_output[current_coords[0]][current_coords[1]]) == Water: #implement water cell interaction where player water bucket increase
            moves_list.append(user_movement) #appending movement 
            memory = Air()
            p.add_bucket()
            parse_output[current_coords[0]][current_coords[1]] = p
            grid_output = g.grid_output(parse_output, p)
            print(grid_output)
            print("\nThank the Honourable Furious Forest, you've found a bucket of water!")

        if type(parse_output[current_coords[0]][current_coords[1]]) == Fire: #implement fire cell interaction where if player has water bucket can put out fire, or if none, will cause game over
            moves_list.append(user_movement) #appending movement 
            if p.num_water_buckets <= 0: #if player has no buckets, game ends
                parse_output[current_coords[0]][current_coords[1]] = p
                grid_output = g.grid_output(parse_output, p)
                print(grid_output)
                print()
                print("\nYou step into the fires and watch your dreams disappear :(.")
                break
            if p.num_water_buckets > 0: #if player has buckets, fire is put out and replaced with air
                p.remove_bucket()
                memory = Air()
                parse_output[current_coords[0]][current_coords[1]] = p
                grid_output = g.grid_output(parse_output, p)
                print(grid_output)
                print("\nWith your strong acorn arms, you throw a water bucket at the fire. You acorn roll your way through the extinguished flames!")

        
        if type(parse_output[current_coords[0]][current_coords[1]]) == Teleport: #teleports the player to the new location
            moves_list.append(user_movement) #appending movement 
            memory = parse_output[current_coords[0]][current_coords[1]]
            parse_output[current_coords[0]][current_coords[1]] = p
            
            for n, string in enumerate(parse_output): #searches the list for the exact same teleport, updating the players location to the new teleport exit location
                for i, cells in enumerate(string):
                    if cells.display == memory.display:
                        new_coords = [n, i]

            parse_output[current_coords[0]][current_coords[1]] = memory
            current_coords = new_coords
            parse_output[current_coords[0]][current_coords[1]] = p

            grid_output = g.grid_output(parse_output, p)
            print(grid_output)
            print("\nWhoosh! The magical gates break Physics as we know it and opens a wormhole through space and time.")


        

        if type(parse_output[current_coords[0]][current_coords[1]]) == End: #once player steps on end cell, game end will be initiated with victory screen
            moves_list.append(user_movement) #appending movement 
            parse_output[current_coords[0]][current_coords[1]] = p
            grid_output = g.grid_output(parse_output, p)
            print(grid_output)
            victory_point +=1
            print()
            print("\nYou conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable Furious Forest Throne, restoring your hometown back to its former glory of rainbow and sunshine! Peace reigns over the lands.")
            break

    else:
        moves_list.append(user_movement) #appending movement 
        memory = parse_output[current_coords[0]][current_coords[1]]
        parse_output[current_coords[0]][current_coords[1]] = p
        grid_output = g.grid_output(parse_output, p)
        print(grid_output)
    
    p.set_row(current_coords[0])
    p.set_col(current_coords[1])


if victory_point == 0: #determine if the game was loss if vicotry point is zero
    print("\nThe Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of ash and is scattered to the winds by the next storm... You have been roasted.")
    print("\nYou made {} moves.".format(len(moves_list)))
    joined_moves = ", ".join(moves_list)
    print("Your moves: {}".format(joined_moves.lower()))
    print("""
=====================
===== GAME OVER =====
=====================""")


if victory_point > 0: #if victory point is more than zero, then game is won and win screen printed
    if len(moves_list) == 1:
        print("\nYou made {} move.".format(len(moves_list)))
        joined_moves = ", ".join(moves_list)
        print("Your move: {}".format(joined_moves.lower()))
        print("""
=====================
====== YOU WIN! =====
=====================""")

    else:
        print("\nYou made {} moves.".format(len(moves_list)))
        joined_moves = ", ".join(moves_list)
        print("Your moves: {}".format(joined_moves.lower()))
        print("""
=====================
====== YOU WIN! =====
=====================""")

