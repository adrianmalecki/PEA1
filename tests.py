from data import ReadData
from itertools import permutations
from sys import maxsize
import datetime


class Tests:
    def __init__(self):
        self.data = ReadData()



    def naive_algorithm_tests_version(self, graph, starting_city):
        perm = list(permutations([i + 1 for i in range(len(graph) - 1)]))

        min_pathweight = maxsize

        for permutation in perm:
            current_pathweight = 0
            k = starting_city

            for i in permutation:
                current_pathweight += graph[k][i]
                k = i
            current_pathweight += graph[k][starting_city]

            if current_pathweight < min_pathweight:
                min_pathweight = current_pathweight

        return min_pathweight

    def testing(self):
        for size in range(3, 11):
            graphs = self.data.generate_random_data(150, size)

            for i in range(50):
                self.naive_algorithm_tests_version(graphs[i], 0)
            start = datetime.datetime.now()
            for i in range(50, 150):
                self.naive_algorithm_tests_version(graphs[i], 0)
            duration = datetime.datetime.now() - start
            print('Rozmiar grafu: ', size)
            print('Średni czas: ', duration / 100)






