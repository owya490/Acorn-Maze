import player

def grid_to_string(grid, player):
    """Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
    """
    string = []
    for lists in grid: #converting back the list of list of cells to characters/ their respective displays to allow for user viewing
        for objects in lists:
            string.append(objects.display)
        string.append("\n")
    if player.num_water_buckets == 1: #adding on the number of water buckets the user possess for user viewing
        string.append("\nYou have {} water bucket.".format(player.num_water_buckets))
    else:
        string.append("\nYou have {} water buckets.".format(player.num_water_buckets))
    string_joined = "".join(string)
    return string_joined

    pass