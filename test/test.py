from src.main import find_shortest_path

def test_shortest_path_1():
    board_size = 8
    start_position = (7, 0)
    destination_position = (0, 7)
    assert find_shortest_path(board_size, start_position, destination_position) == 6

def test_shortest_path_2():
    board_size = 8
    start_position = (0, 0)
    destination_position = (2, 2)
    assert find_shortest_path(board_size, start_position, destination_position) == 4

def test_no_path():
    board_size = 1
    start_position = (0, 0)
    destination_position = (1, 1)
    assert find_shortest_path(board_size, start_position, destination_position) == -1
