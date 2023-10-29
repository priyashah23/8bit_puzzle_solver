import numpy as np
from manhattan import *
from hamming import *

def main():
    print("Welcome to the sliding puzzle!")
    starting_board = board(matrix=np.array([4, 3, 6, 8, 7, 1, 0, 5, 2]))
    manhattan_start = manhattan_board(matrix=np.array([4, 3, 6, 8, 7, 1, 0, 5, 2]))
    print("The starting board is\n", starting_board)
    goal_board = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    print("The goal board is", goal_board)

    print("Please select your heuristic")
    heuristic = int(input("1. Manhattan Distance\n2. Hamming Distance\n"))
    if heuristic == 1:
        Manhattan_Solver(manhattan_start, None, 0).solution()
    else:
        Hamming_Solver(starting_board, None, 0).solution()

def perform_checks(string) -> list:
    if len(string) != 9:
        print("String length is incorrect")
    else:
        string = list(int(string))
        print(string)



if __name__ == "__main__":
	main()

