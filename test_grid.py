from grid import grid_to_string
from game_parser import read_lines
from game_parser import parse

class Player:
    def __init__(self):
        self.num_water_buckets = 0
     
    def add_bucket(self):
        self.num_water_buckets +=1

    def change_bucket(self, change):
        self.num_water_buckets = change

p = Player()
o = Player()
o.add_bucket()
c = Player()
c.change_bucket("p")
d = Player()
d.change_bucket("")
e = Player()
e.change_bucket("!@#$%^&*()")



def test_grid():
    assert grid_to_string(parse(read_lines("board_test.txt")),p) == """*X*
*Y*

You have 0 water buckets.""", "Test case 1 failed"
    print("Simple Grid to String passed!")

    assert grid_to_string(parse(read_lines("board_test.txt")),o) == """*X*
*Y*

You have 1 water bucket.""", "Test case 2 failed"
    print("Increase Water Bucket to String passed!")

    assert grid_to_string(parse(read_lines("board_test.txt")),c) == """*X*
*Y*

You have p water buckets.""", "Test case 3 failed"
    print("Various amounts of water buckets case passed!")

    assert grid_to_string(parse(read_lines("board_test.txt")),d) == """*X*
*Y*

You have  water buckets.""", "Test case 4 failed"
    print("No water buckets case passed!")

    assert grid_to_string(parse(read_lines("board_test.txt")),e) == """*X*
*Y*

You have !@#$%^&*() water buckets.""", "Test case 5 failed"
    print("Various amounts of water buckets case 2 passed!")
    try:
        grid_to_string((1),e)
        print("Test Case Grid to String TypeError Failed!")
    except TypeError:
        print("Test Case Grid to String TypeError Passed!")
def run_tests():
    test_grid()
