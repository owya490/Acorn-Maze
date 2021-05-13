from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

start = Start()
end = End()
air = Air()
water = Water()
fire = Fire()
wall = Wall()
teleport = Teleport(1)
def test_cells():
    assert start.display == "X", "Test Start Display failed!"
    print("Test Start Display passed!")

    assert end.display == "Y", "Test End Display failed!"
    print("Testt End Display passed!")

    assert air.display == " ", "Test Air Display failed!"
    print("Test Air Display passed!")

    assert water.display == "W", "Test Water Display failed!"
    print("Test Water Display passed!")

    assert fire.display == "F", "Test Fire Display failed!"
    print("Test Fire Display passed!")

    assert wall.display == "*", "Test Wall Display failed!"
    print("Test Wall Dispaly passed!")

    assert teleport.display == "1", "Test Teleport Display failed!"
    print("Test Teleport Display passed!")

    assert wall.step_jank([0,0], "s") == [-1,0], "Wall Step s failed!"
    print("Wall Step s passed!")

    assert wall.step_jank([0,0], "a") == [0,1], "Wall Step a failed!"
    print("Wall Step a passed!")

    assert wall.step_jank([0,0], "d") == [0,-1], "Wall Step d failed!"
    print("Wall Step d passed!")

    assert wall.step_jank([0,0], "w") == [1,0], "Wall Step w failed!"
    print("Wall Step w passed!")


def run_cells():
    test_cells()
