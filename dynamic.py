import datetime
from itertools import permutations
from sys import maxsize


class Branch_And_Bound:

    def __init__(self):

        pass

    def bound(self, graph):

        reduced_graph = []
        for row in graph:
            reduced_row = []
            min_value_in_row = min(item for item in row if item >= 0)
            for item in row:
                if item > 0:
                    item = item - min_value_in_row
                reduced_row.append(item)
            reduced_graph.append(reduced_row)
        graph = reduced_graph

        min_value_in_column = []
        size = len(graph)
        for i in range(size):
            min_value = maxsize
            for j in range(size):
                item = graph[j][i]
                if item >= 0:
                    min_value = min(min_value, item)
            min_value_in_column.append(min_value)
        reduced_graph = []
        for row in graph:
            reduced_row = []
            i = 0
            for item in row:
                if item > 0:
                    item = item - min_value_in_column[i]
                reduced_row.append(item)
                i += 1
            reduced_graph.append(reduced_row)
        graph = reduced_graph

        return graph

                







graph = [[-1, 20, 30, 10, 11],
         [15, -1, 16, 4, 2],
         [3, 5, -1, 2, 4],
         [19, 6, 18, -1, 3],
         [16, 4, 7, 16, -1]]


bab = Branch_And_Bound()
bab.bound(graph)

