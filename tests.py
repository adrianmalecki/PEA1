from data import ReadData
import datetime
import time
from naive import Naive
from branch_and_bound import Branch_And_Bound

# funkcja służąca do testów czasowych algorytmów
class Tests:
    def __init__(self):
        self.data = ReadData()
        self.naive = Naive()
        self.branch_and_bound = Branch_And_Bound()

    # testy dla przeglądu zupełnego
    def testing_naive(self):
        for size in range(5, 12):
            graphs = self.data.generate_random_data(150, size) # generowanie losowych grafów
            help_time = 0
            total_time = 0
            for j in range(50):
                exec_time = time.time()
                self.naive.naive_algorithm(graphs[j], 0)
                exec_time = time.time() - exec_time
                help_time += exec_time
                if help_time >= 300.0:
                    break
            for i in range(50, 150):
                exec_time = time.time()
                self.naive.naive_algorithm(graphs[j], 0)
                exec_time = time.time() - exec_time # czas pojedynczego testu
                total_time += exec_time # sumowanie czasu
                if total_time >= 300.0:
                    print('Wykonano: ', i - 50, 'prób')
                    break
            print('Rozmiar grafu: ', size)
            print('Średni czas: ', total_time / (i - j))

    # testy dla metody podziału i ograniczen
    def testing_b_b(self):
        # rozmiary instancji poszczególnych testów
        test = [5,6,7,8,9,10,11,12,14,16,18,21]
        for size in test:
            graphs = self.data.generate_random_data(150, size)
            help_time = 0
            total_time = 0
            for j in range(50):
                exec_time = time.time()
                self.branch_and_bound.find_solution(graphs[j], 0)
                exec_time = time.time() - exec_time
                help_time += exec_time
                if help_time >= 300.0:
                    break
            for i in range(50, 150):
                exec_time = time.time()
                self.branch_and_bound.find_solution(graphs[i], 0)
                exec_time = time.time() - exec_time # czas pojedynczego testu
                total_time += exec_time # sumowanie czasu
                if total_time >= 300.0:
                    print('Wykonano: ', i - 50, 'prób')
                    break
            print('Rozmiar grafu: ', size)
            print('Średni czas: ', total_time / (i-j))