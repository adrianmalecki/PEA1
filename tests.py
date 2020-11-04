from data import ReadData
import datetime
import time
from naive import Naive
from branch_and_bound import Branch_And_Bound


class Tests:
    def __init__(self):
        self.data = ReadData()
        self.naive = Naive()
        self.branch_and_bound = Branch_And_Bound()

    def testing(self):
        TIME_LIMIT = 300
        for size in range(3, 11):
            graphs = self.data.generate_random_data(150, size)
            start = datetime.datetime.now()
            for i in range(50):
                self.naive.naive_algorithm(graphs[i], 0)
                if datetime.datetime.now() >= TIME_LIMIT + start:
                    print('Przerwano po', i, 'pomocniczych testach')
                    duration = datetime.datetime.now() - start
                    print('Rozmiar grafu: ', size)
                    print('Średni czas: ', duration / i)
                    break
            help_time = datetime.datetime.now() - start
            for i in range(50, 150):
                self.naive.naive_algorithm(graphs[i], 0)
                if datetime.datetime.now() >= TIME_LIMIT + start:
                    print('Przerwano po', i, 'pomocniczych testach')
                    duration = datetime.datetime.now() - start
                    print('Rozmiar grafu: ', size)
                    print('Średni czas: ', duration / i)
                    break
            duration = datetime.datetime.now() - start
            print('Rozmiar grafu: ', size)
            print('Średni czas: ', duration / 100)

        test = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 19, 21, 23, 25, 30, 35, 40, 45]
        for size in test:
            graphs = self.data.generate_random_data(150, size)
            start = datetime.datetime.now()
            for i in range(50):
                self.naive.naive_algorithm(graphs[i], 0)
                if datetime.datetime.now() - start > TIME_LIMIT:
                    print('Przerwano po', i, 'pomocniczych testach')
                    duration = datetime.datetime.now() - start
                    print('Rozmiar grafu: ', size)
                    print('Średni czas: ', duration / i)
                    break
            help_time = datetime.datetime.now() - start
            for i in range(50, 150):
                self.naive.naive_algorithm(graphs[i], 0)
                if datetime.datetime.now() - start > TIME_LIMIT:
                    print('Przerwano po', i, 'testach')
                    duration = datetime.datetime.now() - help_time
                    print('Rozmiar grafu: ', size)
                    print('Średni czas: ', duration / i - 50)
                    break
            duration = datetime.datetime.now() - help_time
            print('Rozmiar grafu: ', size)
            print('Średni czas: ', duration / 100)
