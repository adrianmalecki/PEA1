import random


class ReadData:

    # funkcja generująca losowe dane w liczbie - amount i o rozmiarze - size
    def generate_random_data(self, amount, size):
        list_of_graphs = []
        for i in range(amount):
            graph = []
            for row in range(size):
                rows = []
                for column in range(size):
                    if row == column:
                        rows.append(-1)
                    else:
                        rand = random.randint(1, 300)
                        rows.append(rand)
                graph.append(rows)
            list_of_graphs.append(graph)
        return list_of_graphs

    # funkcja zczytująca dane z pliku i umieszczająca je w liście - macierzy sąsiedztwa
    def read_data_from_file(self, filepath):


        f = open(filepath, 'r')


        list_of_graphs = []
        lines = f.readlines()
        number_of_line = 0

        # zczytywanie kolejnych linii pliku
        while lines:
            size = int(lines[number_of_line][:-1])
            number_of_line += 1
            graph = []
            for i in range(number_of_line, size + number_of_line):
                rows = []
                number = ''
                for item in lines[i]:
                    if item == ' ':
                        rows.append(int(number))
                        number = ''
                    elif item == '\n':
                        rows.append(int(number))
                        graph.append(rows)
                        number = ''
                    else:
                        number += item

            number_of_line += size
            if number_of_line >= len(lines):
                rows.append(int(number))
                graph.append(rows)
                list_of_graphs.append(graph)
                break
            list_of_graphs.append(graph)

        return list_of_graphs

    # funkcja zwracająca wybrany typ danych
    def get_data(self):

        print('1. Załaduj dane z pliku: ')
        print('2. Wygeneruj dane: ')
        choice = input('Wybór: ')

        if choice == '1':
            filepath = input('Podaj ścieżke pliku: ')
            # filepath = 'my_data.txt'
            if filepath[-4:] == '.txt':
                return self.read_data_from_file(filepath)
            else:
                print('Nie poprawna ścieżka')

        if choice == '2':
            amount = int(input('Liczba grafów do wygenerowania: '))
            size = int(input('Rozmiar generowanych grafów: '))
            return self.generate_random_data(amount, size)
