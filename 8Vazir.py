# # # Author : MMDSANE # # #
## Dear editor ; When i wrote this only god and i khow how this code works. Now only god knows.
## do not touch it PLEASE.
## DATE : 2024 / April / 22

from typing import List, Tuple
from pprint import pprint
import random

def empty_slots(board: List[List[int]]) -> List[Tuple[int, int]]:
    result = [(x//8, x%8) for x in range(64)]
    for i, row in enumerate(board):
        for j, slot in enumerate(row):
            if slot != 0:
                for k in range(8):
                    if (j, k) in result:
                        result.remove((j, k))
                    if (k, i) in result:
                        result.remove((k, i))
                for k in range(j, -1, -1):
                    if (k, i-abs(k-j)) in result:
                        result.remove((k, i-abs(k-j)))
                for k in range(j, 8):
                    if (k, i+abs(k-j)) in result:
                        result.remove((k, i+abs(k-j)))
                for k in range(i, -1, -1):
                    if (j+abs(k-i), k) in result:
                        result.remove((j+abs(k-i), k))
                for k in range(i, 8):
                    if (j-abs(k-i), k) in result:
                        result.remove((j-abs(k-i), k))

    return result

if __name__ == "__main__":
    left_queens = 8
    board = None

    while left_queens:
        left_queens = 8
        board = [[0] * 8 for _ in range(8)]

        while True:
            empty = empty_slots(board)
            if len(empty) == 0:
                break
            x, y = random.choice(empty)
            board[y][x] = 1
            left_queens -= 1

    pprint(board)
