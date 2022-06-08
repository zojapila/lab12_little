import numpy as np
from math import inf

# do funkcji podaję zmienną fi, która bedzie zliczała zredukowane koszty
def redukcja_macierzy(matrix):
    # wyznaczam minimalne wartości w poszczególnych wierszach
    fi_cols = 0
    fi_rows = 0
    min_in_rows = np.min(matrix, axis=1)
    for i in range(len(matrix)):
        # jeśli minimalna wartość nie jest równa 0, dodaję ją do fi i
        # odejmuję we wszystkich kolumnach
        if min_in_rows[i] != 0 and min_in_rows[i] != inf:
            fi_rows += min_in_rows[i]
            for j in range(len(matrix[i])):
                matrix[i][j] -= min_in_rows[i]
    # wyznaczam minimalne wartosci w kolumnach
    min_in_cols = np.min(matrix, axis=0)
    for i in range(len(matrix[0])):
        # jeśli minimalna wartość nie jest równa 0, dodaję ją do fi i
        # odejmuję we wszystkich wierszach
        if min_in_cols[i] != 0 and min_in_cols[i] != inf:
            fi_cols += min_in_cols[i]
            for j in range(len(matrix)):
                matrix[j][i] -= min_in_cols[i]
    return matrix, fi_rows, fi_cols

# funkcja zwracająca słownik zawierający współrzędne kolejnych zer
def wybor_przejscia(matrix):
    zera = {}
    # Czynność powtarzamy dla każdego elementu macierzy
    for i in range (len(matrix)):
        for j in range (len(matrix[0])):
            # Jeśli element jest równy 0 sumujemy najmniejszą wartość w
            # kolumnie i w wierszu zawierającym element (bez niego samego)
            # i zapisujemy wynik do słownika z danym odcinkiem (i,j)
            if matrix[i][j] is not inf:
                if matrix[i][j] == 0:
                    min_row = inf
                    min_col = inf
                    for x in range(len(matrix[i])):
                        if x != j:
                            if matrix[i][x] < min_row:
                                min_row = matrix[i][x]
                        if x != i:
                            if matrix[x][j] < min_col:
                                min_col = matrix[x][j]
                    zera[(i, j)] = min_col + min_row
    return zera

# Funkcja wyznaczająca potencjalnego kantydata na rozwiązanie
def wybranie_kroku(matrix, zera, LB):
    max_val = 0
    # Szukamy największego elementu
    for i in zera.keys():
        if zera[i] > max_val:
            candidate = i
            max_val = zera[i]
    # Znaleziony element dodajemy do aktualnej wartości LB
    if max_val != inf:
        LB += max_val
    matrix[candidate[0]] = [inf for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        matrix[i][candidate[1]] = inf
    matrix[candidate[1]][candidate[0]] = inf
    return LB, matrix, candidate

# Funkcja reazlizująca kolejne podproblemy po redukcji macierzy
def podproblem(matrix, LB, candidate):
    # Daną macierz kopiujemy, odznaczamy kolejny element (oznaczamy
    # jako inf), po czym wykonujemy redukcję, z któej otrzymane
    # wartości dodajemy do LB
    matrix2 = matrix.copy()
    matrix2[candidate[0]][candidate[1]] = inf
    matrix2, rows, cols = redukcja_macierzy(matrix2)
    LB2 = LB + rows + cols
    return matrix2, LB


if __name__ == '__main__':
    LB = 0
    matrix = [[inf, 2, 3, 4, 1, 3, 6, 5, 6, 8],
                [9, inf, 4, 3, 8, 3, 5, 1, 6, 3],
                [3, 4, inf, 4, 1, 6, 7, 2, 9, 3],
                [8, 6, 2, inf, 3, 2, 6, 4, 5, 5],
                [7, 4, 5, 3, inf, 7, 8, 3, 4, 6],
                [2, 3, 1, 5, 7, inf, 2, 1, 5, 4],
                [3, 4, 2, 8, 9, 1, inf, 5, 6, 3],
                [8, 4, 5, 6, 1, 2, 3, inf, 6, 1],
                [7, 2, 4, 5, 3, 6, 4, 7, inf, 5],
                [4, 1, 3, 1, 6, 3, 7, 8, 9, inf]]

    results = [None for i in range(len(matrix))]
    for i in range(len(matrix[0])):
        print(f"\nKROK {i + 1}")
        matrix, rows, cols = redukcja_macierzy(matrix)
        LB += rows + cols
        print('LB jest równe ', LB)
        zera = wybor_przejscia(matrix)
        LB_pom = LB
        LB, matrix, candidate = wybranie_kroku(matrix, zera, LB)
        LB2, matrix2 = podproblem(matrix, LB_pom, candidate)
        print("wartość lb podproblemu:", LB)
        results[candidate[0]] = (candidate[0] + 1, candidate[1] + 1)
        print(np.array(matrix))
    print('\nwyniki:', results)