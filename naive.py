from itertools import permutations
from sys import maxsize

# klasa służąca do znajdowania rozwiązania metodą przeglądu zupełnego
class Naive:

    # # funkcja służąca do znajdowania rozwiązania
    def naive_algorithm(self, start_graph, starting_city):
        # wyznaczenie kolejnych możliwych ścieżek
        perm = permutations([i + 1 for i in range(len(start_graph) - 1)])

        cost = maxsize
        # obliczenie kosztu dla każdej możliwej ścieżki - permutacji
        for permutation in perm:
            path = [starting_city]
            current_pathweight = 0
            k = starting_city

            for i in permutation:
                current_pathweight += start_graph[k][i]
                k = i
                path.append(i)
            current_pathweight += start_graph[k][starting_city]
            path.append(starting_city)

            # sprawdzenie czy znależiona ścieżka jest najkrótsza
            if current_pathweight < cost:
                cost = current_pathweight
                min_path = path
        return cost, min_path


