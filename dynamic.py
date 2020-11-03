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
        queue = PriorityQueue()
        choosen_node = 0
        current_graph, bound = self.reduce_rows_and_columns(start_graph, 0)
      #  queue.put((bound, current_graph))
        nodes = [1, 2, 3, 4]
        for node in nodes:
            visited_nodes = [0]
            visited_nodes.append(node)
            cost = bound
            temp_graph = current_graph[:]
            print(visited_nodes)
            temp_graph = self.prepare_graph(temp_graph, choosen_node, node, visited_nodes)
            temp_graph, cost = self.reduce_rows_and_columns(temp_graph, cost)
            cost += current_graph[choosen_node][node]
            print(temp_graph)
            print(cost)

            queue.put((cost, node, temp_graph, visited_nodes))

        bound, choosen_node, current_graph, visited = queue.get()
        print(visited)
        visited2 = visited[:]
        nodes = [1, 2, 4]
        for node in nodes:
            cost = bound
            visited2 = visited[:]
            visited2.append(node)
            print(visited2)
            temp_graph = current_graph[:]
            temp_graph = self.prepare_graph(temp_graph, choosen_node, node, visited2)
            temp_graph, cost = self.reduce_rows_and_columns(temp_graph, cost)
            cost += current_graph[choosen_node][node]
            print(temp_graph)
            print(cost)
            queue.put((cost, node, temp_graph, visited2))


graph2 = [[-1, 20, 30, 10, 11],
          [15, -1, 16, 4, 2],
          [3, 5, -1, 2, 4],
          [19, 6, 18, -1, 3],
          [16, 4, 7, 16, -1]]

bab = Branch_And_Bound()
bab.find_solution(graph2)
