import datetime
from itertools import permutations
from sys import maxsize
from queue import *

from numpy.ma import copy


class Branch_And_Bound:

    def __init__(self):
        pass

    def reduce_rows_and_columns(self, input_graph, bound):
        output_graph = input_graph[:]
        reduced_graph = []
        cost = 0
        for row in output_graph:
            reduced_row = []
            min_value_in_row = min((item for item in row if item >= 0), default=0)
            for item in row:
                if item > 0:
                    item = item - min_value_in_row
                reduced_row.append(item)
            cost += min_value_in_row
            reduced_graph.append(reduced_row)
        output_graph = reduced_graph

        reduced_graph = []
        min_value_in_columns = []
        size = len(output_graph)
        for i in range(size):
            min_value = maxsize
            for j in range(size):
                item = output_graph[j][i]
                if item >= 0:
                    min_value = min(min_value, item)
            if min_value == maxsize: min_value = 0
            cost += min_value
            min_value_in_columns.append(min_value)

        for row in output_graph:
            reduced_row = []
            i = 0
            for item in row:
                if item > 0:
                    item = item - min_value_in_columns[i]
                reduced_row.append(item)
                i += 1
            reduced_graph.append(reduced_row)
        cost += bound
        output_graph = reduced_graph
        return output_graph, cost

    def prepare_graph(self, input_graph, row, column, visited):
        size = len(input_graph)
        output_graph = []
        for r in range(size):
            temp = []
            for c in range(size):
                if r == row or c == column: # or (c == row and r == column):
                    temp.append(-1)
                elif c in visited[:-1] and r in visited[-1:]:
                    temp.append(-1)
                else:
                    temp.append(input_graph[r][c])
            output_graph.append(temp)
        return output_graph



    def find_solution(self, start_graph):
        size = len(start_graph)
        queue = PriorityQueue()
        choosen_node = 0
        current_graph, bound = self.reduce_rows_and_columns(start_graph, 0)
        main_path = [0]
        queue.put((bound, choosen_node, current_graph, main_path))
        while not queue.empty():
            bound, choosen_node, current_graph, main_path = queue.get()
            nodes = [i for i in range(size) if i not in main_path]
            for node in nodes:
                cost = bound
                current_path = main_path[:]
                current_path.append(node)
                temp_graph = current_graph[:]
                temp_graph = self.prepare_graph(temp_graph, choosen_node, node, current_path)
                temp_graph, cost = self.reduce_rows_and_columns(temp_graph, cost)
                cost += current_graph[choosen_node][node]
                queue.put((cost, node, temp_graph, current_path))
                print(cost)








graph2 = [[-1, 20, 30, 10, 11],
          [15, -1, 16, 4, 2],
          [3, 5, -1, 2, 4],
          [19, 6, 18, -1, 3],
          [16, 4, 7, 16, -1]]

bab = Branch_And_Bound()
bab.find_solution(graph2)
