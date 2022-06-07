import numpy as np
from math import inf


# do funkcji podaję zmienną fi, która bedzie zliczała zredukowane koszty
def redukcja_macierzy(matrix: list[list]):
    # wyznaczam minimalne wartości w poszczególnych wierszach
    fi_cols = 0
    fi_rows = 0
    min_in_rows = np.min(matrix, axis=1)
    for i in range(len(matrix)):
        # jeśli minimalna wartość nie jest równa 0, dodaję ją do fi i odejmuję we wszystkich kolumnach
        if min_in_rows[i] != 0 and min_in_rows[i] != inf:
            fi_rows += min_in_rows[i]
            for j in range(len(matrix[i])):
                matrix[i][j] -= min_in_rows[i]
    # wyznaczam minimalne wartosci w kolumnach
    min_in_cols = np.min(matrix, axis=0)
    for i in range(len(matrix[0])):
        # jeśli minimalna wartość nie jest równa 0, dodaję ją do fi i odejmuję we wszystkich wierszach
        if min_in_cols[i] != 0 and min_in_cols[i] != inf:
            fi_cols += min_in_cols[i]
            for j in range(len(matrix)):
                matrix[j][i] -= min_in_cols[i]
    return matrix, fi_rows, fi_cols


def wybor_przejscia(matrix):
    zera = {}
    for i in range (len(matrix)):
        for j in range (len(matrix[0])):
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


def wybranie_kroku(matrix, zera, LB):
    max_val = 0
    for i in zera.keys():
        if zera[i] > max_val:
            candidate = i
            max_val = zera[i]
    if max_val != inf:
        LB += max_val
    matrix[candidate[0]] = [inf for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        matrix[i][candidate[1]] = inf
    matrix[candidate[1]][candidate[0]] = inf
    return LB, matrix, candidate


# tab = [[inf, 2, 3, 4, 1, 3, 6, 5, 6, 8],
#        [9, inf, 4, 3, 8, 3, 5, 1, 6, 3],
#        [3, 4, inf, 4, 1, 6, 7, 2, 9, 3],
#        [8, 6, 2, inf, 3, 2, 6, 4, 5, 5],
#        [7, 4, 5, 3, inf, 7, 8, 3, 4, 6],
#        [2, 3, 1, 5, 7, inf, 2, 1, 5, 4],
#        [3, 4, 2, 8, 9, 1, inf, 5, 6, 3],
#        [8, 4, 5, 6, 1, 2, 3, inf, 6, 1],
#        [7, 2, 4, 5, 3, 6, 4, 7, inf, 5],
#        [4, 1, 3, 1, 6, 3, 7, 8, 9, inf]]
# x, rows, cols = redukcja_macierzy(tab)
# LB = rows + cols
# print(np.array(x))
# print('LB jest równe ', LB)
# zera = wybor_przejscia(x)
# print(zera)

results = []
LB = 0
matrix = [[inf, 5, 4, 6, 6],
          [8, inf, 5, 3, 4],
          [4, 3, inf, 3, 1],
          [8, 2, 5, inf, 6],
          [2, 2, 7, 0, inf]]

for i in range(len(matrix[0])):

    print(f"\nKROK {i+1}")
    matrix, rows, cols = redukcja_macierzy(matrix)
    if rows != inf:
        LB += rows
    if cols != inf:
        LB += cols
    print('LB jest równe ', LB)
    zera = wybor_przejscia(matrix)
    LB, matrix, candidate = wybranie_kroku(matrix, zera, LB)
    results.append(candidate)
    print(np.array(matrix))


print('\nwyniki:', results)