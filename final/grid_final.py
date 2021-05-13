import player

def grid_to_string(grid, player):
    """Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
    """
    grid[player.row][player.col] = player
    string = []
    for lists in grid:
        for objects in lists:
            string.append(objects.display)
        string.append("\n")

    if player.num_water_buckets == 1:
        string.append("\nYou have {} water bucket.".format(player.num_water_buckets))
    else:
        string.append("\nYou have {} water buckets.".format(player.num_water_buckets))
    string_joined = "".join(string)
    return string_joined