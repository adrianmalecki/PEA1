import datetime
from itertools import permutations
from sys import maxsize


class Naive:

    def __init__(self):
        pass

    def naive_algorithm(self, graph, starting_city):
        perm = permutations([i + 1 for i in range(len(graph) - 1)])

        min_pathweight = maxsize
        iteration = 0
        for permutation in perm:
            iteration += 1
            path = [starting_city]
            current_pathweight = 0
            k = starting_city

            for i in permutation:
                current_pathweight += graph[k][i]
                k = i
                path.append(i)
            current_pathweight += graph[k][starting_city]
            path.append(starting_city)

            if current_pathweight < min_pathweight:
                min_pathweight = current_pathweight
                min_path = path
        return min_pathweight, min_path


    def naive_algorithm_test(self, graphs):
        start = datetime.datetime.now()
        for graph in graphs:
            self.naive_algorithm(graph, 0)
        duration = datetime.datetime.now() - start

        return duration



