from game import Game



g = Game()




def test_game():
    assert g.search_for_start(['*X*', '*Y*']) == [0, 1], "Search For Start Failed!"
    print("Search For Start Passed!")
    assert g.search_for_start(["X"]) == [0,0], "Search For Start 2 Failed!"
    print("Search For Start 2 Passed!")


def run_tests():
    test_game()
