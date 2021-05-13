from game_parser import read_lines
from game_parser import parse
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

def test_read_lines():
    assert read_lines("parsetest1.txt") == ["XY*11FW"], "Readline Test Case Failed!"
    print("Readlines Test Case Passed!")
def test_parse():
    assert type(parse(read_lines("parsetest1.txt"))[0][0]) == Start, "Parse Start Case Failed!"
    print("Parse Start Case Passed!")
    assert type(parse(read_lines("parsetest1.txt"))[0][1]) == End, "Parse End Case Failed!"
    print("Parse End Case Passed!")
    assert type(parse(read_lines("parsetest1.txt"))[0][2]) == Wall, "Parse Wall Case Failed!"
    print("Parse Wall Case Passed!")
    assert type(parse(read_lines("parsetest1.txt"))[0][3]) == Teleport, "Parse Teleport Case Failed!"
    print("Parse Teleport Case Passed!")
    assert type(parse(read_lines("parsetest1.txt"))[0][4]) == Teleport, "Parse Teleport Case Failed!"
    print("Parse Teleport Case Passed!")
    assert type(parse(read_lines("parsetest1.txt"))[0][5]) == Fire, "Parse Fire Case Failed!"
    print("Parse Fire Case Passed!")
    assert type(parse(read_lines("parsetest1.txt"))[0][6]) == Water, "Parse Water Case Failed!"
    print("Parse Water Case Passed!")
    try: 
        parse(read_lines("parsetest2.txt"))
        print("Parse ValueError case 1 Failed!")
    except ValueError:
        print("Parse ValueError case 1 Passed!")
    try: 
        parse(["Y"])
        print("Parse Missing X Failed!")
    except ValueError:
        print("Parse Missing X Passed!")
    try: 
        parse(["X"])
        print("Parse Missing Y Failed!")
    except ValueError:
        print("Parse Missing Y Passed!")
    try: 
        parse(["XY1"])
        print("Parse Teleporter Pairs Failed!")
    except ValueError:
        print("Parse Teleporter Pairs Passed!")
    
    #assert parse(read_lines("parsetest2.txt")) == raise ValueError

def run_tests():
    test_parse()
    test_read_lines()


