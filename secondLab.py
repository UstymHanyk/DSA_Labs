import pytest


def is_fit(rectangle_w, rectangle_h, N, square_side):
    rectangles_count = (square_side // rectangle_w) * (square_side // rectangle_h)
    return rectangles_count >= N


def find_smallest_square(N, W, H):
    if N not in range(1, 1012) or W not in range(1, 109) or H not in range(1, 109):
        return -1
    lower_bound = 1
    upper_bound = W * H * N

    while lower_bound < upper_bound:
        mid = lower_bound + (upper_bound - lower_bound) // 2
g
        if is_fit(W, H, N, mid):
            upper_bound = mid
        else:
            lower_bound = mid + 1

    return upper_bound


def test_find_smallest_square():
    assert find_smallest_square(10, 2, 3) == 9
    assert find_smallest_square(1, 3, 3) == 3
    assert find_smallest_square(2, 1000000000, 999999999) == -1


if __name__ == "__main__":
    pytest.main()

    width = 2
    height = 3
    count = 10
    print(find_smallest_square(count, width, height))
