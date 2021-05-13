from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)


def read_lines(filename):
    """Read in a file and return the contents as a list of strings."""
    file = open(filename, "r")
    read_lines_list = []
    while True:
        line = file.readline()
        if line == "":
            break
        line = line.strip("\n")
        read_lines_list.append(line)
    file.close()
    return read_lines_list
    pass


def parse(lines):
    """Transform the input into a grid.

    Arguments:
        lines -- list of strings representing the grid

    Returns:
        list -- contains list of lists of Cells
    """
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
                raise ValueError ("Bad letter in configuration file: {}.".format(objects))
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
        raise ValueError ("Expected 1 starting position, got {}.".format(result_x))
    if result_y != 1:
        raise ValueError ("Expected 1 ending position, got {}.".format(result_y))
    if result_1 == 1 or result_1 > 2:            
        raise ValueError ("Teleport pad 1 does not have an exclusively matching pad.")
    if result_2 == 1 or result_2 > 2:            
        raise ValueError ("Teleport pad 2 does not have an exclusively matching pad.")
    if result_3 == 1 or result_3 > 2:            
        raise ValueError ("Teleport pad 3 does not have an exclusively matching pad.")
    if result_4 == 1 or result_4 > 2:            
        raise ValueError ("Teleport pad 4 does not have an exclusively matching pad.")
    if result_5 == 1 or result_5 > 2:            
        raise ValueError ("Teleport pad 5 does not have an exclusively matching pad.")
    if result_6 == 1 or result_6 > 2:            
        raise ValueError ("Teleport pad 6 does not have an exclusively matching pad.")
    if result_7 == 1 or result_7 > 2:            
        raise ValueError ("Teleport pad 7 does not have an exclusively matching pad.")
    if result_8 == 1 or result_8 > 2:            
        raise ValueError ("Teleport pad 8 does not have an exclusively matching pad.")
    if result_9 == 1 or result_9 > 2:            
        raise ValueError ("Teleport pad 9 does not have an exclusively matching pad.")
    
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
