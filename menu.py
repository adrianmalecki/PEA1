import random
from itertools import permutations
from sys import maxsize
import datetime
from naive import Naive
from data import ReadData
from tests import Tests



filepath = "my_data.txt"

class Menu:
    def __init__(self):
        self.read_data = ReadData()
        self.naive = Naive()
        self.tests = Tests()
        self.data = []
        self.choice = 0
        self.starting_city = 0

    def main_menu(self):
        while self.choice != 6:
            print('_________MENU_________')
            print('1. Wybierz dane')
            print('2. Wyświetl dane')
            print('3. Brute force')
            print('4. Testy')
            self.choice = int(input('Wybór: '))

            if self.choice == 1:
                self.data = self.read_data.get_data()

            if self.choice == 2:
                print('Dane: ')
                for graph in self.data:
                    print('')
                    for row in graph:
                        print(row)

            if self.choice == 3:
                for graph in self.data:
                    start = datetime.datetime.now()
                    solution, path = self.naive.naive_algorithm(graph, self.starting_city)
                    duration = datetime.datetime.now() - start
                    print('Duration = ', duration)
                    print('Solution = ', solution)
                    print('Path = ', path)


            if self.choice == 4:
                print('1. Przegląd zupełny: ')
                print('2. Programowanie dynamiczne: ')
                choice = int(input('Wybór: '))
                if choice == 1:
                    self.tests.testing()





M = Menu()
M.main_menu()
