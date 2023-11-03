from collections import deque


def is_valid_position(x, y, board_size):
    return 0 <= x < board_size and 0 <= y < board_size


def find_shortest_path(board_size, start, destination):
    possible_moves_x = [2, 2, -2, -2, 1, 1, -1, -1]
    possible_moves_y = [-1, 1, 1, -1, 2, -2, 2, -2]

    visited = [[False for _ in range(board_size)] for _ in range(board_size)]
    queue = deque([(start[0], start[1], 0)])

    visited[start[0]][start[1]] = True

    while queue:
        current_x, current_y, steps = queue.popleft()

        if (current_x, current_y) == destination:
            return steps

        for move in range(8):
            new_x, new_y = (
                current_x + possible_moves_x[move],
                current_y + possible_moves_y[move],
            )

            if (
                is_valid_position(new_x, new_y, board_size)
                and not visited[new_x][new_y]
            ):
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, steps + 1))

    return -1


if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    with open(input_file, "r") as file:
        board_size = int(file.readline().strip())
        start_position = tuple(map(int, file.readline().strip().split(",")))
        destination_position = tuple(map(int, file.readline().strip().split(",")))

    print(start_position)
    print(destination_position)
    shortest_path = find_shortest_path(board_size, start_position, destination_position)

    with open(output_file, "w") as file:
        file.write(str(shortest_path))
