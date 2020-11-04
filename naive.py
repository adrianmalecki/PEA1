import datetime
from itertools import permutations
from sys import maxsize


class Naive:

    def __init__(self):
        pass

    def naive_algorithm(self, start_graph, starting_city):
        perm = permutations([i + 1 for i in range(len(start_graph) - 1)])

        cost = maxsize
        iteration = 0
        for permutation in perm:
            iteration += 1
            path = [starting_city]
            current_pathweight = 0
            k = starting_city

            for i in permutation:
                current_pathweight += start_graph[k][i]
                k = i
                path.append(i)
            current_pathweight += start_graph[k][starting_city]
            path.append(starting_city)

            if current_pathweight < cost:
                cost = current_pathweight
                min_path = path
        return cost, min_path




