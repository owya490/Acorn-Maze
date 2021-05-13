from player import Player

p = Player()

o = Player()
o.set_col(1)
o.set_row(2)
o.add_bucket()

a = Player()
a.remove_bucket()
def test_player():
    assert p.move("s") == [1, 0], "Player Move s failed!"
    print("Player Move s passed!")
    assert p.move("a") == [0, -1], "Player Move a failed!"
    print("Player Move a passed!")
    assert p.move("w") == [-1, 0], "Player Move w failed!"
    print("Player Move w passed!")
    assert p.move("d") == [0, 1], "Player Move d failed!"
    print("Player Move d passed!")
    assert p.move("e") == [0, 0], "Player Move e failed!"
    print("Player Move e passed!")

    assert p.move("S") == [1, 0], "Player Move S failed!"
    print("Player Move S passed!")
    assert p.move("W") == [-1, 0], "Player Move W failed!"
    print("Player Move W passed!")
    assert p.move("A") == [0, -1], "Player Move A failed!"
    print("Player Move A passed!")
    assert p.move("D") == [0, 1], "Player Move D failed!"
    print("Player Move D passed!")

    assert o.row == 2, "Player Row Test failed!"
    print("Player Row Test passed!")

    assert o.col == 1, "Player Col Test failed!"
    print("Player Col Test passed!")

    assert o.num_water_buckets == 1, "Player Waterbucket failed!"
    print("Player Waterbucket passed!")

    assert a.num_water_buckets == -1, "Player Waterbucket 2 failed!"
    print("Player Waterbucket 2 passed!")
    
    assert p.display == "A", "Player Display failed!"
    print("Player Display passed!")
def run_player():
    test_player()
