import datetime
from itertools import permutations
from sys import maxsize
from queue import *

# klasa służąca do znajdowania rozwiązania metodą podziału i ograniczeń
class Branch_And_Bound:

    # redukcja wierszy i kolumn w celu wyznaczenia ograniczenia
    def reduce_rows_and_columns(self, input_graph, bound):
        output_graph = input_graph[:]
        reduced_graph = []
        cost = 0
        # redukcja wierszy
        for row in output_graph:
            reduced_row = []
            min_value_in_row = min((item for item in row if item >= 0), default=0) # znalezienie minimalnych wartości w wierszach
            for item in row:
                if item > 0:
                    item = item - min_value_in_row
                reduced_row.append(item)
            cost += min_value_in_row
            reduced_graph.append(reduced_row)
        output_graph = reduced_graph

        # znalezienie minimalnych wartości w kolumnach
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

        # redukcja kolumn
        reduced_graph = []
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

    # zablokowanie odpowiednich wierszy i kolumn dla dalszych redukcji
    def prepare_graph(self, input_graph, row, column, visited):
        size = len(input_graph)
        output_graph = []
        for r in range(size):
            temp = []
            for c in range(size):
                if r == row or c == column:
                    temp.append(-1)
                elif c in visited[:-1] and r in visited[-1:]:
                    temp.append(-1)
                else:
                    temp.append(input_graph[r][c])
            output_graph.append(temp)
        return output_graph

    # funkcja znajdująca rozwiązanie dla grafu
    def find_solution(self, start_graph, starting_city):
        size = len(start_graph)
        queue = PriorityQueue() # kolejka priorytetowa służąca do przechowywania danych, według najmniejszego ograniczenia
        chosen_node = starting_city
        current_graph, bound = self.reduce_rows_and_columns(start_graph, 0)
        main_path = [chosen_node]
        queue.put((bound, chosen_node, current_graph, main_path))
        while not queue.empty():
            bound, chosen_node, current_graph, main_path = queue.get()
            if len(main_path) == size and bound >= cost: # sprawdzenie czy ściężka zawiera wszystkie miasta, a ograniczenie jest mniejsze niż następne oczekujące w kolejce - jest to równoznaczne z znaleźieniem rozwiązania
                main_path.append(starting_city)
                return cost, main_path # zwrócenie rozwiązania

            nodes = [i for i in range(size) if i not in main_path]  # wyznaczenie 'dzieci' wierzchołka z najmniejszym ograniczeniem
            for node in nodes:
                cost = bound
                current_path = main_path[:]
                current_path.append(node)
                temp_graph = current_graph[:]
                temp_graph = self.prepare_graph(temp_graph, chosen_node, node, current_path)
                temp_graph, cost = self.reduce_rows_and_columns(temp_graph, cost)
                cost += current_graph[chosen_node][node]
                queue.put((cost, node, temp_graph, current_path))


