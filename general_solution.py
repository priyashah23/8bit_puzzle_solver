import numpy as np
from manhattan import *
from hamming import *

def main():
    print("Welcome to the sliding puzzle!")
    starting_input = input("Enter start board")
    starting_board = board(matrix=np.array(perform_checks(starting_input)))
    manhattan_start = manhattan_board(matrix=np.array(perform_checks(starting_input)))
    print("The starting board is\n", starting_board)
    goal_input = input("Enter the goal board")
    goal_board = perform_checks(goal_input)
    print("The goal board is", goal_board)

    check_solvable(starting_board)

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
        new_list = []
        for char in string:
            char = int(char)
            new_list.append(char)
        return new_list


def check_solvable(start_board):
    no_of_inversions = 0
    for x in range(len(start_board.matrix) - 1):
        if start_board.matrix[x] > start_board.matrix[x + 1]:
            no_of_inversions += 1

    if no_of_inversions % 2 == 0:
        print("Not a solvable board")
        exit(1)


if __name__ == "__main__":
	main()

