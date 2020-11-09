import random
from itertools import permutations
from sys import maxsize
import datetime
from naive import Naive
from branch_and_bound import Branch_And_Bound
from data import ReadData
from tests import Tests



filepath = "my_data.txt"

class Menu:
    def __init__(self):
        self.read_data = ReadData()
        self.naive = Naive()
        self.branch_and_bound = Branch_And_Bound()
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
            print('4. Branch and bound')
            print('5. Testy')
            print('6. Wyjście')

            self.choice = input('Wybór: ')

            if self.choice == '1':
                self.data = self.read_data.get_data()

            elif self.choice == '2':
                print('Dane: ')
                for graph in self.data:
                    print('')
                    for row in graph:
                        print(row)

            elif self.choice == '3':
                for graph in self.data:
                    start = datetime.datetime.now()
                    solution, path = self.naive.naive_algorithm(graph, self.starting_city)
                    duration = datetime.datetime.now() - start
                    print('Duration = ', duration)
                    print('Solution = ', solution)
                    print('Path = ', path)

            elif self.choice == '4':
                for graph in self.data:
                    start = datetime.datetime.now()
                    solution, path = self.branch_and_bound.find_solution(graph, self.starting_city)
                    duration = datetime.datetime.now() - start
                    print('Duration = ', duration)
                    print('Solution = ', solution)
                    print('Path = ', path)

            elif self.choice == '5':
                print('1. Brute force: ')
                print('2. Branch and bound: ')
                choice = int(input('Wybór: '))
                if choice == 1:
                    self.tests.testing_naive()
                if choice == 2:
                    self.tests.testing_b_b()

            elif self.choice == '6':
                exit()

            else:
                print("Wprowadz poprawną liczbę")

M = Menu()
M.main_menu()
