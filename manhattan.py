import numpy as np
import queue
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)


class Manhattan_Solver:
    def __init__(self, board, prev_node, no_of_moves):
        self.board = board
        self.prev_node = prev_node
        self.no_of_moves = no_of_moves
        self.solution_list = []

    def get_solution(self):
        return self.solution()

    def get_moves(self):
        return self.no_of_moves

    def solution(self):
        start = self.board
        closed_list = []
        no_of_moves = 0
        pq = queue.PriorityQueue()
        g = 0
        h = start.get_manhattan()

        pq.put(PrioritizedItem(g + h, self))


        while not(pq.empty()):
            current_node = pq.get().item
            if (current_node.get_board().is_goal()):
                self.get_path(current_node)
                number_of_moves = len(self.solution_list) - 1
                print("The total number of moves:", number_of_moves)
                self.print_path()
                print("Found Goal")
                break

            # Insert current_node into closed_list
            closed_list.append(current_node.get_board())
            neighbours = current_node.get_board().neighbours()
            no_of_moves += 1

            for neighbour in neighbours:
                cost = no_of_moves + neighbour.get_manhattan()
                # Check if neighbour does not already exist in the closed_list
                if self.neighbour_in_list(neighbour, closed_list):
                    continue
                # Check if neighbour is in the priority queue already
                if not(self.find_existing_board(pq, neighbour)):
                    pq.put(PrioritizedItem(cost, Manhattan_Solver(neighbour, current_node, no_of_moves)))
                else:
                    other_node = self.find_neighbour(pq, neighbour)

                    if no_of_moves < other_node.item.no_of_moves:
                        other_node.item.no_of_moves = no_of_moves
                        other_node.item.board.cost = cost
                        other_node.item.prev_node = current_node

    def neighbour_in_list(self, neighbour, closed_list):
        """
        Checks for whether a given neighbour is found in the
        :param neighbour:
        :param closed_list:
        :return:
        """
        for item in closed_list:
            if np.array_equal(item.matrix, neighbour.matrix):
                return True
        return False

    def find_neighbour(self, pq, node):
        for i in pq.queue:
            if np.array_equal(i.item.board.matrix, node.matrix):
                return i

    def find_existing_board(self, pq, neighbour):
        for i in pq.queue:
            if np.array_equal(i.item.board.matrix, neighbour.matrix):
                return True
        return False


    def get_board(self):
        return self.board

    def get_path(self, node):
        if node.get_previous_node() == None:
            self.solution_list.append(node.get_board())
        else:
            self.solution_list.append(node.get_board())
            self.get_path(node.get_previous_node())

    def print_path(self):
        reverse = reversed(self.solution_list)
        for item in reverse:
            print(item)

    def get_previous_node(self):
        return self.prev_node

    def __str__(self):
        return f"Number of moves\n {self.board}, The previous board is \n {self.prev_node}"
    def get_previous_node(self):
        return self.prev_node



class manhattan_board:
    def __init__(self, matrix):
        self.matrix = matrix
        self.manhattan = self.manhattan()
        self.cost = 0

    def get_matrix(self):
        return self.matrix

    def __str__(self):
        altered_matrix = np.reshape(self.matrix, (3, 3))
        return f'{altered_matrix} \n'

    def manhattan(self) -> int:
        """
        Returns the manhattan distance
        :return:
        """
        manhattan = 0
        goal_board = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0])

        for i in range(1, len(self.matrix)):
            goal_pos = self.find_pos(i, goal_board)
            current_pos = self.find_pos(i, self.matrix)

            distance = abs(goal_pos[0] - current_pos[0]) + abs(goal_pos[1] - current_pos[1])
            manhattan += distance

        return manhattan

    def find_pos(self, n, array) -> tuple:
        """
        Finds the position of n in a given matrix
        :param n:
        :param array:
        :return:
        """
        # Reshapes the matrix
        new_array = np.reshape(array, (3, 3))
        for i in range(new_array.shape[0]):
            for j in range(new_array.shape[1]):
                if new_array[i][j] == n:
                    return (i, j)

    def neighbours(self) -> list:
        """
        Gets the neighbours of a given board
        :return:
        """
        positions = {0 : [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [4, 0, 6], 4: [3, 5, 1, 7], 5: [4, 2, 8], 6: [7, 3], 7: [6, 8, 4], 8: [7, 5]}

        empty_tile_position = 0
        neighbour = []
        new_boards = []


        for i in range((self.matrix).shape[0]):
            if self.matrix[i]  == 0:
                neighbour = positions[i]
                empty_tile_position = i

        for n in neighbour:
            new_array = np.copy(self.matrix)
            tmp = self.matrix[empty_tile_position] # Stores the position of 0
            new_array[empty_tile_position] = new_array[n]
            new_array[n] = tmp
            new_boards.append(manhattan_board(new_array))

        return new_boards

    def is_goal(self) -> bool:
        goal_board = manhattan_board(matrix=np.array([1, 2, 3, 4, 5, 6, 7, 8, 0]))
        if (np.array_equal(goal_board.get_matrix(), self.matrix)):
            return True
        return False

    def is_equal(self, other_board):
        if (np.array_equal(other_board, self.matrix)):
            return True
        return False

    def get_manhattan(self):
        return self.manhattan


